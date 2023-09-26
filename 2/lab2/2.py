import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from form2 import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.setFixedSize(412,480)
        self.tasks = []
        self.pushButton.clicked.connect(self.taskHandler)
    def taskHandler(self):
        date = self.calendarWidget.selectedDate().toPyDate()
        plan = self.lineEdit.text()
        time = self.timeEdit.time().toPyTime()
        self.listWidget.addItem(f'{date} {time} - {plan}')



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls,exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())