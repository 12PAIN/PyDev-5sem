# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(10, 40, 550, 550))
        self.image.setText("")
        self.image.setObjectName("image")
        self.rotateRight = QtWidgets.QPushButton(self.centralwidget)
        self.rotateRight.setGeometry(QtCore.QRect(10, 600, 151, 28))
        self.rotateRight.setObjectName("rotateRight")
        self.rotateLeft = QtWidgets.QPushButton(self.centralwidget)
        self.rotateLeft.setGeometry(QtCore.QRect(170, 600, 181, 28))
        self.rotateLeft.setObjectName("rotateLeft")
        self.redButton = QtWidgets.QPushButton(self.centralwidget)
        self.redButton.setGeometry(QtCore.QRect(360, 600, 111, 28))
        self.redButton.setObjectName("redButton")
        self.blueButton = QtWidgets.QPushButton(self.centralwidget)
        self.blueButton.setGeometry(QtCore.QRect(480, 600, 111, 28))
        self.blueButton.setObjectName("blueButton")
        self.greenButton = QtWidgets.QPushButton(self.centralwidget)
        self.greenButton.setGeometry(QtCore.QRect(600, 600, 111, 28))
        self.greenButton.setObjectName("greenButton")
        self.makeOriginal = QtWidgets.QPushButton(self.centralwidget)
        self.makeOriginal.setGeometry(QtCore.QRect(600, 560, 111, 28))
        self.makeOriginal.setObjectName("makeOriginal")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(650, 60, 22, 491))
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setProperty("value", 255)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rotateRight.setText(_translate("MainWindow", "Повернуть по часовой"))
        self.rotateLeft.setText(_translate("MainWindow", "Повернуть против часовой"))
        self.redButton.setText(_translate("MainWindow", "Только красный"))
        self.blueButton.setText(_translate("MainWindow", "Только синий"))
        self.greenButton.setText(_translate("MainWindow", "Только зеленый"))
        self.makeOriginal.setText(_translate("MainWindow", "Оригинал"))
