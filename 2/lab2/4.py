import random
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from form4 import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.setFixedSize(332,538)

        self.rocksCount = 0

        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.lcdNumber.hide()
        self.label_2.hide()
        self.listWidget.hide()
        self.label_game_end.hide()

        self.pushButton.clicked.connect(self.startGame)
        self.pushButton_2.clicked.connect(self.handlePlayerAction)
        self.pushButton_3.clicked.connect(self.handlePlayerAction)
        self.pushButton_4.clicked.connect(self.handlePlayerAction)

    def startGame(self):
        self.label_game_end.hide()
        self.listWidget.clear()
        self.pushButton_4.setDisabled(False)
        self.pushButton_3.setDisabled(False)

        self.rocksCount = int(self.spinBox.text())
        if self.rocksCount > 0:
            self.lcdNumber.show()
            self.lcdNumber.display(self.rocksCount)
            self.pushButton_2.show()
            self.pushButton_3.show()
            self.pushButton_4.show()
            self.lcdNumber.show()
            self.label_2.show()
            self.listWidget.show()
            self.listWidget.addItem("Игра началась!")

        if self.rocksCount < 3:
            self.pushButton_4.setDisabled(True)

        if self.rocksCount < 2:
            self.pushButton_3.setDisabled(True)

    def endGame(self, winnerIsPlayer: bool):
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.lcdNumber.hide()
        self.label_2.hide()
        self.listWidget.hide()

        self.label_game_end.show()

        if winnerIsPlayer:
            self.label_game_end.setText("Вы выйграли!")
        else:
            self.label_game_end.setText("Вы проиграли!")

        self.rocksCount = 0

    def handlePlayerAction(self):
        btn_text = self.sender().text()
        playerTakes = int(btn_text.split(' ')[1])

        self.rocksCount -= playerTakes
        self.listWidget.addItem(f'Игрок берет {playerTakes}')
        self.lcdNumber.display(self.rocksCount)

        if self.rocksCount == 0:
            self.endGame(True)
            return

        if self.rocksCount < 3:
            self.pushButton_4.setDisabled(True)

        if self.rocksCount < 2:
            self.pushButton_3.setDisabled(True)

        self.computerAction()

    def computerAction(self):
        computerTakes = 0
        if self.rocksCount % 4 == 0:

            if self.rocksCount >= 4:
                computerTakes = random.randint(1, 3)
            else:
                computerTakes = self.rocksCount
        else:
            computerTakes = self.rocksCount % 4

        self.listWidget.addItem(f'Компьютер берет {computerTakes}')

        self.rocksCount -= computerTakes
        self.lcdNumber.display(self.rocksCount)

        if self.rocksCount == 0:
            self.endGame(False)
            return

        if self.rocksCount < 3:
            self.pushButton_4.setDisabled(True)

        if self.rocksCount < 2:
            self.pushButton_3.setDisabled(True)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls,exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())