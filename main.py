import Ui_main_window

import sys, random
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore,  QtWidgets

import dataHandler

class Main(QtWidgets.QMainWindow,Ui_main_window.Ui_MainWindow):
    
    def __init__(self, parent =None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        # self.setWindowTitle('此处为标题')
        # self.treeWidget_variable_init()
        self.tableWidgets = []      
        self.listWidgets =[]  
        self.cells = cells = dataHandler.getCells()
        # self.initListWidget()
        self.init_tab_page_ui()        
        self.bindTriggered()
        
        
        # self.listWidgetChanged()
    def initListWidget(self):
        '''
            初始化listWidget
        '''
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)



    def bindTriggered(self):
        '''
            事件绑定
        '''
        # self.listWidget.itemClicked.connect(self.listWidgetChanged)
        self.tabWidget.currentChanged.connect(self.tabWidgetChanged)

    def tabWidgetChanged(self):
        firstFilename = self.listWidgets[0].item(0).text()
        self.loadData(firstFilename)

    def listWidgetChanged(self,item):        
        '''
            list点击之后的事件，需要重新刷新table
        '''
        filename = str(item.text())
        self.loadData(filename)

    def loadData(self,currentFileName):
        currentTabIndex = self.tabWidget.currentIndex() #当前选中的tab下标
        self.cellText = self.cells[currentTabIndex]
        self.currentFileName = currentFileName
        columns,datas = dataHandler.getData(self.cellText,currentFileName)  #根据点击获取数据
        tableWidget = self.tableWidgets[currentTabIndex]
        if datas == None:
            tableWidget.setRowCount(0)#行数
            tableWidget.setColumnCount(0)#列数
        else:
            tableWidget.setRowCount(len(datas))#行数
            tableWidget.setColumnCount(len(columns))#列数
            tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#所有列自动拉伸，充满界面
            tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
            tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
            tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows);  # 设置只有行选中
            tableWidget.setHorizontalHeaderLabels(columns) #横向标题排列，如果使用setVerticalHeaderLabels则是纵向排列标题
            for i in range(len(datas)):#注意上面列表中数字加单引号，否则下面不显示(或者下面str方法转化一下即可)
                item=datas[i]
                for j in range(len(item)):
                    item = QTableWidgetItem(str(datas[i][j]))
                    tableWidget.setItem(i,j,item)

    

  
    
    def init_tab_page_ui(self):        
        self.cellText = self.cells[0]  #默认第一个
        for cell in self.cells:
            tab_cell1 = QtWidgets.QWidget()
            tab_cell1.setObjectName(cell)
            gridLayout_2 = QtWidgets.QGridLayout(tab_cell1)
            gridLayout_2.setObjectName("gridLayout_"+cell) 
            
            listWidget = QtWidgets.QListWidget(tab_cell1)
            listWidget.setMinimumSize(QtCore.QSize(256, 0))
            listWidget.setObjectName("listWidget_"+cell)
            listWidget.itemClicked.connect(self.listWidgetChanged)
            self.listWidgets.append(listWidget)
            binFiles = dataHandler.getBinFilesInCell(cell)
            for binFile in binFiles:
                item = QtWidgets.QListWidgetItem()
                item.setText(binFile)
                listWidget.addItem(item)
            gridLayout_2.addWidget(listWidget, 0, 0, 1, 1, QtCore.Qt.AlignLeft)


            tableWidget = QtWidgets.QTableWidget(tab_cell1)
            tableWidget.setObjectName("tableWidget_"+cell)
            tableWidget.setColumnCount(10)
            tableWidget.setRowCount(20)
            self.tableWidgets.append(tableWidget)
            gridLayout_2.addWidget(tableWidget, 0, 1, 1, 1)
            self.tabWidget.addTab(tab_cell1, cell)


        
