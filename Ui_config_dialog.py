# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\PHYTools_v1.0\dsp\config_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 249)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_village = QtWidgets.QComboBox(Dialog)
        self.comboBox_village.setObjectName("comboBox_village")
        self.comboBox_village.addItem("")
        self.comboBox_village.addItem("")
        self.gridLayout.addWidget(self.comboBox_village, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.comboBox_dsp_type = QtWidgets.QComboBox(Dialog)
        self.comboBox_dsp_type.setObjectName("comboBox_dsp_type")
        self.comboBox_dsp_type.addItem("")
        self.comboBox_dsp_type.addItem("")
        self.comboBox_dsp_type.addItem("")
        self.gridLayout.addWidget(self.comboBox_dsp_type, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.input_ip = QtWidgets.QLineEdit(Dialog)
        self.input_ip.setObjectName("input_ip")
        self.gridLayout.addWidget(self.input_ip, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.button_bind = QtWidgets.QPushButton(Dialog)
        self.button_bind.setObjectName("button_bind")
        self.gridLayout.addWidget(self.button_bind, 4, 1, 1, 1)
        self.input_reserve = QtWidgets.QLineEdit(Dialog)
        self.input_reserve.setObjectName("input_reserve")
        self.gridLayout.addWidget(self.input_reserve, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "打开"))
        self.comboBox_village.setItemText(0, _translate("Dialog", "一小区"))
        self.comboBox_village.setItemText(1, _translate("Dialog", "二小区"))
        self.label.setText(_translate("Dialog", "IP"))
        self.comboBox_dsp_type.setItemText(0, _translate("Dialog", "B4860"))
        self.comboBox_dsp_type.setItemText(1, _translate("Dialog", "BSC9132"))
        self.comboBox_dsp_type.setItemText(2, _translate("Dialog", "5G"))
        self.label_4.setText(_translate("Dialog", "小区规格"))
        self.label_3.setText(_translate("Dialog", "芯片类型"))
        self.label_2.setText(_translate("Dialog", "保留"))
        self.button_bind.setText(_translate("Dialog", "Bind"))
