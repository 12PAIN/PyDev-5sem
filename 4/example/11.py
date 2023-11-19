import sys
from music import Ui_Form
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_mp3('1.mp3')
        self.playBtn.clicked.connect(self.player.play)
        self.pauseBtn.clicked.connect(self.player.pause)
        self.stopBtn.clicked.connect(self.player.stop)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())