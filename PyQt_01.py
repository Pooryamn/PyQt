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
        
        lbl_Hello = QLabel("Hello World",self)
        lbl_Hello2 = QLabel("Hello Python",self)
        lbl_Hello.setGeometry(10,10,100,30) # ser exact geometry
        lbl_Hello2.move(200,10) # move obj form current to +x and +y value

        self.show()


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()