import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt_17")
        self.setGeometry(350,150,500,500)
        self.UI()
        

    def UI(self):
        
        VBox = QVBoxLayout()
        HBox = QHBoxLayout()

        self.editor = QTextEdit()

        FileBtn = QPushButton('Open File')
        FileBtn.clicked.connect(self.OpenFilefunc)

        ClearBtn = QPushButton('Clear')
        ClearBtn.clicked.connect(self.Clearfunc)

        VBox.addWidget(self.editor)
        VBox.addLayout(HBox)

        HBox.addStretch()

        HBox.addWidget(FileBtn)
        HBox.addWidget(ClearBtn)

        HBox.addStretch()

        self.setLayout(VBox)

        self.show()

    def OpenFilefunc(self):
        url = QFileDialog.getOpenFileName(self,'Open File','','All Files(*);;Text File(*.txt)')
        FilePath = url[0]
        
        file = open(FilePath,'r')

        Data = file.read()

        self.editor.setText(Data)
    
    def Clearfunc(self):
        self.editor.clear()


def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()