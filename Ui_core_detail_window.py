# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\dsp\core_detail_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeWidget_variable = QtWidgets.QTreeWidget(self.tab)
        self.treeWidget_variable.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.treeWidget_variable.setObjectName("treeWidget_variable")
        self.gridLayout_2.addWidget(self.treeWidget_variable, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setInputMethodHints(QtCore.Qt.ImhSensitiveData|QtCore.Qt.ImhUppercaseOnly)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.button_refresh = QtWidgets.QPushButton(self.tab)
        self.button_refresh.setObjectName("button_refresh")
        self.horizontalLayout.addWidget(self.button_refresh)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.treeWidget_ram = QtWidgets.QTreeWidget(self.tab_2)
        self.treeWidget_ram.setGeometry(QtCore.QRect(10, 10, 521, 431))
        self.treeWidget_ram.setObjectName("treeWidget_ram")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "core0"))
        self.treeWidget_variable.headerItem().setText(0, _translate("MainWindow", "变量名称"))
        self.treeWidget_variable.headerItem().setText(1, _translate("MainWindow", "变量值"))
        self.treeWidget_variable.headerItem().setText(2, _translate("MainWindow", "变量类型"))
        self.treeWidget_variable.headerItem().setText(3, _translate("MainWindow", "地址"))
        self.treeWidget_variable.headerItem().setText(4, _translate("MainWindow", "显示模式"))
        self.checkBox.setText(_translate("MainWindow", "改写"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.pushButton_2.setText(_translate("MainWindow", "添加变量"))
        self.button_refresh.setText(_translate("MainWindow", "刷新"))
        self.pushButton_3.setText(_translate("MainWindow", "定时刷新"))
        self.pushButton_5.setText(_translate("MainWindow", "导出节点"))
        self.pushButton_4.setText(_translate("MainWindow", "导入节点"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "变量查看"))
        self.treeWidget_ram.headerItem().setText(0, _translate("MainWindow", "1"))
        self.treeWidget_ram.headerItem().setText(1, _translate("MainWindow", "New Column"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "内存查看"))