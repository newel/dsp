import pandas as pd
import csv
import zipfile
import os

import time

import win32timezone

import pywintypes
from win32con import FILE_FLAG_BACKUP_SEMANTICS
from win32con import FILE_SHARE_WRITE
from win32file import CloseHandle
from win32file import CreateFile
from win32file import GENERIC_WRITE
from win32file import OPEN_EXISTING
from win32file import SetFileTime

# import sys
# sys.setrecursionlimit(1000000) #设置递归深度

distDIR = './new'

def modify_file_create_time(path, create_time_str, update_time_str, access_time_str):
    """定义文件或文件夹的创建、修改、访问时间"""
    path = os.path.abspath(path)
    if os.path.exists(path):
        try:
            format_str = "%Y-%m-%d %H:%M:%S"  # 时间格式
            f = CreateFile(path, GENERIC_WRITE, FILE_SHARE_WRITE, None, OPEN_EXISTING,
                           FILE_FLAG_BACKUP_SEMANTICS, 0)
            create_time = pywintypes.Time(time.mktime(time.strptime(create_time_str, format_str)))
            update_time = pywintypes.Time(time.mktime(time.strptime(update_time_str, format_str)))
            access_time = pywintypes.Time(time.mktime(time.strptime(access_time_str, format_str)))
            SetFileTime(f, create_time, update_time, access_time)
            CloseHandle(f)
            print('成功:({})/({})/({})'.format(create_time_str, update_time_str, access_time_str))
        except Exception as e:
            print('失败:{}'.format(e))
    else:
        print('路径不存在:{}'.format(path))

def 解压(file):
    zip_f = zipfile.ZipFile(file)
    list_zip_f = zip_f.namelist() # zip文件中的文件列表名
    for zip_fn in list_zip_f:
        zip_f.extract(zip_fn, '.') # 第二个参数指定输出目录，此处保存在当前目录
        print("%s done" % zip_fn)
        zip_f.close()
        return zip_fn


def 压缩(csvfile):
    # 压缩文件位置
    zipPath = distDIR +'/'+csvfile+'.zip'
    # # 打开一个 ZIP 文件（以w覆盖的方式写入）
    ZipFile = zipfile.ZipFile(zipPath, 'w', zipfile.ZIP_DEFLATED)
    print(csvfile + '===begin zip===')
    ZipFile.write(csvfile , csvfile) # 写入压缩文件
    # 关闭归档文件。 你必须在退出程序之前调用 close() 否则将不会写入关键记录数据。
    ZipFile.close()
    print(csvfile + '===end zip===')
    return zipPath



def 读取文件第一行(fname):
    with open(fname, 'r', encoding='utf-8') as f:  # 打开文件
        lines = f.readlines()  # 读取所有行
        first_line = lines[0]  # 取第一行
        return first_line
    
def 写入文件第一行(filename,text):
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        # f.write(text + '\n' + content)
        f.write(text +  content)
        
def 设置数据(df,source_df,dist_index):    
    exclude_column = ['rmUID','Dn','UserLabel','startTime']
    for columnName,column in source_df.items():
        if columnName not in exclude_column:
            # print(dist_index,columnName,column.iloc[0])
            df.loc[dist_index,columnName] = str(column.iloc[0])


def 修改参数(param_df,myfiles):
    for zipfilename in myfiles:
        file = 解压(zipfilename)       
        print('filename=' + file)
        file_firstLine = 读取文件第一行(file)
        df = pd.read_csv(file,sep='|',header=1,encoding='utf-8',dtype=str) 
        for index,row in param_df.iterrows():   
            source_UserLabel = row['source']  
            dist_UserLabel = row['dist']        
            source_df = df[df['UserLabel'].str.startswith(source_UserLabel)]            
            dist_df = df[df['UserLabel'].str.startswith(dist_UserLabel)]
            # print(source_df.empty,dist_df.empty)
            if source_df.empty == False and dist_df.empty == False:
                dist_index = dist_df.index.tolist()[0]
                # print(source_df.index.tolist()[0],dist_index)
                设置数据(df,source_df,dist_index)
        
        df['UserLabel'] = df.apply(lambda x : '\"%s\"' %x['UserLabel'] ,axis=1)
        df.to_csv(file ,index=False,sep='|',quoting=csv.QUOTE_NONE)
        写入文件第一行(file ,file_firstLine)
        file_modify_time = os.path.getmtime(zipfilename)
        file_modify_time_tmp = time.localtime(file_modify_time)
        file_modify_date = time.strftime("%Y-%m-%d %H:%M:%S", file_modify_time_tmp)
        modify_file_create_time(file, file_modify_date, file_modify_date, file_modify_date)
        zipfile = 压缩(file)
        modify_file_create_time(zipfile, file_modify_date, file_modify_date, file_modify_date)
        print('=======success======')
        os.remove(file)

if __name__ == '__main__':    
    param_df=pd.read_excel('copyParam.xlsx',dtype=str)   
    if os.path.exists(distDIR) == False:
        os.mkdir(distDIR)
    # normal_UserLabel = '郴州苏仙贤良风电场上压站-ZFH'
    files =  os.listdir('.')
    myfiles = [x for x in files if x.startswith('PM-ENB-EUTRANCELLTDD-A1-V3.5.0-') and x.endswith('.zip')]
    print(myfiles)
    # try:
    修改参数(param_df,myfiles)
    # except Exception as e:
            # traceback.print_exc()
        # print('Error in main:',str(e))

    




    
