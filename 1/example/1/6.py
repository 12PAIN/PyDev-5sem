import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Шестая программа')

        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(152, 120)
        self.btn.clicked.connect(self.swap)

        self.line1 = QLineEdit(self)
        self.line1.move(30, 90)
        
        self.line2 = QLineEdit(self)
        self.line2.move(230, 90)
        

    def swap(self):
        if self.btn.text() == "<-":
            self.btn.setText("->")
        else:
            self.btn.setText("<-")
        tmpText = self.line1.text()
        self.line1.setText(self.line2.text())
        self.line2.setText(tmpText) 
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())