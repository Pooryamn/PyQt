import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_05")
        self.setGeometry(50,50,350,350)
        self.UI()
        

    def UI(self):
        # all your code is here :
        self.txt_name = QLineEdit(self)
        self.txt_lastname = QLineEdit(self)

        self.txt_name.move(150,50)
        self.txt_lastname.move(150,80)

        self.txt_name.setPlaceholderText("Your Name")
        self.txt_lastname.setPlaceholderText("Your Lastname")

        self.ch_remember = QCheckBox("Remember me",self)
        self.ch_remember.move(150,110)

        btn_submit = QPushButton("Submit",self)
        btn_submit.move(170,140)

        btn_submit.clicked.connect(self.on_btn_clk)

        self.show()

    def on_btn_clk(self):

        if(self.ch_remember.isChecked()):
            print(" Name : " + self.txt_name.text() + " Lastname : " + self.txt_lastname.text() + " Remember : Checked")
        else :    
            print("Name : " + self.txt_name.text() + " Lastname : " + self.txt_lastname.text() + " Remember : Not Checked")

def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()