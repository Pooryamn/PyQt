import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_14")
        self.setGeometry(350,150,600,500)
        self.UI()
        

    def UI(self):
        
        VBox = QVBoxLayout()
        self.table = QTableWidget()

        btn = QPushButton('Get Value')

        # add row and colums :
        self.table.setRowCount(10)
        self.table.setColumnCount(10)

        # change columns name :
        for i in range(10):
            self.table.setHorizontalHeaderItem(i,QTableWidgetItem(str(i)))
            self.table.setVerticalHeaderItem(i,QTableWidgetItem(str(i)))

        # hide or show headers:
        #self.table.horizontalHeader().hide()
        #self.table.verticalHeader().hide()


        #
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Set data in table :
        for i in range(10):
            for j in range(10):
                self.table.setItem(i,j,QTableWidgetItem(str(i*j)))


        # set Auto size for table:
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        VBox.addWidget(self.table)
        VBox.addWidget(btn)
        self.setLayout(VBox)


        btn.clicked.connect(self.getval)
        self.table.doubleClicked.connect(self.getval)

        self.show()

    def getval(self):
        for item in self.table.selectedItems(): # search for all selected cells :
            print(item.text(),item.row(),item.column())


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()