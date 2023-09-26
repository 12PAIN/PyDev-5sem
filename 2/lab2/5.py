import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow
from form5 import Ui_MainWindow

def checkPlagiat(text1: str, text2: str, threshold: float):
    plagiatPercent = 0.0

    substrLen = 35

    for i in range(0, len(text1), substrLen):

        text1_idx = i if int(len(text1) / substrLen) >= (i / substrLen) else i % ((int(len(text1) / substrLen)) * substrLen)
        text2_idx = i if int(len(text2) / substrLen) >= (i / substrLen) else i % ((int(len(text2) / substrLen)) * substrLen)

        # print(text1_idx)
        # print(text2_idx)

        substr1 = text1[text1_idx:text1_idx+substrLen-1]
        substr2 = text2[text2_idx:text2_idx+substrLen-1]

        countEqualsSubStr = 0.0
        for j in range(0, substrLen):
            if substr1[0:j] in substr2:
                countEqualsSubStr = j+1

        # print(float(countEqualsSubStr) / (float(substrLen)/100.))

        equalityOfSubStrPercent = float(countEqualsSubStr) / (float(substrLen)/100.)

        if equalityOfSubStrPercent >= threshold:
            plagiatPercent += float(substrLen) / (float(len(text1)) / 100.)


    return plagiatPercent if plagiatPercent < 100 else 100.0

# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonCheckPlagiatClicked)

    def buttonCheckPlagiatClicked(self):
        text1 = self.textEdit.toPlainText()
        text2 = self.textEdit_2.toPlainText()
        threshold = float(self.doubleSpinBox.text().replace(",", "."))

        plagiatPercent = checkPlagiat(text1, text2, threshold)

        self.statusBar.showMessage(f'Текст похож на {round(plagiatPercent, 2)}%')

        if plagiatPercent <= 30:
            self.statusBar.setStyleSheet('background-color: green')
        elif plagiatPercent > 30 and plagiatPercent <= 65:
            self.statusBar.setStyleSheet('background-color: yellow')
        else:
            self.statusBar.setStyleSheet('background-color: red')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls,exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())