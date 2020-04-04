import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_12")
        self.setGeometry(350,150,400,400)
        self.UI()
        

    def UI(self):
        # all your code is here :
        
        FormLayout = QFormLayout()
        #FormLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        
        HBox2 = QHBoxLayout()
        HBox2.addWidget(QLineEdit())
        HBox2.addWidget(QLineEdit())

        
        lbl_name = QLabel("Name :")
        txt_name = QLineEdit()

        lbl_Pass = QLabel("Password :")
        txt_Pass = QLineEdit()

        FormLayout.addRow(lbl_name,HBox2)
        FormLayout.addRow(lbl_Pass,txt_Pass)

        FormLayout.addRow(QLabel("Country :"),QComboBox())

        HBox = QHBoxLayout()

        HBox.addStretch()
        
        HBox.addWidget(QPushButton("Enter"))
        HBox.addWidget(QPushButton("Exit"))

        FormLayout.addRow(HBox)

        self.setLayout(FormLayout)

        self.show()


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()