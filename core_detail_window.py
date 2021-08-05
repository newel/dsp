
import Ui_core_detail_window

import sys
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets



class Core_detail_window(QtWidgets.QMainWindow,Ui_core_detail_window.Ui_MainWindow):
    
    def __init__(self, parent =None):
        super(Core_detail_window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('此处为标题')
        self.treeWidget_variable_init()
        self.bindTriggered()


    def treeWidget_variable_init(self):
        '''
            初始化变量数据
        '''        
        parent = None
        for x in range(1,4097):      
            if parent == None:
                parent=QTreeWidgetItem(self.treeWidget_variable)
                parent.setText(0,'变量名称'+str(x))
                parent.setText(1,'变量值'+str(x))
                parent.setText(2,'变量类型'+str(x))
                parent.setText(3,'地址'+str(x))
                parent.setText(4,'显示模式'+str(x))
            else:
                child1=QTreeWidgetItem(parent)
                child1.setText(0,'变量名称'+str(x))
                child1.setText(1,'变量值'+str(x))
                child1.setText(2,'变量类型'+str(x))
                child1.setText(3,'地址'+str(x))
                child1.setText(4,'显示模式'+str(x))
                parent = child1
        self.treeWidget_variable.expandAll()

    def bindTriggered(self):
        '''
            事件绑定
        '''
        self.treeWidget_variable.clicked.connect(self.treeWidget_variable_triggered)
        self.button_refresh.clicked.connect(self.treeWidget_variable_triggered)

    def treeWidget_variable_triggered(self):
        # print('treeWidget_variable triggered')
        pass

        


if __name__ == '__main__':
    app = QApplication(sys.argv) 
    mainWindow = Core_detail_window()
    mainWindow.show()
    sys.exit(app.exec_())
    