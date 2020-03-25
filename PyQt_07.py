import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

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

        self.lbl_color.setStyleSheet("border: 3px solid rgb(255,0,0);"
                                     "background-color:rgb(0,100,100)")

        self.lbl_color.move(40,20)

        btn_start = QPushButton("Start",self)
        btn_stop = QPushButton("Stop",self)

        btn_start.move(80,300)
        btn_stop.move(190,300)

        btn_start.clicked.connect(self.start)
        btn_stop.clicked.connect(self.stop)

        # Timer : 
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.change_color)

        self.value = 0

        self.show()

    def change_color(self):
        if(self.value == 0):
            self.lbl_color.setStyleSheet("border: 3px solid rgb(255,0,0);"
                                         "background-color:rgb(100,100,0)")
            self.value = 1
        
        else:
            self.lbl_color.setStyleSheet("border: 3px solid rgb(255,0,0);"
                                         "background-color:rgb(100,100,100)")
            self.value = 0

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