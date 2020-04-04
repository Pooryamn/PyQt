import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_11")
        self.setGeometry(350,150,400,400)
        self.UI()
        

    def UI(self):
        # all your code is here :
        MainLayout = QVBoxLayout()
        TopLayout = QHBoxLayout()
        BottomLayout = QHBoxLayout()

        MainLayout.addLayout(TopLayout)
        MainLayout.addLayout(BottomLayout)

        CBox = QCheckBox()
        RBtn = QRadioButton()
        COBox = QComboBox()

        btn1 = QPushButton()
        btn2 = QPushButton()

        TopLayout.setContentsMargins(150,10,20,20) #left,Top,right,bottom

        TopLayout.addWidget(CBox)
        TopLayout.addWidget(RBtn)
        TopLayout.addWidget(COBox)

        BottomLayout.setContentsMargins(150,10,150,10)

        BottomLayout.addWidget(btn1)
        BottomLayout.addWidget(btn2)

        self.setLayout(MainLayout)

        self.show()


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()