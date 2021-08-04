#-*- coding:utf-8 -*-
import os
import LOG

def getBinRootDir():
    filePath = os.getcwd()
    fileRootDir = os.path.dirname(filePath) + '/output'
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


def getData(cellText,filename):  
    fileRootDir = getBinRootDir() + "/"+cellText
    if filename == 'g_pdschedf_debug':
        return LOG.pdschedf_debug(fileRootDir)
    elif filename == 'g_rxfft_debug':
        return LOG.pufft_debug(fileRootDir)

def getCells():
    fileRootDir = getBinRootDir()
    lists = getChildrenDIR(fileRootDir)
    return lists



if __name__ == '__main__':
    lists = getCells()
    print(lists)
        