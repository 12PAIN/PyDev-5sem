import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Task2')

        self.btn = QPushButton('Вычислить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 120)
        self.btn.clicked.connect(self.calculate)

        self.calculateInput = QLineEdit(self)
        self.calculateInput.move(30, 90)
        
        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(30, 30)
        
    def calculate(self):
        
        tmpEvalText = self.calculateInput.text()
        if tmpEvalText == "": return
        
        result = eval(tmpEvalText)
        
        self.LCD_count.display(result)
        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())