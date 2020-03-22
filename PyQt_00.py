import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(50,50,300,400)
        self.setWindowTitle("PyQt_00")

        self.show()


App = QApplication(sys.argv)
W = Window()
sys.exit(App.exec_())