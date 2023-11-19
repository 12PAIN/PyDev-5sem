import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(0, 0, 1500, 500)
        self.UFO = QPushButton(self)
        self.UFO.setIcon(QtGui.QIcon('UFO.png'))
        self.x, self.y = 0, 0
        self.UFO.setGeometry(0, 0, 50, 50)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.x = (self.x + 20) % 1500
        elif event.key() == Qt.Key_A:
            self.x = (self.x - 20) % 1500
        elif event.key() == Qt.Key_W:
            self.y = (self.y - 20) % 500
        elif event.key() == Qt.Key_S:
            self.y = (self.y + 20) % 500
        self.UFO.move(self.x, self.y)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
