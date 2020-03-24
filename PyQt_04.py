import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_04")
        self.setGeometry(50,50,350,350)
        self.UI()
        

    def UI(self):
        # all your code is here :

        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('resources\images\image1.jpg'))
        self.image.move(150,50)

        btn_remove = QPushButton("Remove",self)
        btn_show = QPushButton("Show",self)
        
        btn_remove.move(150,220)
        btn_show.move(260,220)

        btn_remove.clicked.connect(self.rmv)
        btn_show.clicked.connect(self.shw)

        self.show()

    def rmv(self):
        self.image.close()

    def shw(self):
        self.image.show()


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()