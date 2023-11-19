# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playBtn = QtWidgets.QPushButton(Form)
        self.playBtn.setObjectName("playBtn")
        self.horizontalLayout_2.addWidget(self.playBtn)
        self.pauseBtn = QtWidgets.QPushButton(Form)
        self.pauseBtn.setObjectName("pauseBtn")
        self.horizontalLayout_2.addWidget(self.pauseBtn)
        self.stopBtn = QtWidgets.QPushButton(Form)
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout_2.addWidget(self.stopBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.playBtn.setText(_translate("Form", "запуск"))
        self.pauseBtn.setText(_translate("Form", "пауза"))
        self.stopBtn.setText(_translate("Form", "стоп"))
