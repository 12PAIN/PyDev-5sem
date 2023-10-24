import random
import sys

from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QInputDialog

from form import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)
        self.pushButton.clicked.connect(self.paint)

    def run(self):
        self.int_num = QInputDialog.getInt(self, "Определить количество флажков", "Введите количество флажков", 1, 1, 10, 1)

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()


    def draw_flag(self, qp):
        h1 = 60
        h2 = 30
        for i in range(self.int_num[0]):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            qp.drawRect(30, h2 * i + h1, 120, h2)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
