import sys

import numpy as np
from PyQt5.QtGui import QPixmap, qRgb, QTransform, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.uic.properties import QtCore

from form import Ui_MainWindow
# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.color = "RGB"
        self.angle = 0.0
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Отображение картинки')
        ## Изображение

        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        print(fname)

        self.original_image = QImage(fname[0])
        self.pixmap = QPixmap(self.original_image.copy())
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.__show_image()

        self.redButton.clicked.connect(self.changeImageMainColorChanel)
        self.greenButton.clicked.connect(self.changeImageMainColorChanel)
        self.blueButton.clicked.connect(self.changeImageMainColorChanel)

        self.rotateLeft.clicked.connect(self.rotateImage)
        self.rotateRight.clicked.connect(self.rotateImage)
        self.makeOriginal.clicked.connect(self.resetToOriginal)

    def resetToOriginal(self):
        self.angle = 0.0
        self.color = "RGB"
        self.__show_image()

    def __show_image(self):
        self.curr_image = self.original_image.copy().convertToFormat(QImage.Format_RGBA8888)

        imgPixelsPtr = self.curr_image.bits()
        imgPixelsPtr.setsize(self.curr_image.byteCount())

        cv_im_in = np.array(imgPixelsPtr, copy=True).reshape(
            self.curr_image.width(), self.curr_image.height(), 4)

        if "R" not in self.color:
            cv_im_in[:, :, 0] *= 0

        if "G" not in self.color:
            cv_im_in[:, :, 1] *= 0

        if "B" not in self.color:
            cv_im_in[:, :, 2] *= 0

        cv_im_in[:, :, 3] = 255

        self.curr_image = QImage(cv_im_in, cv_im_in.shape[1], cv_im_in.shape[0], QImage.Format_RGBA8888).transformed(
            QTransform().rotate(self.angle))
        self.pixmap = QPixmap(self.curr_image)
        self.pixmap = self.pixmap.scaled(self.image.width(), self.image.height())

        self.image.setPixmap(self.pixmap)

    def rotateImage(self):

        flag = -1 if self.sender().text() == "Повернуть против часовой" else 1
        self.angle = (self.angle + 90 * flag) % 360
        self.__show_image()

    def changeImageMainColorChanel(self):
        if self.sender().text() == "Только красный":
            self.color = "R"
        elif self.sender().text() == "Только синий":
            self.color = "B"
        elif self.sender().text() == "Только зеленый":
            self.color = "G"

        self.__show_image()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls,exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())