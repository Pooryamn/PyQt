import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_09")
        self.setGeometry(350,150,400,400)
        self.UI()
        

    def UI(self):
        # all your code is here :
        HBox = QHBoxLayout()
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")

        HBox.addStretch()

        HBox.addWidget(btn1)
        HBox.addWidget(btn2)
        HBox.addWidget(btn3)

        HBox.addStretch()

        self.setLayout(HBox)

        self.show()


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()