#-*- coding:utf-8 -*-
import os
import LOG
import readBinfile

def getBinRootDir():
    filePath = os.getcwd()
    # fileRootDir = os.path.join(os.path.dirname(filePath), 'output')
    fileRootDir = os.path.join(filePath, 'output')
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
    filename = os.path.splitext(filename)[0]
    # print('getData',fileRootDir,filename)
    if filename == 'g_pdschedf_debug':
        return LOG.pdschedf_debug(fileRootDir)
    elif filename == 'g_rxfft_debug':
        return LOG.pufft_debug(fileRootDir)
    elif filename == 'g_cpri_debug':
        return LOG.cpri_debug(fileRootDir)
    elif filename == 'g_cpriDebugOutTime':
        return LOG.cpri_overTimeCnt(fileRootDir)
    elif filename == 'g_eftpe_debug':
        return LOG.eftpe_debug(fileRootDir)
    elif filename == 'g_puschedf_debug':
        return LOG.puschEdf_debug(fileRootDir)
    else:        
        if 'gPhyDebug' in filename:
            return readBinfile.ReadFile_debug(fileRootDir, filename+'.bin')
        elif 'sys_param' in filename:
            return readBinfile.ReadFile_debug(fileRootDir, filename+'.bin')
        elif 'gErrLog' in filename:
            return readBinfile.ReadFile_debug(fileRootDir, filename+'.bin')
        elif 'gEvtMgrCnt' in filename:
            return readBinfile.ReadFile_debug(fileRootDir, filename+'.bin')
        elif 'gEvtWaitCnt' in filename:
            return readBinfile.ReadFile_debug(fileRootDir, filename+'.bin')
        elif 'gcsReport' in filename:
            return readBinfile.ReadFile_debug(fileRootDir, filename+'.bin')
        elif 'gcsBuf' in filename:
            return readBinfile.ReadFile_debug(fileRootDir, filename+'.bin')
        

    return None,None

def getCells():
    fileRootDir = getBinRootDir()
    lists = getChildrenDIR(fileRootDir)
    return lists

def getBinFilesInCell(cell):
    celldir = os.path.join(getBinRootDir(), cell)
    return getChildrenFiles(celldir,"bin")



if __name__ == '__main__':
    files = getData("cell","celdddl1.bin")
    print(os.getcwd())
    print(getBinRootDir())
        