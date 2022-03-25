import os, sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication, QListWidget, QListWidgetItem, QMainWindow
from PyQt5.QtCore import Qt, QUrl
from main import Ui_SecondWindow




class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")

        self.label.setFont(QtGui.QFont("Digital Evidence Package", 12, QtGui.QFont.Bold))
        #
        # font = QtGui.QFont()
        # font.setFamily("Agency FB")
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setWeight(75)
        #
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 2)
        self.pushButton__main__Browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton__main__Browse.setObjectName("pushButton__main__Browse")

        self.gridLayout.addWidget(self.pushButton__main__Browse, 3, 1, 1, 1)
        self.pushButton__main__New = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton__main__New.clicked.connect(lambda: self.openWindow(MainWindow))

        self.pushButton__main__New.setObjectName("pushButton__main__New")
        self.gridLayout.addWidget(self.pushButton__main__New, 4, 0, 1, 1)
        self.pushButton_main__Load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_main__Load.setObjectName("pushButton_main__Load")
        self.gridLayout.addWidget(self.pushButton_main__Load, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton__main__Browse.clicked.connect(self.openBrowse)
        self.pushButton_main__Load.clicked.connect(self.openLoad)



    def openBrowse(self):
        file_name = QFileDialog.getSaveFileName(filter="JSON File (*.json)")
        self.lineEdit.setText(file_name[0])

    def openWindow(self, MainWindow):
        if self.lineEdit.text() == '':
            self.ErrorMessage("경로를 입력해주세요.")
        elif os.path.exists(self.lineEdit.text()):
            self.ErrorMessage("해당 경로에 파일이 존재합니다.")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SecondWindow(self.lineEdit.text(), 'new')
            self.ui.setupUi(self.window)

            self.window.show()
            MainWindow.close()

    def openLoad(self):
        if self.lineEdit.text() == '':
            self.ErrorMessage("경로를 입력해주세요.")

        elif not os.path.exists(self.lineEdit.text()):
            self.ErrorMessage("경로가 존재하지 않습니다.")

        elif os.path.exists(self.lineEdit.text()):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SecondWindow(self.lineEdit.text(), 'load')
            self.ui.setupUi(self.window)

            self.window.show()
            MainWindow.close()


    def ErrorMessage(self, str):
        msg = QMessageBox()
        msg.setText(str)
        msg.setWindowTitle("경고")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SAIDA-P"))
        self.label.setText(_translate("MainWindow", "Digital Evidence Package"))
        self.label_2.setText(_translate("MainWindow", "생성 또는 읽어올 증거팩 파일 경로를 선택해주세요."))
        self.pushButton__main__Browse.setText(_translate("MainWindow", "Browse..."))
        self.pushButton__main__New.setText(_translate("MainWindow", "New"))
        self.pushButton_main__Load.setText(_translate("MainWindow", "Load"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())


