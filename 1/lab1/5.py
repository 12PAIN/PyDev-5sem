import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QRect, QRegularExpression
from PyQt5.uic.properties import QtWidgets, QtCore
from PyQt5.QtCore import Qt

menu = {
    'Кола':50,
    'Бургер':150,
    'Чизбургер': 200,
    'Пицца': 370,
    'Коктейль':100
}

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.check = {pos: 0 for pos in menu.keys()}
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 600, 850)
        self.setWindowTitle('Task5')

        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 450, 200))
        self.menuLayout = QVBoxLayout(self.verticalLayoutWidget)
        # self.menuLayout = QVBoxLayout(self)
        # self.menuLayout.setGeometry(QRect(30, 30, 150, 150))
        self.menuLayout.setSpacing(3)
        self.menuLayout.setContentsMargins(5, 5, 5, 5)

        self.LCDS = {}

        for position in menu.keys():

            positionLayout = QHBoxLayout()
            positionLayout.setSpacing(15)
            positionLayout.setContentsMargins(5,5,5,5)

            posLabel = QLabel(self.verticalLayoutWidget)
            posLabel.setText(position)

            posPriceLabel = QLabel(self.verticalLayoutWidget)
            posPriceLabel.setText(' Цена:' + str(menu[position]) + ' руб.')

            btn_add = QPushButton('+', self.verticalLayoutWidget)
            btn_add.resize(1,1)
            btn_add.setProperty("position", position)
            btn_add.clicked.connect(self.menuHandler)

            btn_minus = QPushButton('-', self.verticalLayoutWidget)
            btn_minus.resize(1,1)
            btn_minus.setProperty("position", position)
            btn_minus.clicked.connect(self.menuHandler)

            LCD_count = QLCDNumber(self.verticalLayoutWidget)
            LCD_count.setProperty("position", position)
            self.LCDS.__setitem__(position, LCD_count)

            positionLayout.addWidget(posLabel)
            positionLayout.addWidget(posPriceLabel)
            positionLayout.addWidget(LCD_count)
            positionLayout.addWidget(btn_add)
            positionLayout.addWidget(btn_minus)

            self.menuLayout.addLayout(positionLayout)

        self.verticalLayoutWidgetCheck = QWidget(self)
        self.verticalLayoutWidgetCheck.setGeometry(QRect(30, 350, 550, 300))
        self.checkLayout = QVBoxLayout(self.verticalLayoutWidgetCheck)
        # self.menuLayout = QVBoxLayout(self)
        # self.menuLayout.setGeometry(QRect(30, 30, 150, 150))
        self.checkLayout.setSpacing(3)
        self.checkLayout.setContentsMargins(5, 5, 5, 5)

        positionLayout = QHBoxLayout()
        positionLayout.setSpacing(15)
        positionLayout.setContentsMargins(5, 5, 5, 5)
        positionLayout.setObjectName(position + '_layout_total_order_check')

        posTotalLabel = QLabel(self.verticalLayoutWidgetCheck)

        totalSum = 0

        for pos in self.check.keys():
            totalSum += self.check[pos] * menu[pos]

        posTotalLabel.setText('К оплате:' + str(totalSum))
        posTotalLabel.setObjectName(position + '_total_order_check')

        positionLayout.addWidget(posTotalLabel)
        self.checkLayout.addLayout(positionLayout)
        self.checkLayout.setAlignment(Qt.AlignTop)



    def menuHandler(self):
        if self.sender().text() == '+':
            position = self.sender().property('position')
            self.check[position] += 1
            self.LCDS[position].display(self.check[position])
        else:
            position = self.sender().property('position')
            self.check[position] -= 1 if self.check[position] > 0 else 0
            self.LCDS[position].display(self.check[position])


        for layout in self.checkLayout.findChildren(QHBoxLayout):
            self.checkLayout.removeItem(layout)
            layout.deleteLater()

        for widget in self.verticalLayoutWidgetCheck.findChildren(QWidget, QRegularExpression(".*_check")):
            widget.deleteLater()

        positionLayout = QHBoxLayout()
        positionLayout.setSpacing(15)
        positionLayout.setContentsMargins(5, 5, 5, 5)
        positionLayout.setObjectName(position + '_layout_total_order_check')

        posTotalLabel = QLabel(self.verticalLayoutWidgetCheck)

        totalSum = 0

        for pos in self.check.keys():
            totalSum += self.check[pos] * menu[pos]

        posTotalLabel.setText('К оплате:' + str(totalSum))
        posTotalLabel.setObjectName(position + '_total_order_check')

        positionLayout.addWidget(posTotalLabel)
        self.checkLayout.addLayout(positionLayout)

        for position in self.check.keys():

            if self.check[position] == 0: continue

            positionLayout = QHBoxLayout()
            positionLayout.setSpacing(15)
            positionLayout.setContentsMargins(5, 5, 5, 5)
            positionLayout.setObjectName(position + '_layout_check')

            posLabel = QLabel(self.verticalLayoutWidgetCheck)
            posLabel.setText(position)
            posLabel.setObjectName(position + '_label_name_check')

            posPriceLabel = QLabel(self.verticalLayoutWidgetCheck)
            posPriceLabel.setText('Цена:' + str(menu[position]) + ' руб.')
            posPriceLabel.setObjectName(position + '_price_check')

            posCountLabel = QLabel(self.verticalLayoutWidgetCheck)
            posCountLabel.setText('Количество:' + str(self.check[position]))
            posCountLabel.setObjectName(position + '_count_check')

            posTotalLabel = QLabel(self.verticalLayoutWidgetCheck)
            posTotalLabel.setText('Общая цена:' + str(self.check[position] * menu[position]))
            posTotalLabel.setObjectName(position + '_total_check')

            positionLayout.addWidget(posLabel)
            positionLayout.addWidget(posPriceLabel)
            positionLayout.addWidget(posCountLabel)
            positionLayout.addWidget(posTotalLabel)

            self.checkLayout.addLayout(positionLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())