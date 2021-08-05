import Ui_config_dialog
import os
import sys, random
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QMessageBox
from PyQt5 import QtCore,  QtWidgets

import dataHandler
import config_dialog

class Config_dialog(QtWidgets.QDialog,Ui_config_dialog.Ui_Dialog):
    
    def __init__(self, parent =None):
        super(Config_dialog, self).__init__(parent)
        self.setupUi(self)
        self.bindTriggered()

    def bindTriggered(self):
        self.button_bind.clicked.connect(self.bindConfig)

    def bindConfig(self):
        '''
            点击bind按钮之后的处理
        '''
        QMessageBox.information(self, "提示", "如何绑定?")
        pass
        
    