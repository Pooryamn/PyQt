import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_15")
        self.setGeometry(350,150,600,600)
        self.UI()
        

    def UI(self):
        
        MainLayout = QVBoxLayout()

        self.tabs = QTabWidget()

        # Create and Show tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1,"First")
        self.tabs.addTab(self.tab2,"Second")
        self.tabs.addTab(self.tab3,"Third")

        # Widgets :
        Vbox = QVBoxLayout()
        HBox = QHBoxLayout()

        self.lbl = QLabel("Hello Python")

        self.btn1 = QPushButton("First Tab")
        self.btn1.clicked.connect(self.btnFunc)

        self.btn2 = QPushButton("Second Tab")

        Vbox.addWidget(self.lbl)
        Vbox.addWidget(self.btn1)
        HBox.addWidget(self.btn2)

        self.tab1.setLayout(Vbox)
        self.tab2.setLayout(HBox)

        MainLayout.addWidget(self.tabs)
        self.setLayout(MainLayout)

        self.show()

    def btnFunc(self):
        self.lbl.setText('Hello Poorya')


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()