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
        self.cells = cells = dataHandler.getCells()
        self.add_page()        
        self.bindTriggered()
        
        # self.listWidgetChanged()

    def bindTriggered(self):
        '''
            事件绑定
        '''
        self.listWidget.itemClicked.connect(self.listWidgetChanged)
        self.tab_widget.currentChanged.connect(self.tabWidgetChanged)

    def tabWidgetChanged(self):
        currentIndex = self.tab_widget.currentIndex()
        self.loadData(currentIndex,self.itemText)

    def listWidgetChanged(self,item):        
        '''
            list点击之后的事件，需要重新刷新table
        '''
        itemText = str(item.text())
        self.loadData(0,itemText)

    def loadData(self,cellIndex,itemText):
        self.cellText = self.cells[cellIndex]
        self.itemText = itemText
        columns,datas = dataHandler.getData(self.cellText,itemText)  #根据点击获取数据
        tableWidget = self.tableWidgets[cellIndex]
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

    

  
    
    def add_page(self):        
        for cell in self.cells:
            tab_cell1 = QtWidgets.QWidget()
            tab_cell1.setObjectName(cell)
            gridLayout_2 = QtWidgets.QGridLayout(tab_cell1)
            gridLayout_2.setObjectName("gridLayout_"+cell)            
            tableWidget = QtWidgets.QTableWidget(tab_cell1)
            tableWidget.setObjectName("tableWidget_"+cell)
            tableWidget.setColumnCount(10)
            tableWidget.setRowCount(20)
            self.tableWidgets.append(tableWidget)
            gridLayout_2.addWidget(tableWidget, 0, 1, 1, 1)
            self.tab_widget.addTab(tab_cell1, cell)


        
