import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_03")
        self.setGeometry(50,50,350,350)
        self.UI()
        

    def UI(self):
        # all your code is here :

        self.txt_name = QLineEdit(self)
        self.txt_name.move(120,50)
        self.txt_name.setPlaceholderText("Your name")

        self.txt_pass = QLineEdit(self)
        self.txt_pass.move(120,80)
        self.txt_pass.setPlaceholderText("Your password")
        self.txt_pass.setEchoMode(QLineEdit.Password)

        btn = QPushButton("save",self)
        btn.move(170,110)
        btn.clicked.connect(self.on_btn_clicked)
        self.show()

    def on_btn_clicked(self):

        name = self.txt_name.text()
        password = self.txt_pass.text()

        self.setWindowTitle(name)


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()