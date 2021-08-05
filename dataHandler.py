#-*- coding:utf-8 -*-
import os
import LOG

def getBinRootDir():
    filePath = os.getcwd()
    fileRootDir = os.path.join(os.path.dirname(filePath), 'output')
    return fileRootDir


def getChildrenDIR(path):
    list = []
    if (os.path.exists(path)):
        files = os.listdir(path)
        for file in files:
            m = os.path.join(path,file)
            if (os.path.isdir(m)):
                h = os.path.split(m)                
                list.append(h[1])
    return list

def getChildrenFiles(file_dir,fileType):
    childrenFiles=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.'+fileType:  
                childrenFiles.append(file)
    return childrenFiles 


def getData(cellText,filename):  
    fileRootDir = os.path.join(getBinRootDir(), cellText)
    print('getData',fileRootDir)
    if filename == 'g_pdschedf_debug.bin':
        return LOG.pdschedf_debug(fileRootDir)
    elif filename == 'g_rxfft_debug.bin':
        return LOG.pufft_debug(fileRootDir)
    return None,None

def getCells():
    fileRootDir = getBinRootDir()
    lists = getChildrenDIR(fileRootDir)
    return lists

def getBinFilesInCell(cell):
    celldir = os.path.join(getBinRootDir(), cell)
    return getChildrenFiles(celldir,"bin")



if __name__ == '__main__':
    files = getBinFilesInCell("cell1")
    print(files)
        