import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_10")
        self.setGeometry(350,150,400,400)
        self.UI()
        

    def UI(self):
        # all your code is here :
        VBox = QVBoxLayout()

        btn1 = QPushButton("Save")
        btn2 = QPushButton("Load")
        btn3 = QPushButton("Exit",self)

        VBox.addStretch()

        VBox.addWidget(btn1)
        VBox.addWidget(btn2)
        VBox.addWidget(btn3)

        VBox.addStretch()

        self.setLayout(VBox)

        self.show()


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()