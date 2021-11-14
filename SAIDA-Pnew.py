import os, sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from make import Ui_SecondWindow


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

        '''file_name = QFileDialog.getOpenFileName(filter="JSON File (*.json)")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow(self.lineEdit.text(), 'load')
        self.ui.setupUi(self.window)
        if file_name[0]:


                #Digital Evidences
                management_id = data['Digital Evidence Package']['Digital Evidences'][0]['management_id']
                digital_evidence_type = data['Digital Evidence Package']['Digital Evidences'][0]['digital_evidence_type']
                evidences_gathering_type = data['Digital Evidence Package']['Digital Evidences'][0]['evidences_gathering_type']

                vessel_management_id = data['Digital Evidence Package']['Digital Evidences'][0]['Vessel Info']['vessel_management_id']
                vessel_name = data['Digital Evidence Package']['Digital Evidences'][0]['Vessel Info']['vessel_name']
                vessel_MMSI = data['Digital Evidence Package']['Digital Evidences'][0]['Vessel Info']['vessel_MMSI']
                vessel_callsign = data['Digital Evidence Package']['Digital Evidences'][0]['Vessel Info']['vessel_callsign']
                vessel_IMO = data['Digital Evidence Package']['Digital Evidences'][0]['Vessel Info']['vessel_IMO']
                vessel_MRN = data['Digital Evidence Package']['Digital Evidences'][0]['Vessel Info']['vessel_MRN']
                vessel_tonnage = data['Digital Evidence Package']['Digital Evidences'][0]['Vessel Info']['vessel_tonnage']
                vessel_length = data['Digital Evidence Package']['Digital Evidences'][0]['Vessel Info']['vessel_length']
                total_number_of_equipment_with_track = data['Digital Evidence Package']['Digital Evidences'][0]['Vessel Info']['total_number_of_equipment_with_track']

                device_management_id = data['Digital Evidence Package']['Digital Evidences'][0]['Marine Electronics Info']['device_management_id']













        #Digital Evidences
        self.ui.DE_management_id__lineEdit_1.setText(management_id)
        self.ui.DE_digital_evidence_type__lineEdit_1.setText(digital_evidence_type)
        self.ui.DE_evidences_gathering_type__ineEdit_1.setText(evidences_gathering_type)

        self.ui.DE_Vessel_Info_vessel_management_id__lineEdit_1.setText(vessel_management_id)
        self.ui.DE_Vessel_Info_vessel_name__lineEdit_1.setText(vessel_name)
        self.ui.DE_Vessel_Info_vessel_MMSI__lineEdit_1.setText(vessel_MMSI)
        self.ui.DE_Vessel_Info_vessel_callsign__lineEdit_1.setText(vessel_callsign)
        self.ui.DE_Vessel_Info_vessel_IMO__lineEdit_1.setText(vessel_IMO)
        self.ui.DE_Vessel_Info_vessel_MRN__lineEdit_1.setText(vessel_MRN)
        self.ui.DE_Vessel_Info_vessel_tonnage__lineEdit_1.setText(vessel_tonnage)
        self.ui.DE_Vessel_Info_vessel_length__lineEdit_1.setText(vessel_length)
        self.ui.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1.setText(total_number_of_equipment_with_track)

        self.ui.DE_Marines_Electronics_Info_device_management_id__lineEdit_1.setText(device_management_id)


















        self.window.show()
        MainWindow.close()'''

    def ErrorMessage(self, str):
        msg = QMessageBox()
        msg.setText(str)
        msg.setWindowTitle("경고")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
