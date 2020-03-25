import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
import random

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_07")
        self.setGeometry(250,150,350,350)
        self.UI()
        

    def UI(self):
        # all your code is here :
        self.lbl_color = QLabel(self)
        self.lbl_color.resize(250,250)

        self.lbl_color.move(40,20)

        btn_start = QPushButton("Start",self)
        btn_stop = QPushButton("Stop",self)

        btn_start.move(80,300)
        btn_stop.move(190,300)

        btn_start.clicked.connect(self.start)
        btn_stop.clicked.connect(self.stop)

        # Timer : 
        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.change_color)

        self.value = 0
        self.R = 0
        self.G = 0
        self.B = 0

        self.show()

    def change_color(self):
        
        self.R = random.randint(0,256)
        self.G = random.randint(0,256)
        self.B = random.randint(0,256)

        self.lbl_color.setStyleSheet("background-color:rgb(" + str(self.R) +","+ str(self.G)+","+ str(self.B) +");")

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()