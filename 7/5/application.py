import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow

from form1 import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Task 5')

        self.paintButton.stateChanged.connect(self.changeColorFunc)
        self.hideButton.stateChanged.connect(self.hideButtonFunc)
        self.changeText.stateChanged.connect(self.changeTextFunc)
        self.enlargeFontOnButton.stateChanged.connect(self.enlargeFontFunc)
        self.disableButton.stateChanged.connect(self.disableButtonFunc)

    def changeColorFunc(self):
        if self.paintButton.isChecked():
            self.pushButton.setStyleSheet('QPushButton {background-color: red}')
        else:
            self.pushButton.setStyleSheet('QPushButton {background-color: #fdfdfd}')

    def hideButtonFunc(self):
        if self.hideButton.isChecked():
            self.pushButton.setVisible(False)
        else:
            self.pushButton.setVisible(True)

    def changeTextFunc(self):
        if self.changeText.isChecked():

            self.pushButton.setText("Текст изменён")
        else:
            self.pushButton.setText("Button")

    def enlargeFontFunc(self):
        if self.enlargeFontOnButton.isChecked():
            self.pushButton.setFont(QFont('Times', 18))
        else:
            self.pushButton.setFont(QFont('Times', 12))

    def disableButtonFunc(self):
        if self.disableButton.isChecked():
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
