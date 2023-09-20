import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QPlainTextEdit
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QRect, QRegularExpression, QCoreApplication
from PyQt5.uic.properties import QtWidgets, QtCore
from PyQt5.QtCore import Qt


class MyApplication(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.decimalPoint = False
        self.operations = []
        self.currentOperation = 0

    def initUI(self):
        self.setGeometry(300, 100, 600, 850)
        self.setWindowTitle('Task5')

        self.setObjectName("MainWindow")
        self.resize(255, 331)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(40, 80, 40, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(80, 80, 40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(80, 120, 40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QRect(40, 120, 40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QRect(80, 160, 40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QRect(40, 160, 40, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QRect(120, 80, 40, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QRect(120, 120, 40, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QRect(120, 160, 40, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QRect(40, 200, 40, 40))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QRect(120, 200, 40, 40))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QRect(160, 80, 40, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QRect(160, 120, 40, 40))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QRect(160, 200, 40, 40))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QRect(160, 160, 40, 40))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QRect(80, 200, 40, 40))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QRect(160, 40, 40, 40))
        self.pushButton_17.setObjectName("pushButton_17")

        self.result = QPlainTextEdit(self.centralwidget)
        self.result.setGeometry(QRect(40, 40, 120, 40))
        self.result.setObjectName("resultField")
        self.result.setReadOnly(True)
        self.retranslateUi()

        for btn in self.findChildren(QPushButton):
            btn.clicked.connect(self.btnHandler)

    #     self.result.textChanged.connect(self.fieldAutoEditor)
    #
    # def fieldAutoEditor(self):
    #
    #     currentFieldText = self.result.toPlainText()
    #
    #     newTextField = (currentFieldText + '.')[:-1]
    #
    #     toDelete = []
    #     for i in range(0, len(newTextField)):
    #
    #         if newTextField[i].isdigit() == False and newTextField[i] != ".":
    #             toDelete.append(i)
    #
    #     for i in range(0, len(toDelete)):
    #         del newTextField[i]
    #
    #     if currentFieldText != newTextField:
    #         self.result.setPlainText(str(currentFieldText))
    #
    #     pass

    def btnHandler(self):

        action = self.sender().text()

        if action not in ("+", "-", "*", "/", "=", "<-", "."):
            # print(self.result.toPlainText())
            if self.result.toPlainText() in ("", "ОШИБКА!") or "Результат: " in self.result.toPlainText():
                self.result.setPlainText(action)
            else:
                currentValue = self.result.toPlainText()
                self.result.setPlainText(currentValue + action)

        elif action == "<-":

            if self.result.toPlainText() in ("", "ОШИБКА!") or "Результат: " in self.result.toPlainText():
                self.result.setPlainText("")
                return

            currentValue = self.result.toPlainText()
            currentValue = currentValue[:-1]
            self.result.setPlainText(currentValue)

        elif action == ".":

            if self.result.toPlainText() in ("", "ОШИБКА!") or "Результат: " in self.result.toPlainText():
                self.result.setPlainText("")
                return

            currentValue = self.result.toPlainText()
            self.result.setPlainText(currentValue + '.')

        elif action in ("+", "-", "*", "/"):

            if self.result.toPlainText() in ("", "ОШИБКА!") or "Результат: " in self.result.toPlainText():
                self.result.setPlainText("")
                return

            currentValue = self.result.toPlainText()

            if currentValue == "":
                self.result.setPlainText('ОШИБКА!')
                self.operations = []
                self.currentOperation = 0
                return

            self.currentOperation += 1
            currentValueFloat = float(currentValue)

            if len(self.operations) > 0:
                if currentValueFloat == 0.0 and self.operations[self.currentOperation - 1]["actionKey"] == "/":
                    self.result.setPlainText('ОШИБКА!')
                    self.operations = []
                    self.currentOperation = 0
                    return

            self.operations.append({"actionKey": action, "value": currentValueFloat})
            self.result.setPlainText('')

        elif action == "=":

            if self.result.toPlainText() in ("", "ОШИБКА!") or "Результат: " in self.result.toPlainText():
                self.result.setPlainText("")
                return

            if len(self.operations) == 0:
                return

            currentValue = self.result.toPlainText()

            if currentValue == "":
                self.result.setPlainText('ОШИБКА!')
                self.operations = []
                self.currentOperation = 0
                return

            currentValueFloat = float(currentValue)

            if len(self.operations) > 0:
                if currentValueFloat == 0.0 and self.operations[self.currentOperation - 1]["actionKey"] == "/":
                    self.result.setPlainText('ОШИБКА!')
                    self.operations = []
                    self.currentOperation = 0
                    return



            result = 0
            tmpOperationCode = ''
            tmpCurrentOperation = 0
            for operation in self.operations:

                if tmpCurrentOperation == 0:

                    tmpOperationCode = operation["actionKey"]
                    print(operation["value"])
                    tmpCurrentOperation += 1
                    result = operation["value"]
                elif tmpCurrentOperation != len(self.operations):

                    if tmpOperationCode == "+":
                        result += operation["value"]
                    elif tmpOperationCode == "-":
                        result -= operation["value"]
                    elif tmpOperationCode == "*":
                        result *= operation["value"]
                    elif tmpOperationCode == "/":
                        result /= operation["value"]

                    tmpOperationCode = operation["actionKey"]
                    tmpCurrentOperation += 1

            if tmpOperationCode == "+":
                result += currentValueFloat
            elif tmpOperationCode == "-":
                result -= currentValueFloat
            elif tmpOperationCode == "*":
                result *= currentValueFloat
            elif tmpOperationCode == "/":
                result /= currentValueFloat

            tmpOperationCode = self.operations[::-1][0]["actionKey"]
            tmpCurrentOperation += 1

            self.result.setPlainText('Результат: ' + str(result))
            self.operations =[]
            self.currentOperation = 0

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "5"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "8"))
        self.pushButton_6.setText(_translate("MainWindow", "7"))
        self.pushButton_7.setText(_translate("MainWindow", "3"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "="))
        self.pushButton_12.setText(_translate("MainWindow", "+"))
        self.pushButton_13.setText(_translate("MainWindow", "-"))
        self.pushButton_14.setText(_translate("MainWindow", "/"))
        self.pushButton_15.setText(_translate("MainWindow", "*"))
        self.pushButton_16.setText(_translate("MainWindow", "."))
        self.pushButton_17.setText(_translate("MainWindow", "<-"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApplication()
    ex.show()
    sys.exit(app.exec())
