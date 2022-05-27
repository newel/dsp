#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'lxr'

from numpy import NaN
import pandas as pd
from soupsieve import select


if __name__ == '__main__':
    config_df = pd.read_excel('./config.xlsx') 
    result_column = None
    result_df = pd.DataFrame()
    for index,row in config_df.iterrows():    
        if row['type'] == 'result':
            result_column = row['value'].split(',')
        elif row['type'] == 'file_column':
            filename = row['key']
            if row['sheet'] != -1:
                file_df = pd.read_excel(filename,sheet_name=row['sheet'])
            else:
                file_df = pd.read_excel(filename)
            file_df['EnbType'] = 0
            file_df['NoX2'] = 1
            file_df['PLMNID'] = 46011
            file_df['LTENeighborCellId'] = 1
            
            if 'HC4G工参' in filename:
                pass   
            elif 'L网基础工参数据库' in filename:
                file_df['EnbType'] = file_df.apply(lambda x : 0 if x['小区覆盖类型'] == '宏站' else 1 ,axis=1)
            elif '诺基亚' in filename:
                file_df['EnbType'] = file_df.apply(lambda x : 0 if x['站点类型'] == '宏站' else 1 ,axis=1) 
            elif '京信' in filename:
                pass                           
             
            value = str(row['value'])
            select_column = value.split(",")            
            file_df = file_df[select_column]
            file_df.columns = result_column
            for x in range(1,33):
                file_df["pre_neName_"+str(x)] = file_df['neName'].shift(x,axis=0)     
            for x in range(1,33):
                file_df['LTENeighborCellId'] = file_df.apply(lambda item : 
                        x + 1 if  item['neName'] == item['pre_neName_'+str(x)] else item['LTENeighborCellId'],axis =1)
            # file_df.columns = result_column
            rtn_df = file_df[result_column]
            if result_df.empty:
                result_df = rtn_df
            else:
                result_df = pd.concat([result_df,rtn_df]) 
    
    result_df['小区名称'] = result_df.apply(lambda x : x['neName']+str(x['CID']) ,axis=1)
    result_df['mod3'] = result_df.apply(lambda x : x['PCI'] % 3  ,axis=1)
    # print(result_df.head())
    # print(result_df.tail())
    result_df.to_excel('merge.xlsx',index = False)
    