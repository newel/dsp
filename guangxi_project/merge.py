#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'lxr'

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
            file_df = pd.read_excel(row['key'])
            value = str(row['value'])
            select_column = value.split(",")
            file_df = file_df[row['value'].split(",")]
            file_df.columns = result_column
            if result_df.empty:
                result_df = file_df
            else:
                result_df = pd.concat([result_df,file_df]) 
            # print(file_df.head())
            
    print(result_df.head())
    print(result_df.tail())
    # result_df.to_excel('merge.xlsx',index = False)
    