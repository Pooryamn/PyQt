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

        FontBtn = QPushButton('Font...')
        FontBtn.clicked.connect(self.FontFunc)

        ColorBtn = QPushButton('Color...')
        ColorBtn.clicked.connect(self.ColorFunc)


        VBox.addWidget(self.editor)
        VBox.addLayout(HBox)

        HBox.addStretch()

        HBox.addWidget(FileBtn)
        HBox.addWidget(FontBtn)
        HBox.addWidget(ColorBtn)
        HBox.addWidget(ClearBtn)

        HBox.addStretch()

        self.setLayout(VBox)

        self.show()

    def OpenFilefunc(self):
        url = QFileDialog.getOpenFileName(self,'Open File','','All Files(*);;Text File(*.txt)')
        FilePath = url[0]
        
        if(FilePath != ''):
            file = open(FilePath,'r')

            Data = file.read()

            self.editor.setText(Data)

            file.close()
    
    def Clearfunc(self):
        self.editor.clear()

    def FontFunc(self):
        font,Ok = QFontDialog.getFont()

        if (Ok):
            self.editor.setCurrentFont(font)
            

    
    def ColorFunc(self):
        color = QColorDialog.getColor()

        self.editor.setTextColor(color)



def main():
    App = QApplication(sys.argv)
    W = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()