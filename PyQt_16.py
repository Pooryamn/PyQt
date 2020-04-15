import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_16")
        self.setGeometry(150,350,600,600)
        self.UI()
        

    def UI(self):
        
        # Main menu :
        MenuBar = self.menuBar()

        file = MenuBar.addMenu("File")
        edit = MenuBar.addMenu('Edit')
        code = MenuBar.addMenu('Code')
        help_Menu = MenuBar.addMenu('Help')


        # Sub menu:
        new = QAction("New",self)
        new.setShortcut('Ctrl+O')
        file.addAction(new)

        open = QAction('Open',self)
        file.addAction(open)

        exit = QAction('Exit',self)
        exit.setIcon(QIcon('icons/exit.png'))
        exit.triggered.connect(self.exitfunc)
        file.addAction(exit)


        # Tool bar : 
        TB = self.addToolBar('MyToolBar')
        TB.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ExitTB = QAction(QIcon('icons/exit.png'),'Exit',self)

        ExitTB.triggered.connect(self.exitfunc)

        TB.addAction(ExitTB)

        OpenA = QAction(QIcon('icons/open.png'),'Open',self)
        OpenA.triggered.connect(self.openfunc)
        TB.addAction(OpenA)

        self.show()

    def exitfunc(self):
        mBox = QMessageBox.information(self,'Warning','Are you sure ?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

        if(mBox == QMessageBox.Yes):
            exit(0)

    def openfunc(self):
        QMessageBox.information(self,'Open','Open toolbar clicked')    

    
def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()