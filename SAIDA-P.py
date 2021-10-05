import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

test_ui = r'.\ui\SAIDA-P.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(test_ui, self)

        self.pushButton.clicked.connect(self.Button_click)
        

    def Button_click(self):
        file_names = QFileDialog.getOpenFileNames(self)

        for file in file_names[0]:
            exist = self.textEdit.toPlainText()
            self.textEdit.setText(exist + file) 

if __name__== '__main__':
    app = QApplication(sys.argv)
    Dialog = MainDialog()
    Dialog.show()
    app.exec_()