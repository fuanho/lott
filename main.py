import sys
import random
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from mainwindow import Ui_MainWindow


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player = QMediaPlayer(None)
        self.ui.pushButton.clicked.connect(self.play)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display)
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile('{}\lott.wmv'.format(os.getcwd()))))
        self.videoWidget = QVideoWidget()
        self.ui.verticalLayout.addWidget(self.videoWidget)
        self.player.setVideoOutput(self.videoWidget)

        self.lott_name = []
        self.gift_name = []
        self.pick_gift=[]
        self.congratulation = ""
        with open('names.txt', 'r', encoding="utf-8") as f:
            names = f.readlines()
        for name in names:
            self.lott_name.append(name.split('\n')[0])
            self.gift_name.append(name.split('\n')[0])
        for name in self.lott_name:
            self.ui.textBrowser.append(name)

    def play(self):
        # Play
        self.player.play()
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(6000)
        self.pick()

    def pick(self):
        person = random.choice(self.lott_name)
        self.lott_name.remove(person)
        self.pick_gift.clear()
        for _ in self.gift_name:
            self.pick_gift.append(_)
        if person in self.pick_gift:
            self.pick_gift.remove(person)
        gift=random.choice(self.pick_gift)
        self.gift_name.remove(gift)
        self.congratulation = f'恭喜 {person} 抽中 {gift} 的禮物!!'
        print(self.congratulation)
        self.ui.textBrowser.clear()
        for name in self.lott_name:
            self.ui.textBrowser.append(name)

    def display(self):
        self.timer.stop()
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.information)

        msg.setStyleSheet("QLabel {min-width: 400px; min-height: 200px;}")
        msg.setWindowTitle("Congratulation")
        message = f'<p style="font-size:20pt; color: #4e9a06;">{self.congratulation}</p>'
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        print("stop")

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
