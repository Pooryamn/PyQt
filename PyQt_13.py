import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_13")
        self.setGeometry(350,150,600,500)
        self.UI()
        

    def UI(self):
        
        Vbox = QVBoxLayout()

        self.slider = QSlider(Qt.Horizontal)

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.setTickPosition(QSlider.TicksAbove)

        self.slider.setTickInterval(10)

        self.slider.valueChanged.connect(self.getval)

        self.txt_1 = QLabel('Poorya')
        self.txt_1.setAlignment(Qt.AlignCenter)

        self.txt_2 = QLabel('0')
        self.txt_2.setAlignment(Qt.AlignCenter)

        Vbox.addStretch()

        Vbox.addWidget(self.txt_1)

        Vbox.addStretch()

        Vbox.addWidget(self.txt_2)

        Vbox.addStretch()

        Vbox.addWidget(self.slider)

        Vbox.addStretch()
        Vbox.addStretch()

        self.setLayout(Vbox)


        self.show()

    def getval(self):
        val = self.slider.value()

        self.txt_2.setText(str(val))

        Font = QFont("Times",val)

        self.txt_1.setFont(Font)


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()