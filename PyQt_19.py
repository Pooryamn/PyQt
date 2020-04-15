import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

count = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_19")
        self.setGeometry(350,150,500,500)
        self.UI()
        

    def UI(self):
        
        VBox = QVBoxLayout()
        HBox = QHBoxLayout()

        self.Progress = QProgressBar()

        BtnStart = QPushButton('Start')
        BtnStart.clicked.connect(self.timeStart)
        
        BtnStop = QPushButton('Stop')
        BtnStop.clicked.connect(self.timeStop)


        self.Timer = QTimer()
        self.Timer.setInterval(500)
        self.Timer.timeout.connect(self.runProgressBar)

        VBox.addWidget(self.Progress)

        HBox.addStretch()
        HBox.addWidget(BtnStart)
        HBox.addWidget(BtnStop)
        HBox.addStretch()

        VBox.addLayout(HBox)

        self.setLayout(VBox)
        

        self.show()

    def runProgressBar(self):
        global count
        count += 1
        if(count == 100):
            self.Timer.stop()
        self.Progress.setValue(count)
        
    def timeStart(self):
        self.Timer.start()

    def timeStop(self):
        self.Timer.stop()


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()