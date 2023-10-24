import sys

from PyQt5 import uic
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtMultimedia


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)
        self.player = QtMultimedia.QMediaPlayer()

        self.notes = {}

        buttons = [
            self.C,
            self.Cs,
            self.D,
            self.Ds,
            self.E,
            self.F,
            self.Fs,
            self.G,
            self.Gs,
            self.A,
            self.As,
            self.B
        ]

        for b in buttons:
            self.notes[b.objectName()] = self.load_file(f'Samples/{b.objectName()}3.mp3')
            b.clicked.connect(self.playNote)

    def playNote(self):
        self.player.setMedia(self.notes[self.sender().objectName()])
        self.player.play()

    def load_file(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        return content


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())