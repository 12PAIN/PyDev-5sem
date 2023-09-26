import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from form1 import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.setFixedSize(259,617)
        self.pushButton.clicked.connect(self.handleFlag)

    def handleFlag(self):
        self.label.setText(f'Флаг: {self.buttonGroup.checkedButton().text()}, {self.buttonGroup_2.checkedButton().text()}, {self.buttonGroup_3.checkedButton().text()}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls,exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())