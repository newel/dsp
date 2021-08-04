import sys
import os
import subprocess

#coding=utf-8
import subprocess

def cmd_test(batfile):
    # cmd = 'cmd.exe d:/start.bat'
    p = subprocess.Popen("cmd.exe /c" + batfile, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    curline = p.stdout.readline()
    while (curline != b''):
        print(curline)
        curline = p.stdout.readline()
    p.wait()
    print(p.returncode)


if __name__=="__main__":
    filePath = os.getcwd()
    fileDir = os.path.dirname(filePath)
    batfile = fileDir + '\debugTools\start.ps1'
    subprocess.Popen("powershell.exe -ExecutionPolicy RemoteSigned -file "+batfile+ " arg1 arg2 arg3" ,shell=True)
    # subprocess.Popen(['powershell.exe', batfile,'hello'],shell=True)


   
    

