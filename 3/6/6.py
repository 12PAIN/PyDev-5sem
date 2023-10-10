import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from form import Ui_MainWindow

import passwdCheckUtil as pwd
import phoneNumberCheckUtil as ph

# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.setFixedSize(509,122)
        self.pushButton.clicked.connect(self.handleRegistration)

    def handleRegistration(self):

        try:

            passwd = self.lineEdit_2.text()
            phoneNumber = self.lineEdit_3.text()

            pwd.checkPassword(passwd)
            ph.checkNumber(phoneNumber)

            self.statusbar.showMessage(f'Успех! Вы зарегистрированы!')
        except pwd.LetterError:
            self.statusbar.showMessage(f'Ошибка! Ваш пароль не содержит больших или маленьких букв!')
        except pwd.DigitError:
            self.statusbar.showMessage(f'Ошибка! Ваш пароль не содержит цифр!')
        except pwd.LengthError:
            self.statusbar.showMessage(f'Ошибка! Длина пароля меньше 8 символов!')
        except pwd.SequenceError:
            self.statusbar.showMessage(f'Ошибка! Ваш пароль содержит последовательности!')
        except ph.NumberFormatException:
            self.statusbar.showMessage(f'Ошибка! Неверный формат номера телефона!')
        except ph.NumberLengthException:
            self.statusbar.showMessage(f'Ошибка! Неверный номер телефона. Мало цифр!')
        except ph.WrongOperatorException:
            self.statusbar.showMessage(f'Ошибка! Оператор вашего номера телефона не найден!')
        except ph.CountryCodeException:
            self.statusbar.showMessage(f'Ошибка! Неверный код страны в номере телефона!')

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls,exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())