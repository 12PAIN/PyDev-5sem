from PyQt5.QtGui import QPolygon
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from random import choice, randint
from form1 import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.D_x, self.D_y = -1, -1
        self.x, self.y = -1, -1
        self.GOG = None
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black', 'Pink']

    def setupUi(self, Form):
        self.setMouseTracking(True)
        Form.resize(500, 500)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.RightButton:
            self.GOG = 1
        elif event.button() == Qt.LeftButton:
            self.GOG = -1
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.GOG = 2
        self.update()

    def mouseMoveEvent(self, event):
        self.D_x = event.x()
        self.D_y = event.y()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        if self.x > -1 and self.y > -1 and self.GOG == 1:
            qp.setBrush(QColor(choice(self.colors)))

            leigt = randint(50, 200)

            qp.drawRect(self.x - leigt // 2, self.y - leigt // 2, leigt, leigt)
            ex.show()

        elif self.x > -1 and self.y > -1 and self.GOG == -1:
            qp.setBrush(QColor(choice(self.colors)))

            leigt = randint(50, 200)

            qp.drawEllipse(self.x - leigt // 2, self.y - leigt // 2, leigt,
                           leigt)

        elif self.D_x > -1 and self.D_y > -1 and self.GOG == 2:
            qp.setBrush(QColor(choice(self.colors)))

            leigt = randint(50, 200)

            points = QPolygon(
                [QPoint((self.D_x + leigt // 2), (self.D_y + leigt // 2)),
                 # Правая
                 QPoint(self.D_x, self.D_y - leigt // 2),  # Верхушка
                 QPoint(self.D_x - leigt // 2,
                        self.D_y + leigt // 2)])  # Левая
            qp.drawPolygon(points)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = MyWindow()
    ex.show()
    exit(app.exec())
