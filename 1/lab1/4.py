import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox

morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•',
         'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••', 'j': '•———',
         'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———',
         'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'
         }

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def morzeHandler(self):
        self.lineEdit.setText(self.lineEdit.text() + self.sender().property("morzeCode"))

    def initUI(self):
        self.setGeometry(300, 100, 600, 850)
        self.setWindowTitle('Task4')

        i = 0
        for letter in morze.keys():
            btn = QPushButton(letter, self)
            btn.setProperty("morzeCode", morze[letter])
            btn.clicked.connect(self.morzeHandler)
            i += 30
            btn.move(15, i)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(200,425)
        self.lineEdit.resize(390,30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())