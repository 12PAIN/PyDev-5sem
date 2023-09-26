import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from form3 import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.setFixedSize(268,390)
        self.tasks = []
        self.pushButton.clicked.connect(self.contactAdd)

    def contactAdd(self):
        name = self.lineEdit.text()
        number = self.lineEdit_2.text()
        self.listWidget.addItem(f'{name}: {number}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls,exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())