import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_06")
        self.setGeometry(250,150,500,500)
        self.UI()
        

    def UI(self):
        # all your code is here :
        self.combo = QComboBox(self)
        self.combo.move(150,100)

        btn = QPushButton("Save",self)
        btn.move(150,130)
        
        # add items to combo :
        self.combo.addItem("Python")
        self.combo.addItems(["C","C++","C#","PHP"])

        btn.clicked.connect(self.getval)

        self.show()

    def getval(self):
        value = self.combo.currentText()
        print(value)

def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()