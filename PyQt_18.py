import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_18")
        self.setGeometry(150,350,500,500)
        self.UI()
        

    def UI(self):
        
        self.Grid = QGridLayout()

        # Manual Way :

        # Btn1 = QPushButton('BTN 1')
        # Btn2 = QPushButton('BTN 2')
        # Btn3 = QPushButton('BTN 3')
        # Btn4 = QPushButton('BTN 4')

        # self.Grid.addWidget(Btn1,0,0)
        # self.Grid.addWidget(Btn2,0,1)
        # self.Grid.addWidget(Btn3,1,0)
        # self.Grid.addWidget(Btn4,1,1)

        # Automatic Way :

        for i in range(0,3): # rows
            for j in range(0,5): # cols
                btn = QPushButton('Button{}{}'.format(i,j))
                self.Grid.addWidget(btn,i,j)
                btn.clicked.connect(self.clickme)


        self.setLayout(self.Grid)

        self.show()
    
    def clickme(self):
        ButtonID = str(self.sender().text()).replace('Button','')
        if(ButtonID == '00'):
            QMessageBox.information(self,'click','Button 0 0 has clicked')


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()