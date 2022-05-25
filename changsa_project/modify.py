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
        
def 设置数据(df,userLabel,param,value):
    myIndex = -1
    # for index, row in df.iterrows():        
    #     if str(row['UserLabel']).startswith(userLabel):
    #         myIndex = index
    #         break
    source_df = df[df['UserLabel'].str.startswith(userLabel)]  
    if source_df.empty == False:
    # if myIndex != -1:
        if value != None and value !='' and value !='0':
            myIndex = source_df.index.tolist()[0]
            df.loc[myIndex ,param] = str(value)

def 修改参数(param_df,myfiles):
    for zipfilename in myfiles:
        file = 解压(zipfilename)       
        print('filename=' + file)
        file_firstLine = 读取文件第一行(file)
        df = pd.read_csv(file,sep='|',header=1,encoding='utf-8',dtype=str)    
        for index,row in param_df.iterrows():        
        # for userLabel in userLabels:           
            userLabel = row['UserLabel']
            param = row['param']                 
            value = row['value']
            source_df = df[df['UserLabel'].str.startswith(userLabel)]  
            if source_df.empty == False:
                if value != None and value !='' and value !='0':
                    myIndex = source_df.index.tolist()[0]
                    df.loc[myIndex ,param] = str(value)
            # print(userLabel,param,value)
            # if userLabel != None:
                设置数据(df,userLabel,param,value)
        df['UserLabel'] = df.apply(lambda x : '\"%s\"' %x['UserLabel'] ,axis=1)
        df.to_csv(file ,index=False,sep='|',quoting=csv.QUOTE_NONE)
        写入文件第一行(file ,file_firstLine)
        file_modify_time = os.path.getmtime(zipfilename)
        file_modify_time_tmp = time.localtime(file_modify_time)
        file_modify_date = time.strftime("%Y-%m-%d %H:%M:%S", file_modify_time_tmp)
        # print(file_modify_date)
        # 修改文件时间(file)
        modify_file_create_time(file, file_modify_date, file_modify_date, file_modify_date)
        zipfile = 压缩(file)
        # 修改文件时间(zipfile)
        modify_file_create_time(zipfile, file_modify_date, file_modify_date, file_modify_date)
        print('=======success======')
        os.remove(file)
        
def 修改文件时间(file):
    # filename =  file[file.rfind('/')+1:]  #文件名
    # riqi = filename[31:39]
    # file_date = riqi[0:4] + '-' + riqi[4:6] + '-' + riqi[6:8]
    # if file.endswith('120000-15-001.csv') or file.endswith('120000-15-001.csv.zip'):
    #     file_date = file_date + ' 12:15:00'
    # if file.endswith('121500-15-001.csv') or file.endswith('121500-15-001.csv.zip'):
    #     file_date = file_date + ' 12:30:00'
    # if file.endswith('123000-15-001.csv') or file.endswith('123000-15-001.csv.zip'):
    #     file_date = file_date + ' 12:45:00'
    # if file.endswith('124500-15-001.csv') or file.endswith('124500-15-001.csv.zip'):
    #     file_date = file_date + ' 13:00:00'
    file_date  = os.path.getmtime(file)
    modify_file_create_time(file, file_date, file_date, file_date)

        
    print(file)

if __name__ == '__main__':    
    param_df=pd.read_excel('modify.xlsx',dtype=str)   
    if os.path.exists(distDIR) == False:
        os.mkdir(distDIR)
        
    # param_df = pd.read_json('modify.json')
    # print(param_pf)
    # userLabels = [
    #                 '长沙浏阳小河乡新河村鳄鱼嘴湾AU393987DP-SFH',
    #                 '邵阳洞口县石江镇石塘村皮基站ENB281297PZ-QFH'
    #               ]
    # zipfilename = 'PM-ENB-EUTRANCELLTDD-A1-V3.5.0-20220417170000-15-001.csv.zip'
    files =  os.listdir('.')
    myfiles = [x for x in files if x.startswith('PM-ENB-EUTRANCELLTDD-A1-V3.5.0-') and x.endswith('.zip')]
    print(myfiles)
    try:
        修改参数(param_df,myfiles)
        # for zipfilename in myfiles:
        #     file = 解压(zipfilename)       
        #     print('filename=' + file)
        #     file_firstLine = 读取文件第一行(file)
        #     df = pd.read_csv(file,sep='|',header=1,encoding='utf-8',dtype=str)    
        #     for index,row in param_df.iterrows():        
        #     # for userLabel in userLabels:           
        #         userLabel = row['UserLabel']
        #         param = row['param']                 
        #         value = row['value']
        #         print(userLabel,param,value)
        #         if userLabel != None:
        #             设置数据(df,userLabel,param,value)
        #     df['UserLabel'] = df.apply(lambda x : '\"%s\"' %x['UserLabel'] ,axis=1)
        #     df.to_csv(file ,index=False,sep='|',quoting=csv.QUOTE_NONE)
        #     写入文件第一行(file ,file_firstLine)
        #     压缩(file)
        #     print('=======success======')
        #     os.remove(file)
    except Exception as e:
            # traceback.print_exc()
        print('Error in main:',str(e))

    




    
