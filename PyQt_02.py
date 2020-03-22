import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_01")
        self.setGeometry(50,50,350,350)
        self.UI()
        

    def UI(self):
        # all your code is here :

        self.lbl = QLabel("My Text",self)
        btn_enter = QPushButton("Enter",self)
        btn_exit = QPushButton("Exit",self)

        self.lbl.move(160,50)
        btn_enter.move(100,100)
        btn_exit.move(200,100)
        
        btn_enter.clicked.connect(self.enterFunc)
        btn_exit.clicked.connect(self.exitFunc)

        self.show()

    def enterFunc(self):
        self.lbl.setText("Enter")
        self.lbl.resize(150,30)

    def exitFunc(self):
        self.lbl.setText("Exit")
        self.lbl.resize(150,30)

def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()