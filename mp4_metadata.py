import datetime
import hashlib
import json
import os
from PIL import Image
from PIL.ExifTags import TAGS
from shutil import copyfile
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Ui_SecondWindow(object):

    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

        # CI
        self.CI_num = 1
        self.CI_List = list()

        # DE 전체 add
        self.DE_AddAll_num = 1
        self.DE_AddAll_List = list()

        # DE 채증정보 파일 리스트
        self.DE_Gather_Info_File_num = 1
        self.DE_Gather_Info_File_List = list()

        # DE 채증정보 add , 3차원
        self.DE_Gather_Info_num = 1
        self.DE_Gather_Info_List = list()
        self.DE_Gather_Info_List.append(list())

        # DE 수집 정보 add , 3차원
        self.DE_Acquisition_Info_num = 1
        self.DE_Acquisition_Info_List = list()
        self.DE_Acquisition_Info_List.append(list())

        # DE 수집 정보 파일 리스트 add
        self.DE_Acquisition_Info_File_num = 1
        self.DE_Acquisition_Info_File_List = list()

        # DE Browse, Enter 버튼
        self.DE_Button_num = 1
        self.DE_Button_List = list()

        # DE 기타파일 +누르면 add
        self.DE_Other_Files_num = 1
        self.DE_Other_Files_Info_List = list()
        self.DE_Other_Files_Info_List.append(list())

        # DE 기타파일 파일 리스트
        self.DE_Other_Files_File_num = 1
        self.DE_Other_Files_File_List = list()


        # AI 보고서 add
        self.AIReports_num = 1
        self.AIReports_List = list()

        # AI Reports Browse, Enter 버튼
        self.AIReports_Button_num = 1
        self.AIReports_Button_List = list()

        # AI 기타파일 add
        self.AI_num = 1
        self.AI_List = list()

        # AI 기타파일 버튼
        self.AI_other_files_Button_num = 1
        self.AI_other_files_Button_List = list()

        # AI 장비 흔적  add
        self.AI_EquipmentTraces_num = 1
        self.AI_EquipmentTraces_List = list()

        # DEPL 전체 add
        self.DEPL_num = 1
        self.DEPL_List = list()

        #++
        self.DE_AddAll_Gather_Browse_num = 1
        self.DE_AddAll_Gather_Browse_List = list()

        self.DE_AddAll_Other_Files_Browse_num = 1
        self.DE_AddAll_Other_Files_Browse_List = list()

        self.DE_AddAll_Acquisition_Browse_num = 1
        self.DE_AddAll_Acquisition_Browse_List = list()

        self.DE_AddAll_Gather_Enter_num = 1
        self.DE_AddAll_Gather_Enter_List = list()

        self.DE_AddAll_Acquisition_Enter_num = 1
        self.DE_AddAll_Acquisition_Enter_List = list()

        self.DE_AddAll_Other_Files_Enter_num = 1
        self.DE_AddAll_Other_Files_Enter_List = list()


    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(848, 646)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_14.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_14.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_14.addWidget(self.label_4)
        self.ExportButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ExportButton.setFont(font)
        self.ExportButton.setObjectName("ExportButton")
        self.horizontalLayout_14.addWidget(self.ExportButton)
        self.gridLayout_8.addLayout(self.horizontalLayout_14, 2, 0, 1, 1)
        self.Digital_Evidence_Package = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Digital_Evidence_Package.setFont(font)
        self.Digital_Evidence_Package.setObjectName("Digital_Evidence_Package")
        self.gridLayout_8.addWidget(self.Digital_Evidence_Package, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Case_Info_tab = QtWidgets.QWidget()
        self.Case_Info_tab.setObjectName("Case_Info_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.Case_Info_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.Case_Info = QtWidgets.QLabel(self.Case_Info_tab)
        self.Case_Info.setObjectName("Case_Info")
        self.gridLayout.addWidget(self.Case_Info, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.Case_Info_tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 796, 422))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.case_management_id__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.case_management_id__label.setObjectName("case_management_id__label")
        self.gridLayout_2.addWidget(self.case_management_id__label, 0, 0, 1, 1)
        self.case_management_id__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.case_management_id__lineEdit.setObjectName("case_management_id__lineEdit")
        self.gridLayout_2.addWidget(self.case_management_id__lineEdit, 0, 1, 1, 1)
        self.contents_of_request__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.contents_of_request__label.setObjectName("contents_of_request__label")
        self.gridLayout_2.addWidget(self.contents_of_request__label, 0, 2, 1, 1)
        self.agency_case_no__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.agency_case_no__label.setObjectName("agency_case_no__label")
        self.gridLayout_2.addWidget(self.agency_case_no__label, 1, 0, 1, 1)
        self.contents_of_request__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.contents_of_request__lineEdit.setObjectName("contents_of_request__lineEdit")
        self.gridLayout_2.addWidget(self.contents_of_request__lineEdit, 0, 3, 1, 1)
        self.agency_organization_code__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.agency_organization_code__lineEdit.setObjectName("agency_organization_code__lineEdit")
        self.gridLayout_2.addWidget(self.agency_organization_code__lineEdit, 2, 1, 1, 1)
        self.agency_organization_party_name__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.agency_organization_party_name__lineEdit.setObjectName("agency_organization_party_name__lineEdit")
        self.gridLayout_2.addWidget(self.agency_organization_party_name__lineEdit, 4, 1, 1, 1)
        self.ordering_datetime__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ordering_datetime__label.setObjectName("ordering_datetime__label")
        self.gridLayout_2.addWidget(self.ordering_datetime__label, 4, 2, 1, 1)
        self.agency_case_no__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.agency_case_no__lineEdit.setObjectName("agency_case_no__lineEdit")
        self.gridLayout_2.addWidget(self.agency_case_no__lineEdit, 1, 1, 1, 1)
        self.case_summary__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.case_summary__label.setObjectName("case_summary__label")
        self.gridLayout_2.addWidget(self.case_summary__label, 1, 2, 1, 1)
        self.case_description__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.case_description__lineEdit.setObjectName("case_description__lineEdit")
        self.gridLayout_2.addWidget(self.case_description__lineEdit, 2, 3, 1, 1)
        self.case_datetime__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.case_datetime__label.setObjectName("case_datetime__label")
        self.gridLayout_2.addWidget(self.case_datetime__label, 3, 2, 1, 1)
        self.case_datetime__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.case_datetime__lineEdit.setObjectName("case_datetime__lineEdit")
        self.gridLayout_2.addWidget(self.case_datetime__lineEdit, 3, 3, 1, 1)
        self.agency_organization_code__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.agency_organization_code__label.setObjectName("agency_organization_code__label")
        self.gridLayout_2.addWidget(self.agency_organization_code__label, 2, 0, 1, 1)
        self.agency_organization_name__labe = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.agency_organization_name__labe.setObjectName("agency_organization_name__labe")
        self.gridLayout_2.addWidget(self.agency_organization_name__labe, 3, 0, 1, 1)
        self.case_summary__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.case_summary__lineEdit.setObjectName("case_summary__lineEdit")
        self.gridLayout_2.addWidget(self.case_summary__lineEdit, 1, 3, 1, 1)
        self.case_description__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.case_description__label.setObjectName("case_description__label")
        self.gridLayout_2.addWidget(self.case_description__label, 2, 2, 1, 1)
        self.agency_organization_name__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.agency_organization_name__lineEdit.setObjectName("agency_organization_name__lineEdit")
        self.gridLayout_2.addWidget(self.agency_organization_name__lineEdit, 3, 1, 1, 1)
        self.agency_organization_party_name__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.agency_organization_party_name__label.setObjectName("agency_organization_party_name__label")
        self.gridLayout_2.addWidget(self.agency_organization_party_name__label, 4, 0, 1, 1)
        self.ordering_datetime__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ordering_datetime__lineEdit.setObjectName("ordering_datetime__lineEdit")
        self.gridLayout_2.addWidget(self.ordering_datetime__lineEdit, 4, 3, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Case_Info_tab, "")
        self.DE_tab = QtWidgets.QWidget()
        self.DE_tab.setObjectName("DE_tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.DE_tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.DE__addButton = QtWidgets.QPushButton(self.DE_tab)
        self.DE__addButton.setObjectName("DE__addButton")
        self.gridLayout_9.addWidget(self.DE__addButton, 0, 1, 1, 1)
        self.DE_Digitlal_Evidence__label = QtWidgets.QLabel(self.DE_tab)
        self.DE_Digitlal_Evidence__label.setObjectName("DE_Digitlal_Evidence__label")
        self.gridLayout_9.addWidget(self.DE_Digitlal_Evidence__label, 0, 0, 1, 1)
        self.DE__scrollArea_1 = QtWidgets.QScrollArea(self.DE_tab)
        self.DE__scrollArea_1.setWidgetResizable(True)
        self.DE__scrollArea_1.setObjectName("DE__scrollArea_1")
        self.DE__scrollAreaWidgetContents = QtWidgets.QWidget()
        self.DE__scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 796, 409))
        self.DE__scrollAreaWidgetContents.setObjectName("DE__scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.DE__scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.DE_AddAll__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_AddAll__verticalLayout_1.setObjectName("DE_AddAll__verticalLayout_1")
        self.DE_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_management_id__horizontalLayout_1.setObjectName("DE_management_id__horizontalLayout_1")
        self.DE_management_id__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_management_id__label_1.setObjectName("DE_management_id__label_1")
        self.DE_management_id__horizontalLayout_1.addWidget(self.DE_management_id__label_1)
        self.DE_management_id__lineEdit_1 = QtWidgets.QLineEdit(self.DE__scrollAreaWidgetContents)
        self.DE_management_id__lineEdit_1.setObjectName("DE_management_id__lineEdit_1")
        self.DE_management_id__horizontalLayout_1.addWidget(self.DE_management_id__lineEdit_1)
        self.DE_AddAll__verticalLayout_1.addLayout(self.DE_management_id__horizontalLayout_1)
        self.DE_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_digital_evidence_type__horizontalLayout_1.setObjectName("DE_digital_evidence_type__horizontalLayout_1")
        self.DE_digital_evidence_type__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_digital_evidence_type__label_1.setObjectName("DE_digital_evidence_type__label_1")
        self.DE_digital_evidence_type__horizontalLayout_1.addWidget(self.DE_digital_evidence_type__label_1)
        self.DE_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE__scrollAreaWidgetContents)
        self.DE_digital_evidence_type__lineEdit_1.setObjectName("DE_digital_evidence_type__lineEdit_1")
        self.DE_digital_evidence_type__horizontalLayout_1.addWidget(self.DE_digital_evidence_type__lineEdit_1)
        self.DE_AddAll__verticalLayout_1.addLayout(self.DE_digital_evidence_type__horizontalLayout_1)
        self.DE_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_evidences_gathering_type__horizontalLayout_1.setObjectName("DE_evidences_gathering_type__horizontalLayout_1")
        self.DE_evidences_gathering_type__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_evidences_gathering_type__label_1.setObjectName("DE_evidences_gathering_type__label_1")
        self.DE_evidences_gathering_type__horizontalLayout_1.addWidget(self.DE_evidences_gathering_type__label_1)
        self.DE_evidences_gathering_type__ineEdit_1 = QtWidgets.QLineEdit(self.DE__scrollAreaWidgetContents)
        self.DE_evidences_gathering_type__ineEdit_1.setObjectName("DE_evidences_gathering_type__ineEdit_1")
        self.DE_evidences_gathering_type__horizontalLayout_1.addWidget(self.DE_evidences_gathering_type__ineEdit_1)
        self.DE_AddAll__verticalLayout_1.addLayout(self.DE_evidences_gathering_type__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1")
        self.DE_Vessel_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info__horizontalLayout_1.setObjectName("DE_Vessel_Info__horizontalLayout_1")
        self.DE_Vessel_Info__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_Vessel_Info__label_1.setObjectName("DE_Vessel_Info__label_1")
        self.DE_Vessel_Info__horizontalLayout_1.addWidget(self.DE_Vessel_Info__label_1)
        self.DE_Vessel_Info__blanklabel_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_Vessel_Info__blanklabel_1.setText("")
        self.DE_Vessel_Info__blanklabel_1.setObjectName("DE_Vessel_Info__blanklabel_1")
        self.DE_Vessel_Info__horizontalLayout_1.addWidget(self.DE_Vessel_Info__blanklabel_1)
        self.DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1.addLayout(self.DE_Vessel_Info__horizontalLayout_1)
        self.DE_Marine_Electronics_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marine_Electronics_Info__horizontalLayout_1.setObjectName("DE_Marine_Electronics_Info__horizontalLayout_1")
        self.DE_Marine_Electronics_Info__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_Marine_Electronics_Info__label_1.setObjectName("DE_Marine_Electronics_Info__label_1")
        self.DE_Marine_Electronics_Info__horizontalLayout_1.addWidget(self.DE_Marine_Electronics_Info__label_1)
        self.label_5 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.DE_Marine_Electronics_Info__horizontalLayout_1.addWidget(self.label_5)
        self.DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1.addLayout(self.DE_Marine_Electronics_Info__horizontalLayout_1)
        self.DE_other_files__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files__horizontalLayout_1.setObjectName("DE_other_files__horizontalLayout_1")
        self.DE_other_files__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_other_files__label_1.setObjectName("DE_other_files__label_1")
        self.DE_other_files__horizontalLayout_1.addWidget(self.DE_other_files__label_1)
        self.DE_other_files__addButton_1 = QtWidgets.QPushButton(self.DE__scrollAreaWidgetContents)
        self.DE_other_files__addButton_1.setObjectName("DE_other_files__addButton_1")
        self.DE_other_files__horizontalLayout_1.addWidget(self.DE_other_files__addButton_1)
        self.DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1.addLayout(self.DE_other_files__horizontalLayout_1)
        self.DE_AddAll__verticalLayout_1.addLayout(self.DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1)
        self.DE_sub__scrollArea_1 = QtWidgets.QScrollArea(self.DE__scrollAreaWidgetContents)
        self.DE_sub__scrollArea_1.setWidgetResizable(True)
        self.DE_sub__scrollArea_1.setObjectName("DE_sub__scrollArea_1")
        self.DE_sub__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_sub__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 770, 254))
        self.DE_sub__scrollAreaWidgetContents_1.setObjectName("DE_sub__scrollAreaWidgetContents_1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.DE_sub__scrollAreaWidgetContents_1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.DE_Gather_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info__horizontalLayout_1.setObjectName("DE_Gather_Info__horizontalLayout_1")
        self.DE_Gather_Info__label_1 = QtWidgets.QLabel(self.DE_sub__scrollAreaWidgetContents_1)
        self.DE_Gather_Info__label_1.setObjectName("DE_Gather_Info__label_1")
        self.DE_Gather_Info__horizontalLayout_1.addWidget(self.DE_Gather_Info__label_1)
        self.gridLayout_5.addLayout(self.DE_Gather_Info__horizontalLayout_1, 3, 0, 1, 1)
        self.DE_Gather_Info__scrollArea_1 = QtWidgets.QScrollArea(self.DE_sub__scrollAreaWidgetContents_1)
        self.DE_Gather_Info__scrollArea_1.setWidgetResizable(True)
        self.DE_Gather_Info__scrollArea_1.setObjectName("DE_Gather_Info__scrollArea_1")
        self.DE_Gather_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Gather_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 251, 330))
        self.DE_Gather_Info__scrollAreaWidgetContents_1.setObjectName("DE_Gather_Info__scrollAreaWidgetContents_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.DE_Gather_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Gather_Info__verticalLayout_1.setObjectName("DE_Gather_Info__verticalLayout_1")
        self.DE_Gather_Info_gather_location__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_location__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_location__horizontalLayout_1")
        self.DE_Gather_Info_gather_location__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_location__label_1.setObjectName("DE_Gather_Info_gather_location__label_1")
        self.DE_Gather_Info_gather_location__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_location__label_1)
        self.DE_Gather_Info_gather_location__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_location__lineEdit_1.setObjectName("DE_Gather_Info_gather_location__lineEdit_1")
        self.DE_Gather_Info_gather_location__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_location__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_location__horizontalLayout_1)
        self.DE_Gather_Info_gather_person_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_person_name__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_person_name__horizontalLayout_1")
        self.DE_Gather_Info_gather_person_name__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_name__label_1.setObjectName("DE_Gather_Info_gather_person_name__label_1")
        self.DE_Gather_Info_gather_person_name__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_person_name__label_1)
        self.DE_Gather_Info_gather_person_name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_name__lineEdit_1.setObjectName("DE_Gather_Info_gather_person_name__lineEdit_1")
        self.DE_Gather_Info_gather_person_name__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_person_name__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_person_name__horizontalLayout_1)
        self.DE_Gather_Info_gather_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_datetime__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_datetime__horizontalLayout_1")
        self.DE_Gather_Info_gather_datetime__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_datetime__label_1.setObjectName("DE_Gather_Info_gather_datetime__label_1")
        self.DE_Gather_Info_gather_datetime__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_datetime__label_1)
        self.DE_Gather_Info_gather_datetime__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_datetime__lineEdit_1.setObjectName("DE_Gather_Info_gather_datetime__lineEdit_1")
        self.DE_Gather_Info_gather_datetime__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_datetime__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_datetime__horizontalLayout_1)
        self.DE_Gather_Info_gather_person_agency__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_person_agency__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_person_agency__horizontalLayout_1")
        self.DE_Gather_Info_gather_person_agency__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_agency__label_1.setObjectName("DE_Gather_Info_gather_person_agency__label_1")
        self.DE_Gather_Info_gather_person_agency__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_person_agency__label_1)
        self.DE_Gather_Info_gather_person_agency__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_agency__lineEdit_1.setObjectName("DE_Gather_Info_gather_person_agency__lineEdit_1")
        self.DE_Gather_Info_gather_person_agency__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_person_agency__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_person_agency__horizontalLayout_1)
        self.DE_Gather_Info_gather_person_rank__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_person_rank__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_person_rank__horizontalLayout_1")
        self.DE_Gather_Info_gather_person_rank__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_rank__label_1.setObjectName("DE_Gather_Info_gather_person_rank__label_1")
        self.DE_Gather_Info_gather_person_rank__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_person_rank__label_1)
        self.DE_Gather_Info_gather_person_rank__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_rank__lineEdit_1.setObjectName("DE_Gather_Info_gather_person_rank__lineEdit_1")
        self.DE_Gather_Info_gather_person_rank__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_person_rank__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_person_rank__horizontalLayout_1)
        self.DE_Gather_Info_submitter_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_submitter_name__horizontalLayout_1.setObjectName("DE_Gather_Info_submitter_name__horizontalLayout_1")
        self.DE_Gather_Info_submitter_name__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_submitter_name__label_1.setObjectName("DE_Gather_Info_submitter_name__label_1")
        self.DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(self.DE_Gather_Info_submitter_name__label_1)
        self.DE_Gather_Info_submitter_name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_submitter_name__lineEdit_1.setObjectName("DE_Gather_Info_submitter_name__lineEdit_1")
        self.DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(self.DE_Gather_Info_submitter_name__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_submitter_name__horizontalLayout_1)
        self.DE_Gather_Info_file_addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_file_addButton__horizontalLayout_1.setObjectName("DE_Gather_Info_file_addButton__horizontalLayout_1")
        self.DE_Gather_Info_file__blanklabel_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__blanklabel_1.setText("")
        self.DE_Gather_Info_file__blanklabel_1.setObjectName("DE_Gather_Info_file__blanklabel_1")
        self.DE_Gather_Info_file_addButton__horizontalLayout_1.addWidget(self.DE_Gather_Info_file__blanklabel_1)
        self.DE_Gather_Info__addButton_1 = QtWidgets.QPushButton(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info__addButton_1.setObjectName("DE_Gather_Info__addButton_1")
        self.DE_Gather_Info_file_addButton__horizontalLayout_1.addWidget(self.DE_Gather_Info__addButton_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_file_addButton__horizontalLayout_1)
        self.DE_Gather_Info_file__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_file__horizontalLayout_1.setObjectName("DE_Gather_Info_file__horizontalLayout_1")
        self.DE_Gather_Info_file__scrollArea_1 = QtWidgets.QScrollArea(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__scrollArea_1.setWidgetResizable(True)
        self.DE_Gather_Info_file__scrollArea_1.setObjectName("DE_Gather_Info_file__scrollArea_1")
        self.DE_Gather_Info_file__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Gather_Info_file__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 344, 174))
        self.DE_Gather_Info_file__scrollAreaWidgetContents_1.setObjectName("DE_Gather_Info_file__scrollAreaWidgetContents_1")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.DE_Gather_Info_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Gather_Info_file__verticalLayout_1.setObjectName("DE_Gather_Info_file__verticalLayout_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.setObjectName("DE_Gather_Info_file__filebrowse__horizontalLayout_1")
        self.DE_Gather_Info_file__filebrowse__label_1 = QtWidgets.QLabel(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__filebrowse__label_1.setObjectName("DE_Gather_Info_file__filebrowse__label_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(self.DE_Gather_Info_file__filebrowse__label_1)
        self.DE_Gather_Info_file__filebrowse__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__filebrowse__lineEdit_1.setObjectName("DE_Gather_Info_file__filebrowse__lineEdit_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(self.DE_Gather_Info_file__filebrowse__lineEdit_1)
        self.DE_Gather_Info_file__filebrowse__browseButton_1 = QtWidgets.QPushButton(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__filebrowse__browseButton_1.setObjectName("DE_Gather_Info_file__filebrowse__browseButton_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(self.DE_Gather_Info_file__filebrowse__browseButton_1)
        self.DE_Gather_Info_file__filebrowse__enterButton_1 = QtWidgets.QPushButton(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__filebrowse__enterButton_1.setObjectName("DE_Gather_Info_file__filebrowse__enterButton_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(self.DE_Gather_Info_file__filebrowse__enterButton_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_file__filebrowse__horizontalLayout_1)
        self.DE_Gather_Info_gather_media_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_media_type__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_media_type__horizontalLayout_1")
        self.DE_Gather_Info_gather_media_type__label_1 = QtWidgets.QLabel(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_media_type__label_1.setObjectName("DE_Gather_Info_gather_media_type__label_1")
        self.DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_media_type__label_1)
        self.DE_Gather_Info_gather_media_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_media_type__lineEdit_1.setObjectName("DE_Gather_Info_gather_media_type__lineEdit_1")
        self.DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_media_type__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_media_type__horizontalLayout_1)
        self.DE_Gather_Info_gather_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_hash_type__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_hash_type__horizontalLayout_1")
        self.DE_Gather_Info__gather_hash_type__label_1 = QtWidgets.QLabel(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info__gather_hash_type__label_1.setObjectName("DE_Gather_Info__gather_hash_type__label_1")
        self.DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(self.DE_Gather_Info__gather_hash_type__label_1)
        self.DE_Gather_Info__gather_hash_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info__gather_hash_type__lineEdit_1.setObjectName("DE_Gather_Info__gather_hash_type__lineEdit_1")
        self.DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(self.DE_Gather_Info__gather_hash_type__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_hash_type__horizontalLayout_1)
        self.DE_Gather_Info_gather_hash__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_hash__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_hash__horizontalLayout_1")
        self.DE_Gather_Info_gather_hash__label_1 = QtWidgets.QLabel(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_hash__label_1.setObjectName("DE_Gather_Info_gather_hash__label_1")
        self.DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_hash__label_1)
        self.DE_Gather_Info_gather_hash__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_hash__lineEdit_1.setObjectName("DE_Gather_Info_gather_hash__lineEdit_1")
        self.DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_hash__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_hash__horizontalLayout_1)
        self.DE_Gather_Info_gather_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_path__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_path__horizontalLayout_1")
        self.DE_Gather_Info_gather_path__label_1 = QtWidgets.QLabel(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_path__label_1.setObjectName("DE_Gather_Info_gather_path__label_1")
        self.DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_path__label_1)
        self.DE_Gather_Info_gather_path__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_path__lineEdit_1.setObjectName("DE_Gather_Info_gather_path__lineEdit_1")
        self.DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_path__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_path__horizontalLayout_1)
        self.gridLayout_18.addLayout(self.DE_Gather_Info_file__verticalLayout_1, 1, 0, 1, 1)
        self.DE_Gather_Info_file__scrollArea_1.setWidget(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__horizontalLayout_1.addWidget(self.DE_Gather_Info_file__scrollArea_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_file__horizontalLayout_1)
        self.gridLayout_3.addLayout(self.DE_Gather_Info__verticalLayout_1, 0, 0, 1, 1)
        self.DE_Gather_Info__scrollArea_1.setWidget(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.gridLayout_5.addWidget(self.DE_Gather_Info__scrollArea_1, 4, 0, 1, 1)
        self.DE_Acquisition_Info__scrollArea_1 = QtWidgets.QScrollArea(self.DE_sub__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info__scrollArea_1.setWidgetResizable(True)
        self.DE_Acquisition_Info__scrollArea_1.setObjectName("DE_Acquisition_Info__scrollArea_1")
        self.DE_Acquisition_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Acquisition_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 249, 268))
        self.DE_Acquisition_Info__scrollAreaWidgetContents_1.setObjectName("DE_Acquisition_Info__scrollAreaWidgetContents_1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.DE_Acquisition_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Acquisition_Info__verticalLayout_1.setObjectName("DE_Acquisition_Info__verticalLayout_1")
        self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.setObjectName("DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_person_name__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_person_name__label_1.setObjectName("DE_Acquisition_Info_acquisition_person_name__label_1")
        self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_person_name__label_1)
        self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_person_name__lineEdit_1")
        self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1)
        self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.setObjectName("DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_date_time__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_date_time__label_1.setObjectName("DE_Acquisition_Info_acquisition_date_time__label_1")
        self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_date_time__label_1)
        self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_date_time__lineEdit_1")
        self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1)
        self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.setObjectName("DE_Acquisiton_Info_acquisition_location__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_location__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_location__label_1.setObjectName("DE_Acquisition_Info_acquisition_location__label_1")
        self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_location__label_1)
        self.DE_Acquisition_Info_acquisition_location__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_location__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_location__lineEdit_1")
        self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_location__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1)
        self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.setObjectName("DE_Acquisition_Info_acquisition_tool__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_tool__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_tool__label_1.setObjectName("DE_Acquisition_Info_acquisition_tool__label_1")
        self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_tool__label_1)
        self.DE_Acquisition_Info_acquisition_tool__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_tool__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_tool__lineEdit_1")
        self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_tool__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1)
        self.DE_Acquisition_Info_addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_addButton__horizontalLayout_1.setObjectName("DE_Acquisition_Info_addButton__horizontalLayout_1")
        self.DE_Acquisition_Info__blanklabel_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info__blanklabel_1.setText("")
        self.DE_Acquisition_Info__blanklabel_1.setObjectName("DE_Acquisition_Info__blanklabel_1")
        self.DE_Acquisition_Info_addButton__horizontalLayout_1.addWidget(self.DE_Acquisition_Info__blanklabel_1)
        self.DE_Acquisition_Info__addButton_1 = QtWidgets.QPushButton(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info__addButton_1.setObjectName("DE_Acquisition_Info__addButton_1")
        self.DE_Acquisition_Info_addButton__horizontalLayout_1.addWidget(self.DE_Acquisition_Info__addButton_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(self.DE_Acquisition_Info_addButton__horizontalLayout_1)
        self.DE_Acquisition_Info_file__scrollArea_1 = QtWidgets.QScrollArea(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_file__scrollArea_1.setWidgetResizable(True)
        self.DE_Acquisition_Info_file__scrollArea_1.setObjectName("DE_Acquisition_Info_file__scrollArea_1")
        self.DE_Aquisition_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Aquisition_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 344, 174))
        self.DE_Aquisition_Info__scrollAreaWidgetContents_1.setObjectName("DE_Aquisition_Info__scrollAreaWidgetContents_1")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.DE_Aquisition_Info_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Aquisition_Info_file__verticalLayout_1.setObjectName("DE_Aquisition_Info_file__verticalLayout_1")
        self.DE_Aquisition_Info_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Aquisition_Info_file_browse_horizontalLayout_1.setObjectName("DE_Aquisition_Info_file_browse_horizontalLayout_1")
        self.DE_Acquisition_Info_file_browse__label_1 = QtWidgets.QLabel(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_file_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        self.DE_Acquisition_Info_file_browse__label_1.setObjectName("DE_Acquisition_Info_file_browse__label_1")
        self.DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(self.DE_Acquisition_Info_file_browse__label_1)
        self.DE_Acquisition_Info_file_browse__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_file_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_file_browse__lineEdit_1")
        self.DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(self.DE_Acquisition_Info_file_browse__lineEdit_1)
        self.DE_Acquisition_Info_file_browse__browseButton_1 = QtWidgets.QPushButton(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_file_browse__browseButton_1.setObjectName("DE_Acquisition_Info_file_browse__browseButton_1")
        self.DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(self.DE_Acquisition_Info_file_browse__browseButton_1)
        self.DE_Acquisition_Info_file_browse__enterButton_1 = QtWidgets.QPushButton(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_file_browse__enterButton_1.setObjectName("DE_Acquisition_Info_file_browse__enterButton_1")
        self.DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(self.DE_Acquisition_Info_file_browse__enterButton_1)
        self.DE_Aquisition_Info_file__verticalLayout_1.addLayout(self.DE_Aquisition_Info_file_browse_horizontalLayout_1)
        self.DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1.setObjectName("DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1")
        self.DE_Acquisition_Info_digital_evidence_file_name__label_1 = QtWidgets.QLabel(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_digital_evidence_file_name__label_1.setObjectName("DE_Acquisition_Info_digital_evidence_file_name__label_1")
        self.DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_digital_evidence_file_name__label_1)
        self.DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1.setObjectName("DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1")
        self.DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        self.DE_Aquisition_Info_file__verticalLayout_1.addLayout(self.DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1)
        self.DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1.setObjectName("DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1")
        self.DE_Acquisition_Info_digital_evidence_file_path__label_1 = QtWidgets.QLabel(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_digital_evidence_file_path__label_1.setObjectName("DE_Acquisition_Info_digital_evidence_file_path__label_1")
        self.DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_digital_evidence_file_path__label_1)
        self.DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1.setObjectName("DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1")
        self.DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        self.DE_Aquisition_Info_file__verticalLayout_1.addLayout(self.DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1)
        self.DE_Acquisition_Info_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_hash_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_hash_type__horizontalLayout_1")
        self.DE_Acquisition_Info_hash_type__label_1 = QtWidgets.QLabel(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_hash_type__label_1.setObjectName("DE_Acquisition_Info_hash_type__label_1")
        self.DE_Acquisition_Info_hash_type__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_hash_type__label_1)
        self.DE_Acquisition_Info_hash_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_hash_type__lineEdit_1.setObjectName("DE_Acquisition_Info_hash_type__lineEdit_1")
        self.DE_Acquisition_Info_hash_type__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_hash_type__lineEdit_1)
        self.DE_Aquisition_Info_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_hash_type__horizontalLayout_1)
        self.DE_Acquisition_Info_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_hash_value__horizontalLayout_1.setObjectName("DE_Acquisition_Info_hash_value__horizontalLayout_1")
        self.DE_Acquisition_Info_hash_value__label_1 = QtWidgets.QLabel(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_hash_value__label_1.setObjectName("DE_Acquisition_Info_hash_value__label_1")
        self.DE_Acquisition_Info_hash_value__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_hash_value__label_1)
        self.DE_Acquisition_Info_hash_value__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_hash_value__lineEdit_1.setObjectName("DE_Acquisition_Info_hash_value__lineEdit_1")
        self.DE_Acquisition_Info_hash_value__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_hash_value__lineEdit_1)
        self.DE_Aquisition_Info_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_hash_value__horizontalLayout_1)
        self.gridLayout_15.addLayout(self.DE_Aquisition_Info_file__verticalLayout_1, 0, 0, 1, 1)
        self.DE_Acquisition_Info_file__scrollArea_1.setWidget(self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info__verticalLayout_1.addWidget(self.DE_Acquisition_Info_file__scrollArea_1)
        self.gridLayout_4.addLayout(self.DE_Acquisition_Info__verticalLayout_1, 0, 0, 1, 1)
        self.DE_Acquisition_Info__scrollArea_1.setWidget(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.gridLayout_5.addWidget(self.DE_Acquisition_Info__scrollArea_1, 4, 1, 1, 1)
        self.DE_Vessel_Info__scrollArea_1 = QtWidgets.QScrollArea(self.DE_sub__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info__scrollArea_1.setWidgetResizable(True)
        self.DE_Vessel_Info__scrollArea_1.setObjectName("DE_Vessel_Info__scrollArea_1")
        self.DE_Vessel_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Vessel_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 251, 287))
        self.DE_Vessel_Info__scrollAreaWidgetContents_1.setObjectName("DE_Vessel_Info__scrollAreaWidgetContents_1")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.DE_Vessel_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Vessel_Info__verticalLayout_1.setObjectName("DE_Vessel_Info__verticalLayout_1")
        self.DE_Veseel_Info_vessel_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Veseel_Info_vessel_name__horizontalLayout_1.setObjectName("DE_Veseel_Info_vessel_name__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_name__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_name__label_1.setObjectName("DE_Vessel_Info_vessel_name__label_1")
        self.DE_Veseel_Info_vessel_name__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_name__label_1)
        self.DE_Vessel_Info_vessel_name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_name__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_name__lineEdit_1")
        self.DE_Veseel_Info_vessel_name__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_name__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Veseel_Info_vessel_name__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_management_id__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_management_id__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_management_id__label_1.setObjectName("DE_Vessel_Info_vessel_management_id__label_1")
        self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_management_id__label_1)
        self.DE_Vessel_Info_vessel_management_id__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_management_id__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_management_id__lineEdit_1")
        self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_management_id__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_MMSI__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_MMSI__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_MMSI__label_1.setObjectName("DE_Vessel_Info_vessel_MMSI__label_1")
        self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_MMSI__label_1)
        self.DE_Vessel_Info_vessel_MMSI__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_MMSI__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_MMSI__lineEdit_1")
        self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_MMSI__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_callsign__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_callsign__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_callsign__label_1.setObjectName("DE_Vessel_Info_vessel_callsign__label_1")
        self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_callsign__label_1)
        self.DE_Vessel_Info_vessel_callsign__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_callsign__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_callsign__lineEdit_1")
        self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_callsign__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_IMO__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_IMO__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_IMO__label_1.setObjectName("DE_Vessel_Info_vessel_IMO__label_1")
        self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_IMO__label_1)
        self.DE_Vessel_Info_vessel_IMO__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_IMO__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_IMO__lineEdit_1")
        self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_IMO__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_MRN__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_MRN__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_MRN__label_1.setObjectName("DE_Vessel_Info_vessel_MRN__label_1")
        self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_MRN__label_1)
        self.DE_Vessel_Info_vessel_MRN__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_MRN__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_MRN__lineEdit_1")
        self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_MRN__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_tonnage__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_tonnage__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_tonnage__label_1.setObjectName("DE_Vessel_Info_vessel_tonnage__label_1")
        self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_tonnage__label_1)
        self.DE_Vessel_Info_vessel_tonnage__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_tonnage__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_tonnage__lineEdit_1")
        self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_tonnage__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_length__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_length__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_length__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_length__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_length__label_1.setObjectName("DE_Vessel_Info_vessel_length__label_1")
        self.DE_Vessel_Info_vessel_length__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_length__label_1)
        self.DE_Vessel_Info_vessel_length__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_length__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_length__lineEdit_1")
        self.DE_Vessel_Info_vessel_length__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_length__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_length__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1.setObjectName("DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1")
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1)
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1")
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1)
        self.gridLayout_20.addLayout(self.DE_Vessel_Info__verticalLayout_1, 0, 0, 1, 1)
        self.DE_Vessel_Info__scrollArea_1.setWidget(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.gridLayout_5.addWidget(self.DE_Vessel_Info__scrollArea_1, 2, 0, 1, 1)
        self.DE_Acquisition_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info__horizontalLayout_1.setObjectName("DE_Acquisition_Info__horizontalLayout_1")
        self.DE_Acquisition_Info__label_1 = QtWidgets.QLabel(self.DE_sub__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info__label_1.setObjectName("DE_Acquisition_Info__label_1")
        self.DE_Acquisition_Info__horizontalLayout_1.addWidget(self.DE_Acquisition_Info__label_1)
        self.gridLayout_5.addLayout(self.DE_Acquisition_Info__horizontalLayout_1, 3, 1, 1, 1)
        self.DE_Marines_Electronics_Info__scrollArea_1 = QtWidgets.QScrollArea(self.DE_sub__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info__scrollArea_1.setWidgetResizable(True)
        self.DE_Marines_Electronics_Info__scrollArea_1.setObjectName("DE_Marines_Electronics_Info__scrollArea_1")
        self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 249, 227))
        self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1.setObjectName("DE_Marines_Electronics_Info__scrollAreaWidgetContents_1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.DE_Marines_Electronics_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Marines_Electronics_Info__verticalLayout_1.setObjectName("DE_Marines_Electronics_Info__verticalLayout_1")
        self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_management_id__label_1 = QtWidgets.QLabel(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_management_id__label_1.setObjectName("DE_Marines_Electronics_Info_device_management_id__label_1")
        self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_management_id__label_1)
        self.DE_Marines_Electronics_Info_device_management_id__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_management_id__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_management_id__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_management_id__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_type__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_type__label_1 = QtWidgets.QLabel(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_type__label_1.setObjectName("DE_Marines_Electronics_Info_device_type__label_1")
        self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_type__label_1)
        self.DE_Marines_Electronics_Info_device_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_type__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_type__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_type__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_manufacturer__label_1 = QtWidgets.QLabel(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_manufacturer__label_1.setObjectName("DE_Marines_Electronics_Info_device_manufacturer__label_1")
        self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_manufacturer__label_1)
        self.DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_model_name__label_1 = QtWidgets.QLabel(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_model_name__label_1.setObjectName("DE_Marines_Electronics_Info_device_model_name__label_1")
        self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_model_name__label_1)
        self.DE_Marines_Electronics_Info_device_model_name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_model_name__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_model_name__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_model_name__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_model_serial_number__label_1 = QtWidgets.QLabel(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_model_serial_number__label_1.setObjectName("DE_Marines_Electronics_Info_device_model_serial_number__label_1")
        self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_model_serial_number__label_1)
        self.DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_os_firmware__label_1 = QtWidgets.QLabel(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_os_firmware__label_1.setObjectName("DE_Marines_Electronics_Info_device_os_firmware__label_1")
        self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_os_firmware__label_1)
        self.DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_description__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_description__label_1 = QtWidgets.QLabel(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_description__label_1.setObjectName("DE_Marines_Electronics_Info_device_description__label_1")
        self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_description__label_1)
        self.DE_Marines_Electronics_Info_device_description__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_description__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_description__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1.addWidget(self.DE_Marines_Electronics_Info_device_description__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1)
        self.gridLayout_6.addLayout(self.DE_Marines_Electronics_Info__verticalLayout_1, 0, 0, 1, 1)
        self.DE_Marines_Electronics_Info__scrollArea_1.setWidget(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.gridLayout_5.addWidget(self.DE_Marines_Electronics_Info__scrollArea_1, 2, 1, 1, 1)
        self.DE_other_files__scrollArea_1 = QtWidgets.QScrollArea(self.DE_sub__scrollAreaWidgetContents_1)
        self.DE_other_files__scrollArea_1.setWidgetResizable(True)
        self.DE_other_files__scrollArea_1.setObjectName("DE_other_files__scrollArea_1")
        self.DE_other_files__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_other_files__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 349, 294))
        self.DE_other_files__scrollAreaWidgetContents_1.setObjectName("DE_other_files__scrollAreaWidgetContents_1")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.DE_other_files__scrollAreaWidgetContents_1)
        self.gridLayout_13.setObjectName("gridLayout_13")

        self.DE_other_files__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_other_files__verticalLayout_1.setObjectName("DE_other_files__verticalLayout_1")
        self.DE_other_files_file_browse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_browse__horizontalLayout_1.setObjectName("DE_other_files_file_browse__horizontalLayout_1")
        self.DE_other_files_file_browse__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_browse__label_1.setObjectName("DE_other_files_file_browse__label_1")
        self.DE_other_files_file_browse__horizontalLayout_1.addWidget(self.DE_other_files_file_browse__label_1)
        self.DE_other_files_file_browse__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_browse__lineEdit_1.setObjectName("DE_other_files_file_browse__lineEdit_1")
        self.DE_other_files_file_browse__horizontalLayout_1.addWidget(self.DE_other_files_file_browse__lineEdit_1)
        self.DE_other_files_file_browse__browseButton_1 = QtWidgets.QPushButton(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_browse__browseButton_1.setObjectName("DE_other_files_file_browse__browseButton_1")
        self.DE_other_files_file_browse__horizontalLayout_1.addWidget(self.DE_other_files_file_browse__browseButton_1)
        self.DE_other_files_file_browse__EnterButton_1 = QtWidgets.QPushButton(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_browse__EnterButton_1.setObjectName("DE_other_files_file_browse__EnterButton_1")
        self.DE_other_files_file_browse__horizontalLayout_1.addWidget(self.DE_other_files_file_browse__EnterButton_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_browse__horizontalLayout_1)
        self.DE_other_files_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_id__horizontalLayout_1.setObjectName("DE_other_files_id__horizontalLayout_1")
        self.DE_other_files_id__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_id__label_1.setObjectName("DE_other_files_id__label_1")
        self.DE_other_files_id__horizontalLayout_1.addWidget(self.DE_other_files_id__label_1)
        self.DE_other_files_id__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_id__lineEdit_1.setObjectName("DE_other_files_id__lineEdit_1")
        self.DE_other_files_id__horizontalLayout_1.addWidget(self.DE_other_files_id__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_id__horizontalLayout_1)
        self.DE_other_files_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_type__horizontalLayout_1.setObjectName("DE_other_files_type__horizontalLayout_1")
        self.DE_other_files_type__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_type__label_1.setObjectName("DE_other_files_type__label_1")
        self.DE_other_files_type__horizontalLayout_1.addWidget(self.DE_other_files_type__label_1)
        self.DE_other_files_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_type__lineEdit_1.setObjectName("DE_other_files_type__lineEdit_1")
        self.DE_other_files_type__horizontalLayout_1.addWidget(self.DE_other_files_type__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_type__horizontalLayout_1)
        self.DE_other_files_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_size__horizontalLayout_1.setObjectName("DE_other_files_file_size__horizontalLayout_1")
        self.DE_other_files_file_size__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_size__label_1.setObjectName("DE_other_files_file_size__label_1")
        self.DE_other_files_file_size__horizontalLayout_1.addWidget(self.DE_other_files_file_size__label_1)
        self.DE_other_files_file_size__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_size__lineEdit_1.setObjectName("DE_other_files_file_size__lineEdit_1")
        self.DE_other_files_file_size__horizontalLayout_1.addWidget(self.DE_other_files_file_size__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_size__horizontalLayout_1)
        self.DE_other_files_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_path__horizontalLayout_1.setObjectName("DE_other_files_file_path__horizontalLayout_1")
        self.DE_other_files_file_path__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_path__label_1.setObjectName("DE_other_files_file_path__label_1")
        self.DE_other_files_file_path__horizontalLayout_1.addWidget(self.DE_other_files_file_path__label_1)
        self.DE_other_files_file_path__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_path__lineEdit_1.setObjectName("DE_other_files_file_path__lineEdit_1")
        self.DE_other_files_file_path__horizontalLayout_1.addWidget(self.DE_other_files_file_path__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_path__horizontalLayout_1)
        self.DE_other_files_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_hash_type__horizontalLayout_1.setObjectName("DE_other_files_file_hash_type__horizontalLayout_1")
        self.DE_other_files_file_hash_type__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_hash_type__label_1.setObjectName("DE_other_files_file_hash_type__label_1")
        self.DE_other_files_file_hash_type__horizontalLayout_1.addWidget(self.DE_other_files_file_hash_type__label_1)
        self.DE_other_files_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_hash_type__lineEdit_1.setObjectName("DE_other_files_file_hash_type__lineEdit_1")
        self.DE_other_files_file_hash_type__horizontalLayout_1.addWidget(self.DE_other_files_file_hash_type__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_hash_type__horizontalLayout_1)
        self.DE_other_files_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_hash_value__horizontalLayout_1.setObjectName("DE_other_files_file_hash_value__horizontalLayout_1")
        self.DE_other_files_file_hash_value__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_hash_value__label_1.setObjectName("DE_other_files_file_hash_value__label_1")
        self.DE_other_files_file_hash_value__horizontalLayout_1.addWidget(self.DE_other_files_file_hash_value__label_1)
        self.DE_other_files_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_hash_value__lineEdit_1.setObjectName("DE_other_files_file_hash_value__lineEdit_1")
        self.DE_other_files_file_hash_value__horizontalLayout_1.addWidget(self.DE_other_files_file_hash_value__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_hash_value__horizontalLayout_1)
        self.DE_other_files_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_description__horizontalLayout_1.setObjectName("DE_other_files_file_description__horizontalLayout_1")
        self.DE_other_files_file_description__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_description__label_1.setObjectName("DE_other_files_file_description__label_1")
        self.DE_other_files_file_description__horizontalLayout_1.addWidget(self.DE_other_files_file_description__label_1)
        self.DE_other_files_file_description__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_description__lineEdit_1.setObjectName("DE_other_files_file_description__lineEdit_1")
        self.DE_other_files_file_description__horizontalLayout_1.addWidget(self.DE_other_files_file_description__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_description__horizontalLayout_1)
        self.DE_other_files_file_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_metadata__horizontalLayout_1.setObjectName("DE_other_files_file_metadata__horizontalLayout_1")
        self.DE_other_files_file_metadata__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_metadata__label_1.setObjectName("DE_other_files_file_metadata__label_1")
        self.DE_other_files_file_metadata__horizontalLayout_1.addWidget(self.DE_other_files_file_metadata__label_1)
        self.DE_other_files_file_metadata__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_metadata__lineEdit_1.setObjectName("DE_other_files_file_metadata__lineEdit_1")
        self.DE_other_files_file_metadata__horizontalLayout_1.addWidget(self.DE_other_files_file_metadata__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_metadata__horizontalLayout_1)
        self.gridLayout_13.addLayout(self.DE_other_files__verticalLayout_1, 0, 0, 1, 1)
        self.DE_other_files__scrollArea_1.setWidget(self.DE_other_files__scrollAreaWidgetContents_1)
        self.gridLayout_5.addWidget(self.DE_other_files__scrollArea_1, 2, 2, 3, 1)
        self.DE_sub__scrollArea_1.setWidget(self.DE_sub__scrollAreaWidgetContents_1)
        self.DE_AddAll__verticalLayout_1.addWidget(self.DE_sub__scrollArea_1)
        self.gridLayout_7.addLayout(self.DE_AddAll__verticalLayout_1, 0, 0, 1, 1)
        self.DE__scrollArea_1.setWidget(self.DE__scrollAreaWidgetContents)
        self.gridLayout_9.addWidget(self.DE__scrollArea_1, 2, 0, 1, 2)
        self.tabWidget.addTab(self.DE_tab, "")
        self.AI_tab = QtWidgets.QWidget()
        self.AI_tab.setObjectName("AI_tab")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.AI_tab)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.AI_title__label = QtWidgets.QLabel(self.AI_tab)
        self.AI_title__label.setObjectName("AI_title__label")
        self.gridLayout_33.addWidget(self.AI_title__label, 0, 0, 1, 1)
        self.AI_scrollArea = QtWidgets.QScrollArea(self.AI_tab)
        self.AI_scrollArea.setWidgetResizable(True)
        self.AI_scrollArea.setObjectName("AI_scrollArea")
        self.AI_scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.AI_scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 796, 422))
        self.AI_scrollAreaWidgetContents_1.setObjectName("AI_scrollAreaWidgetContents_1")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.AI_scrollAreaWidgetContents_1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.AI_Reports_scrollArea = QtWidgets.QScrollArea(self.AI_scrollAreaWidgetContents_1)
        self.AI_Reports_scrollArea.setWidgetResizable(True)
        self.AI_Reports_scrollArea.setObjectName("AI_Reports_scrollArea")
        self.AI_Reports__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.AI_Reports__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 360, 504))
        self.AI_Reports__scrollAreaWidgetContents_1.setObjectName("AI_Reports__scrollAreaWidgetContents_1")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.AI_Reports__scrollAreaWidgetContents_1)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.AI_Reports__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.AI_Reports__verticalLayout_1.setObjectName("AI_Reports__verticalLayout_1")
        self.AI_Reports_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_id__horizontalLayout_1.setObjectName("AI_Reports_id__horizontalLayout_1")
        self.AI_Reports_id__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_id__label_1.setObjectName("AI_Reports_id__label_1")
        self.AI_Reports_id__horizontalLayout_1.addWidget(self.AI_Reports_id__label_1)
        self.AI_Reports_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_id__lineEdit_1.setObjectName("AI_Reports_id__lineEdit_1")
        self.AI_Reports_id__horizontalLayout_1.addWidget(self.AI_Reports_id__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_id__horizontalLayout_1)
        self.AI_Reports_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_type__horizontalLayout_1.setObjectName("AI_Reports_type__horizontalLayout_1")
        self.AI_Reports_type__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_type__label_1.setObjectName("AI_Reports_type__label_1")
        self.AI_Reports_type__horizontalLayout_1.addWidget(self.AI_Reports_type__label_1)
        self.AI_Reports_type__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_type__lineEdit_1.setObjectName("AI_Reports_type__lineEdit_1")
        self.AI_Reports_type__horizontalLayout_1.addWidget(self.AI_Reports_type__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_type__horizontalLayout_1)
        self.AI_Reports_subtype__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_subtype__horizontalLayout_1.setObjectName("AI_Reports_subtype__horizontalLayout_1")
        self.AI_Reports_subtype__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_subtype__label_1.setObjectName("AI_Reports_subtype__label_1")
        self.AI_Reports_subtype__horizontalLayout_1.addWidget(self.AI_Reports_subtype__label_1)
        self.AI_Reports_subtype__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_subtype__lineEdit_1.setObjectName("AI_Reports_subtype__lineEdit_1")
        self.AI_Reports_subtype__horizontalLayout_1.addWidget(self.AI_Reports_subtype__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_subtype__horizontalLayout_1)
        self.AI_Reports_mgmt_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_mgmt_id__horizontalLayout_1.setObjectName("AI_Reports_mgmt_id__horizontalLayout_1")
        self.AI_Reports_mgmt_id__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_mgmt_id__label_1.setObjectName("AI_Reports_mgmt_id__label_1")
        self.AI_Reports_mgmt_id__horizontalLayout_1.addWidget(self.AI_Reports_mgmt_id__label_1)
        self.AI_Reports_mgmt_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_mgmt_id__lineEdit_1.setObjectName("AI_Reports_mgmt_id__lineEdit_1")
        self.AI_Reports_mgmt_id__horizontalLayout_1.addWidget(self.AI_Reports_mgmt_id__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_mgmt_id__horizontalLayout_1)
        self.AI_Reports_submission_agency__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_submission_agency__horizontalLayout_1.setObjectName("AI_Reports_submission_agency__horizontalLayout_1")
        self.AI_Reports_submission_agency__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_submission_agency__label_1.setObjectName("AI_Reports_submission_agency__label_1")
        self.AI_Reports_submission_agency__horizontalLayout_1.addWidget(self.AI_Reports_submission_agency__label_1)
        self.AI_Reports_submission_agency__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_submission_agency__lineEdit_1.setObjectName("AI_Reports_submission_agency__lineEdit_1")
        self.AI_Reports_submission_agency__horizontalLayout_1.addWidget(self.AI_Reports_submission_agency__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_submission_agency__horizontalLayout_1)
        self.AI_Reports_reports_creation_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_reports_creation_datetime__horizontalLayout_1.setObjectName("AI_Reports_reports_creation_datetime__horizontalLayout_1")
        self.AI_Reports_reprot_creation_datetime__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_reprot_creation_datetime__label_1.setObjectName("AI_Reports_reprot_creation_datetime__label_1")
        self.AI_Reports_reports_creation_datetime__horizontalLayout_1.addWidget(self.AI_Reports_reprot_creation_datetime__label_1)
        self.AI_Reports_reprot_creation_datetime__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_reprot_creation_datetime__lineEdit_1.setObjectName("AI_Reports_reprot_creation_datetime__lineEdit_1")
        self.AI_Reports_reports_creation_datetime__horizontalLayout_1.addWidget(self.AI_Reports_reprot_creation_datetime__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_reports_creation_datetime__horizontalLayout_1)
        self.AI_Reports_division_name_of_report_maker__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_division_name_of_report_maker__horizontalLayout_1.setObjectName("AI_Reports_division_name_of_report_maker__horizontalLayout_1")
        self.AI_Reports_division_name_of_report_maker__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_division_name_of_report_maker__label_1.setObjectName("AI_Reports_division_name_of_report_maker__label_1")
        self.AI_Reports_division_name_of_report_maker__horizontalLayout_1.addWidget(self.AI_Reports_division_name_of_report_maker__label_1)
        self.AI_Reports_division_name_of_report_maker__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_division_name_of_report_maker__lineEdit_1.setObjectName("AI_Reports_division_name_of_report_maker__lineEdit_1")
        self.AI_Reports_division_name_of_report_maker__horizontalLayout_1.addWidget(self.AI_Reports_division_name_of_report_maker__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_division_name_of_report_maker__horizontalLayout_1)
        self.AI_Reports_team_name_of_report_maker__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_team_name_of_report_maker__horizontalLayout_1.setObjectName("AI_Reports_team_name_of_report_maker__horizontalLayout_1")
        self.AI_Reports_team_name_of_report_maker__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_team_name_of_report_maker__label_1.setObjectName("AI_Reports_team_name_of_report_maker__label_1")
        self.AI_Reports_team_name_of_report_maker__horizontalLayout_1.addWidget(self.AI_Reports_team_name_of_report_maker__label_1)
        self.AI_Reports_team_name_of_report_maker__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_team_name_of_report_maker__lineEdit_1.setObjectName("AI_Reports_team_name_of_report_maker__lineEdit_1")
        self.AI_Reports_team_name_of_report_maker__horizontalLayout_1.addWidget(self.AI_Reports_team_name_of_report_maker__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_team_name_of_report_maker__horizontalLayout_1)
        self.AI_Reports_file_info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_file_info__horizontalLayout_1.setObjectName("AI_Reports_file_info__horizontalLayout_1")
        self.AI_Reports_file_info__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_info__label_1.setObjectName("AI_Reports_file_info__label_1")
        self.AI_Reports_file_info__horizontalLayout_1.addWidget(self.AI_Reports_file_info__label_1)
        self.AI_Reports_file_info__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_info__lineEdit_1.setObjectName("AI_Reports_file_info__lineEdit_1")
        self.AI_Reports_file_info__horizontalLayout_1.addWidget(self.AI_Reports_file_info__lineEdit_1)
        self.AI_Reports_file_info__browseButton_1 = QtWidgets.QPushButton(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_info__browseButton_1.setObjectName("AI_Reports_file_info__browseButton_1")
        self.AI_Reports_file_info__horizontalLayout_1.addWidget(self.AI_Reports_file_info__browseButton_1)
        self.AI_Reports_file_info__enterButton_1 = QtWidgets.QPushButton(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_info__enterButton_1.setObjectName("AI_Reports_file_info__enterButton_1")
        self.AI_Reports_file_info__horizontalLayout_1.addWidget(self.AI_Reports_file_info__enterButton_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_file_info__horizontalLayout_1)
        self.AI_Reports_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_file_name__horizontalLayout_1.setObjectName("AI_Reports_file_name__horizontalLayout_1")
        self.AI_Reports_file_name__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_name__label_1.setObjectName("AI_Reports_file_name__label_1")
        self.AI_Reports_file_name__horizontalLayout_1.addWidget(self.AI_Reports_file_name__label_1)
        self.AI_Reports_file_name__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_name__lineEdit_1.setObjectName("AI_Reports_file_name__lineEdit_1")
        self.AI_Reports_file_name__horizontalLayout_1.addWidget(self.AI_Reports_file_name__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_file_name__horizontalLayout_1)
        self.AI_Reports_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_file_size__horizontalLayout_1.setObjectName("AI_Reports_file_size__horizontalLayout_1")
        self.AI_Reports_file_size__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_size__label_1.setObjectName("AI_Reports_file_size__label_1")
        self.AI_Reports_file_size__horizontalLayout_1.addWidget(self.AI_Reports_file_size__label_1)
        self.AI_Reports_file_size__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_size__lineEdit_1.setObjectName("AI_Reports_file_size__lineEdit_1")
        self.AI_Reports_file_size__horizontalLayout_1.addWidget(self.AI_Reports_file_size__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_file_size__horizontalLayout_1)
        self.AI_Reports_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_file_path__horizontalLayout_1.setObjectName("AI_Reports_file_path__horizontalLayout_1")
        self.AI_Reports_file_path__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_path__label_1.setObjectName("AI_Reports_file_path__label_1")
        self.AI_Reports_file_path__horizontalLayout_1.addWidget(self.AI_Reports_file_path__label_1)
        self.AI_Reports_file_path__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_path__lineEdit_1.setObjectName("AI_Reports_file_path__lineEdit_1")
        self.AI_Reports_file_path__horizontalLayout_1.addWidget(self.AI_Reports_file_path__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_file_path__horizontalLayout_1)
        self.AI_Reports_file_creation_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_file_creation_datetime__horizontalLayout_1.setObjectName("AI_Reports_file_creation_datetime__horizontalLayout_1")
        self.AI_Reports_file_creation_datetime__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_creation_datetime__label_1.setObjectName("AI_Reports_file_creation_datetime__label_1")
        self.AI_Reports_file_creation_datetime__horizontalLayout_1.addWidget(self.AI_Reports_file_creation_datetime__label_1)
        self.AI_Reports_file_creation_datetime__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_creation_datetime__lineEdit_1.setObjectName("AI_Reports_file_creation_datetime__lineEdit_1")
        self.AI_Reports_file_creation_datetime__horizontalLayout_1.addWidget(self.AI_Reports_file_creation_datetime__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_file_creation_datetime__horizontalLayout_1)
        self.AI_Reports_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_file_description__horizontalLayout_1.setObjectName("AI_Reports_file_description__horizontalLayout_1")
        self.AI_Reports_file_description__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_description__label_1.setObjectName("AI_Reports_file_description__label_1")
        self.AI_Reports_file_description__horizontalLayout_1.addWidget(self.AI_Reports_file_description__label_1)
        self.AI_Reports_file_description__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_description__lineEdit_1.setObjectName("AI_Reports_file_description__lineEdit_1")
        self.AI_Reports_file_description__horizontalLayout_1.addWidget(self.AI_Reports_file_description__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_file_description__horizontalLayout_1)
        self.AI_Reports_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_file_hash_type__horizontalLayout_1.setObjectName("AI_Reports_file_hash_type__horizontalLayout_1")
        self.AI_Reports_file_hash_type__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_hash_type__label_1.setObjectName("AI_Reports_file_hash_type__label_1")
        self.AI_Reports_file_hash_type__horizontalLayout_1.addWidget(self.AI_Reports_file_hash_type__label_1)
        self.AI_Reports_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_hash_type__lineEdit_1.setObjectName("AI_Reports_file_hash_type__lineEdit_1")
        self.AI_Reports_file_hash_type__horizontalLayout_1.addWidget(self.AI_Reports_file_hash_type__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_file_hash_type__horizontalLayout_1)
        self.AI_Reports_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Reports_file_hash_value__horizontalLayout_1.setObjectName("AI_Reports_file_hash_value__horizontalLayout_1")
        self.AI_Reports_file_hash_value__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_hash_value__label_1.setObjectName("AI_Reports_file_hash_value__label_1")
        self.AI_Reports_file_hash_value__horizontalLayout_1.addWidget(self.AI_Reports_file_hash_value__label_1)
        self.AI_Reports_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        self.AI_Reports_file_hash_value__lineEdit_1.setObjectName("AI_Reports_file_hash_value__lineEdit_1")
        self.AI_Reports_file_hash_value__horizontalLayout_1.addWidget(self.AI_Reports_file_hash_value__lineEdit_1)
        self.AI_Reports__verticalLayout_1.addLayout(self.AI_Reports_file_hash_value__horizontalLayout_1)
        self.gridLayout_12.addLayout(self.AI_Reports__verticalLayout_1, 0, 0, 1, 1)
        self.AI_Reports_scrollArea.setWidget(self.AI_Reports__scrollAreaWidgetContents_1)
        self.gridLayout_10.addWidget(self.AI_Reports_scrollArea, 5, 0, 1, 1)
        self.AI_other_files__scrollArea = QtWidgets.QScrollArea(self.AI_scrollAreaWidgetContents_1)
        self.AI_other_files__scrollArea.setWidgetResizable(True)
        self.AI_other_files__scrollArea.setObjectName("AI_other_files__scrollArea")
        self.AI__scrollAreaWidgetContents = QtWidgets.QWidget()
        self.AI__scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 382, 361))
        self.AI__scrollAreaWidgetContents.setObjectName("AI__scrollAreaWidgetContents")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.AI__scrollAreaWidgetContents)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.AI_other_files__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.AI_other_files__verticalLayout_1.setObjectName("AI_other_files__verticalLayout_1")
        self.AI_other_files_file_browse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files_file_browse__horizontalLayout_1.setObjectName("AI_other_files_file_browse__horizontalLayout_1")
        self.AI_other_files_file_browse__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_browse__label_1.setObjectName("AI_other_files_file_browse__label_1")
        self.AI_other_files_file_browse__horizontalLayout_1.addWidget(self.AI_other_files_file_browse__label_1)
        self.AI_other_files_file_browse__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_browse__lineEdit_1.setObjectName("AI_other_files_file_browse__lineEdit_1")
        self.AI_other_files_file_browse__horizontalLayout_1.addWidget(self.AI_other_files_file_browse__lineEdit_1)
        self.AI_other_files_file_browse__browseButton_1 = QtWidgets.QPushButton(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_browse__browseButton_1.setObjectName("AI_other_files_file_browse__browseButton_1")
        self.AI_other_files_file_browse__horizontalLayout_1.addWidget(self.AI_other_files_file_browse__browseButton_1)
        self.AI_other_files_file_browse__enterButton_1 = QtWidgets.QPushButton(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_browse__enterButton_1.setObjectName("AI_other_files_file_browse__enterButton_1")
        self.AI_other_files_file_browse__horizontalLayout_1.addWidget(self.AI_other_files_file_browse__enterButton_1)
        self.AI_other_files__verticalLayout_1.addLayout(self.AI_other_files_file_browse__horizontalLayout_1)
        self.AI_other_files_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files_id__horizontalLayout_1.setObjectName("AI_other_files_id__horizontalLayout_1")
        self.AI_other_files_id__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_id__label_1.setObjectName("AI_other_files_id__label_1")
        self.AI_other_files_id__horizontalLayout_1.addWidget(self.AI_other_files_id__label_1)
        self.AI_other_files_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_id__lineEdit_1.setObjectName("AI_other_files_id__lineEdit_1")
        self.AI_other_files_id__horizontalLayout_1.addWidget(self.AI_other_files_id__lineEdit_1)
        self.AI_other_files__verticalLayout_1.addLayout(self.AI_other_files_id__horizontalLayout_1)
        self.AI_other_files_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files_type__horizontalLayout_1.setObjectName("AI_other_files_type__horizontalLayout_1")
        self.AI_other_files_type__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_type__label_1.setObjectName("AI_other_files_type__label_1")
        self.AI_other_files_type__horizontalLayout_1.addWidget(self.AI_other_files_type__label_1)
        self.AI_other_files_type__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_type__lineEdit_1.setObjectName("AI_other_files_type__lineEdit_1")
        self.AI_other_files_type__horizontalLayout_1.addWidget(self.AI_other_files_type__lineEdit_1)
        self.AI_other_files__verticalLayout_1.addLayout(self.AI_other_files_type__horizontalLayout_1)
        self.AI_other_files_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files_file_size__horizontalLayout_1.setObjectName("AI_other_files_file_size__horizontalLayout_1")
        self.AI_other_files_file_size__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_size__label_1.setObjectName("AI_other_files_file_size__label_1")
        self.AI_other_files_file_size__horizontalLayout_1.addWidget(self.AI_other_files_file_size__label_1)
        self.AI_other_files_file_size__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_size__lineEdit_1.setObjectName("AI_other_files_file_size__lineEdit_1")
        self.AI_other_files_file_size__horizontalLayout_1.addWidget(self.AI_other_files_file_size__lineEdit_1)
        self.AI_other_files__verticalLayout_1.addLayout(self.AI_other_files_file_size__horizontalLayout_1)
        self.AI_other_files_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files_file_path__horizontalLayout_1.setObjectName("AI_other_files_file_path__horizontalLayout_1")
        self.AI_other_files_file_path__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_path__label_1.setObjectName("AI_other_files_file_path__label_1")
        self.AI_other_files_file_path__horizontalLayout_1.addWidget(self.AI_other_files_file_path__label_1)
        self.AI_other_files_file_path__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_path__lineEdit_1.setObjectName("AI_other_files_file_path__lineEdit_1")
        self.AI_other_files_file_path__horizontalLayout_1.addWidget(self.AI_other_files_file_path__lineEdit_1)
        self.AI_other_files__verticalLayout_1.addLayout(self.AI_other_files_file_path__horizontalLayout_1)
        self.AI_other_files_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files_file_hash_type__horizontalLayout_1.setObjectName("AI_other_files_file_hash_type__horizontalLayout_1")
        self.AI_other_files_file_hash_type__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_hash_type__label_1.setObjectName("AI_other_files_file_hash_type__label_1")
        self.AI_other_files_file_hash_type__horizontalLayout_1.addWidget(self.AI_other_files_file_hash_type__label_1)
        self.AI_other_files_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_hash_type__lineEdit_1.setObjectName("AI_other_files_file_hash_type__lineEdit_1")
        self.AI_other_files_file_hash_type__horizontalLayout_1.addWidget(self.AI_other_files_file_hash_type__lineEdit_1)
        self.AI_other_files__verticalLayout_1.addLayout(self.AI_other_files_file_hash_type__horizontalLayout_1)
        self.AI_other_files_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files_file_hash_value__horizontalLayout_1.setObjectName("AI_other_files_file_hash_value__horizontalLayout_1")
        self.AI_other_files_file_hash_value__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_hash_value__label_1.setObjectName("AI_other_files_file_hash_value__label_1")
        self.AI_other_files_file_hash_value__horizontalLayout_1.addWidget(self.AI_other_files_file_hash_value__label_1)
        self.AI_other_files_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_hash_value__lineEdit_1.setObjectName("AI_other_files_file_hash_value__lineEdit_1")
        self.AI_other_files_file_hash_value__horizontalLayout_1.addWidget(self.AI_other_files_file_hash_value__lineEdit_1)
        self.AI_other_files__verticalLayout_1.addLayout(self.AI_other_files_file_hash_value__horizontalLayout_1)
        self.AI_other_files_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files_file_description__horizontalLayout_1.setObjectName("AI_other_files_file_description__horizontalLayout_1")
        self.AI_other_files_file_description__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_description__label_1.setObjectName("AI_other_files_file_description__label_1")
        self.AI_other_files_file_description__horizontalLayout_1.addWidget(self.AI_other_files_file_description__label_1)
        self.AI_other_files_file_description__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_description__lineEdit_1.setObjectName("AI_other_files_file_description__lineEdit_1")
        self.AI_other_files_file_description__horizontalLayout_1.addWidget(self.AI_other_files_file_description__lineEdit_1)
        self.AI_other_files__verticalLayout_1.addLayout(self.AI_other_files_file_description__horizontalLayout_1)
        self.AI_other_files_file_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files_file_metadata__horizontalLayout_1.setObjectName("AI_other_files_file_metadata__horizontalLayout_1")
        self.AI_other_files_file_metadata__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_metadata__label_1.setObjectName("AI_other_files_file_metadata__label_1")
        self.AI_other_files_file_metadata__horizontalLayout_1.addWidget(self.AI_other_files_file_metadata__label_1)
        self.AI_other_files_file_metadata__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        self.AI_other_files_file_metadata__lineEdit_1.setObjectName("AI_other_files_file_metadata__lineEdit_1")
        self.AI_other_files_file_metadata__horizontalLayout_1.addWidget(self.AI_other_files_file_metadata__lineEdit_1)
        self.AI_other_files__verticalLayout_1.addLayout(self.AI_other_files_file_metadata__horizontalLayout_1)
        self.gridLayout_11.addLayout(self.AI_other_files__verticalLayout_1, 0, 0, 1, 1)
        self.AI_other_files__scrollArea.setWidget(self.AI__scrollAreaWidgetContents)
        self.gridLayout_10.addWidget(self.AI_other_files__scrollArea, 5, 1, 3, 1)
        self.AI_EquipmentTraces__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces__horizontalLayout_1.setObjectName("AI_EquipmentTraces__horizontalLayout_1")
        self.AI_EquipmentTraces__label = QtWidgets.QLabel(self.AI_scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces__label.setObjectName("AI_EquipmentTraces__label")
        self.AI_EquipmentTraces__horizontalLayout_1.addWidget(self.AI_EquipmentTraces__label)
        self.AI_EquipmentTraces__addButton = QtWidgets.QPushButton(self.AI_scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces__addButton.setObjectName("AI_EquipmentTraces__addButton")
        self.AI_EquipmentTraces__horizontalLayout_1.addWidget(self.AI_EquipmentTraces__addButton)
        self.gridLayout_10.addLayout(self.AI_EquipmentTraces__horizontalLayout_1, 6, 0, 1, 1)
        self.AI_EquipmentTraces__scrollArea_1 = QtWidgets.QScrollArea(self.AI_scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces__scrollArea_1.setWidgetResizable(True)
        self.AI_EquipmentTraces__scrollArea_1.setObjectName("AI_EquipmentTraces__scrollArea_1")
        self.AI_EquipmentTraces__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.AI_EquipmentTraces__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 381, 317))
        self.AI_EquipmentTraces__scrollAreaWidgetContents_1.setObjectName("AI_EquipmentTraces__scrollAreaWidgetContents_1")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.AI_EquipmentTraces__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.AI_EquipmentTraces__verticalLayout_1.setObjectName("AI_EquipmentTraces__verticalLayout_1")
        self.AI_EquipmentTraces_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_id__horizontalLayout_1.setObjectName("AI_EquipmentTraces_id__horizontalLayout_1")
        self.AI_EquipmentTraces_id__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_id__label_1.setObjectName("AI_EquipmentTraces_id__label_1")
        self.AI_EquipmentTraces_id__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_id__label_1)
        self.AI_EquipmentTraces_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_id__lineEdit_1.setReadOnly(True)
        self.AI_EquipmentTraces_id__lineEdit_1.setObjectName("AI_EquipmentTraces_id__lineEdit_1")
        self.AI_EquipmentTraces_id__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_id__lineEdit_1)
        self.AI_EquipmentTraces__verticalLayout_1.addLayout(self.AI_EquipmentTraces_id__horizontalLayout_1)
        self.AI_EquipmentTraces_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_type__horizontalLayout_1.setObjectName("AI_EquipmentTraces_type__horizontalLayout_1")
        self.AI_EquipmentTraces_type__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_type__label_1.setObjectName("AI_EquipmentTraces_type__label_1")
        self.AI_EquipmentTraces_type__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_type__label_1)
        self.AI_EquipmentTraces_type__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_type__lineEdit_1.setObjectName("AI_EquipmentTraces_type__lineEdit_1")
        self.AI_EquipmentTraces_type__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_type__lineEdit_1)
        self.AI_EquipmentTraces__verticalLayout_1.addLayout(self.AI_EquipmentTraces_type__horizontalLayout_1)
        self.AI_EquipmentTraces_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_description__horizontalLayout_1.setObjectName("AI_EquipmentTraces_description__horizontalLayout_1")
        self.AI_EquipmentTraces_description__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_description__label_1.setObjectName("AI_EquipmentTraces_description__label_1")
        self.AI_EquipmentTraces_description__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_description__label_1)
        self.AI_EquipmentTraces_description__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_description__lineEdit_1.setObjectName("AI_EquipmentTraces_description__lineEdit_1")
        self.AI_EquipmentTraces_description__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_description__lineEdit_1)
        self.AI_EquipmentTraces__verticalLayout_1.addLayout(self.AI_EquipmentTraces_description__horizontalLayout_1)
        self.AI_EquipmentTraces_mgmt_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_mgmt_id__horizontalLayout_1.setObjectName("AI_EquipmentTraces_mgmt_id__horizontalLayout_1")
        self.AI_EquipmentTraces_mgmt_id__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_mgmt_id__label_1.setObjectName("AI_EquipmentTraces_mgmt_id__label_1")
        self.AI_EquipmentTraces_mgmt_id__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_mgmt_id__label_1)
        self.AI_EquipmentTraces_mgmt_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_mgmt_id__lineEdit_1.setObjectName("AI_EquipmentTraces_mgmt_id__lineEdit_1")
        self.AI_EquipmentTraces_mgmt_id__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_mgmt_id__lineEdit_1)
        self.AI_EquipmentTraces__verticalLayout_1.addLayout(self.AI_EquipmentTraces_mgmt_id__horizontalLayout_1)
        self.AI_EquipmentTraces_vessel_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_vessel_id__horizontalLayout_1.setObjectName("AI_EquipmentTraces_vessel_id__horizontalLayout_1")
        self.AI_EquipmentTraces_vessel_id__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_vessel_id__label_1.setObjectName("AI_EquipmentTraces_vessel_id__label_1")
        self.AI_EquipmentTraces_vessel_id__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_vessel_id__label_1)
        self.AI_EquipmentTraces_vessel_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_vessel_id__lineEdit_1.setObjectName("AI_EquipmentTraces_vessel_id__lineEdit_1")
        self.AI_EquipmentTraces_vessel_id__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_vessel_id__lineEdit_1)
        self.AI_EquipmentTraces__verticalLayout_1.addLayout(self.AI_EquipmentTraces_vessel_id__horizontalLayout_1)
        self.AI_EquipmentTraces_evidence_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_evidence_id__horizontalLayout_1.setObjectName("AI_EquipmentTraces_evidence_id__horizontalLayout_1")
        self.AI_EquipmentTraces_evidence_id__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_evidence_id__label_1.setObjectName("AI_EquipmentTraces_evidence_id__label_1")
        self.AI_EquipmentTraces_evidence_id__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_evidence_id__label_1)
        self.AI_EquipmentTraces_evidence_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_evidence_id__lineEdit_1.setObjectName("AI_EquipmentTraces_evidence_id__lineEdit_1")
        self.AI_EquipmentTraces_evidence_id__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_evidence_id__lineEdit_1)
        self.AI_EquipmentTraces__verticalLayout_1.addLayout(self.AI_EquipmentTraces_evidence_id__horizontalLayout_1)
        self.AI_EquipmentTraces_user_trace_info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_trace_info__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info__horizontalLayout_1")
        self.AI_EquipmentTraces_user_trace_info__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info__label_1.setObjectName("AI_EquipmentTraces_user_trace_info__label_1")
        self.AI_EquipmentTraces_user_trace_info__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info__label_1)
        self.AI_EquipmentTraces__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_trace_info__horizontalLayout_1)
        self.AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1")
        self.AI_EquipmentTraces_user_traces_info_sub__scrollArea_1 = QtWidgets.QScrollArea(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_traces_info_sub__scrollArea_1.setWidgetResizable(True)
        self.AI_EquipmentTraces_user_traces_info_sub__scrollArea_1.setObjectName("AI_EquipmentTraces_user_traces_info_sub__scrollArea_1")
        self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 332, 257))
        self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1.setObjectName("AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.setObjectName("AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1")
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1")
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1")
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1)
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1")
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1)
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1)
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1")
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1")
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1)
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1")
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1)
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1)
        self.AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1")
        self.AI_EquipmentTraces_user_trace_info_system_description__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_system_description__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_description__label_1")
        self.AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_system_description__label_1)
        self.AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1")
        self.AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1)
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1)
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1")
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_operation_status__label_1")
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_system_operation_status__label_1)
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1")
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1)
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1)
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1")
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1")
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1)
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1")
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1)
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1)
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1")
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_recording_period__label_1")
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_track_recording_period__label_1)
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1")
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1)
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1)
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1")
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1")
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1)
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1")
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1)
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1)
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1")
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1")
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1)
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1 = QtWidgets.QLineEdit(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1")
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1)
        self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1)
        self.gridLayout_14.addLayout(self.AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1, 0, 0, 1, 1)
        self.AI_EquipmentTraces_user_traces_info_sub__scrollArea_1.setWidget(self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1.addWidget(self.AI_EquipmentTraces_user_traces_info_sub__scrollArea_1)
        self.AI_EquipmentTraces__verticalLayout_1.addLayout(self.AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1)
        self.gridLayout_19.addLayout(self.AI_EquipmentTraces__verticalLayout_1, 0, 0, 2, 2)
        self.AI_EquipmentTraces__scrollArea_1.setWidget(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        self.gridLayout_10.addWidget(self.AI_EquipmentTraces__scrollArea_1, 7, 0, 1, 1)
        self.AI_other_files__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files__horizontalLayout_1.setObjectName("AI_other_files__horizontalLayout_1")
        self.AI_other_files__label_1 = QtWidgets.QLabel(self.AI_scrollAreaWidgetContents_1)
        self.AI_other_files__label_1.setObjectName("AI_other_files__label_1")
        self.AI_other_files__horizontalLayout_1.addWidget(self.AI_other_files__label_1)
        self.AI_other_files__addButton = QtWidgets.QPushButton(self.AI_scrollAreaWidgetContents_1)
        self.AI_other_files__addButton.setObjectName("AI_other_files__addButton")
        self.AI_other_files__horizontalLayout_1.addWidget(self.AI_other_files__addButton)
        self.gridLayout_10.addLayout(self.AI_other_files__horizontalLayout_1, 4, 1, 1, 1)
        self.AI_Report__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Report__horizontalLayout_1.setObjectName("AI_Report__horizontalLayout_1")
        self.AI_Report__label = QtWidgets.QLabel(self.AI_scrollAreaWidgetContents_1)
        self.AI_Report__label.setObjectName("AI_Report__label")
        self.AI_Report__horizontalLayout_1.addWidget(self.AI_Report__label)
        self.AI_Reports__addButton = QtWidgets.QPushButton(self.AI_scrollAreaWidgetContents_1)
        self.AI_Reports__addButton.setObjectName("AI_Reports__addButton")
        self.AI_Report__horizontalLayout_1.addWidget(self.AI_Reports__addButton)
        self.gridLayout_10.addLayout(self.AI_Report__horizontalLayout_1, 4, 0, 1, 1)
        self.AI_scrollArea.setWidget(self.AI_scrollAreaWidgetContents_1)
        self.gridLayout_33.addWidget(self.AI_scrollArea, 1, 0, 1, 2)
        self.tabWidget.addTab(self.AI_tab, "")
        self.DEPL_tab = QtWidgets.QWidget()
        self.DEPL_tab.setObjectName("DEPL_tab")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.DEPL_tab)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_127 = QtWidgets.QLabel(self.DEPL_tab)
        self.label_127.setText("")
        self.label_127.setObjectName("label_127")
        self.gridLayout_17.addWidget(self.label_127, 0, 2, 1, 1)
        self.DEPL__addButton = QtWidgets.QPushButton(self.DEPL_tab)
        self.DEPL__addButton.setObjectName("DEPL__addButton")
        self.gridLayout_17.addWidget(self.DEPL__addButton, 0, 3, 1, 1)
        self.DEPL__scrollArea = QtWidgets.QScrollArea(self.DEPL_tab)
        self.DEPL__scrollArea.setWidgetResizable(True)
        self.DEPL__scrollArea.setObjectName("DEPL__scrollArea")
        self.scrollAreaWidgetContents_12 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 796, 399))
        self.scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_12)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.DEPL__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DEPL__verticalLayout_1.setObjectName("DEPL__verticalLayout_1")
        self.DEPL_digital_evidence_package_management_id___horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DEPL_digital_evidence_package_management_id___horizontalLayout_1.setObjectName("DEPL_digital_evidence_package_management_id___horizontalLayout_1")
        self.DEPL_digital_evidence_package_management_id__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.DEPL_digital_evidence_package_management_id__label_1.setObjectName("DEPL_digital_evidence_package_management_id__label_1")
        self.DEPL_digital_evidence_package_management_id___horizontalLayout_1.addWidget(self.DEPL_digital_evidence_package_management_id__label_1)
        self.DEPL_digital_evidence_package_management_id__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.DEPL_digital_evidence_package_management_id__lineEdit_1.setObjectName("DEPL_digital_evidence_package_management_id__lineEdit_1")
        self.DEPL_digital_evidence_package_management_id___horizontalLayout_1.addWidget(self.DEPL_digital_evidence_package_management_id__lineEdit_1)
        self.DEPL__verticalLayout_1.addLayout(self.DEPL_digital_evidence_package_management_id___horizontalLayout_1)
        self.DEPL_log_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DEPL_log_datetime__horizontalLayout_1.setObjectName("DEPL_log_datetime__horizontalLayout_1")
        self.DEPL_log_datetime__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.DEPL_log_datetime__label_1.setObjectName("DEPL_log_datetime__label_1")
        self.DEPL_log_datetime__horizontalLayout_1.addWidget(self.DEPL_log_datetime__label_1)
        self.DEPL_log_datetime__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.DEPL_log_datetime__lineEdit_1.setObjectName("DEPL_log_datetime__lineEdit_1")
        self.DEPL_log_datetime__horizontalLayout_1.addWidget(self.DEPL_log_datetime__lineEdit_1)
        self.DEPL__verticalLayout_1.addLayout(self.DEPL_log_datetime__horizontalLayout_1)
        self.DEPL_log_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DEPL_log_type__horizontalLayout_1.setObjectName("DEPL_log_type__horizontalLayout_1")
        self.DEPL_log_type__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.DEPL_log_type__label_1.setObjectName("DEPL_log_type__label_1")
        self.DEPL_log_type__horizontalLayout_1.addWidget(self.DEPL_log_type__label_1)
        self.DEPL_log_type__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.DEPL_log_type__lineEdit_1.setObjectName("DEPL_log_type__lineEdit_1")
        self.DEPL_log_type__horizontalLayout_1.addWidget(self.DEPL_log_type__lineEdit_1)
        self.DEPL__verticalLayout_1.addLayout(self.DEPL_log_type__horizontalLayout_1)
        self.DEPL_log_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DEPL_log_description__horizontalLayout_1.setObjectName("DEPL_log_description__horizontalLayout_1")
        self.DEPL_log_description__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.DEPL_log_description__label_1.setObjectName("DEPL_log_description__label_1")
        self.DEPL_log_description__horizontalLayout_1.addWidget(self.DEPL_log_description__label_1)
        self.DEPL_log_description__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.DEPL_log_description__lineEdit_1.setObjectName("DEPL_log_description__lineEdit_1")
        self.DEPL_log_description__horizontalLayout_1.addWidget(self.DEPL_log_description__lineEdit_1)
        self.DEPL__verticalLayout_1.addLayout(self.DEPL_log_description__horizontalLayout_1)
        self.DEPL_devision_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DEPL_devision_name_of_logger__horizontalLayout_1.setObjectName("DEPL_devision_name_of_logger__horizontalLayout_1")
        self.DEPL_devision_name_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.DEPL_devision_name_of_logger__label_1.setObjectName("DEPL_devision_name_of_logger__label_1")
        self.DEPL_devision_name_of_logger__horizontalLayout_1.addWidget(self.DEPL_devision_name_of_logger__label_1)
        self.DEPL_devision_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.DEPL_devision_name_of_logger__lineEdit_1.setObjectName("DEPL_devision_name_of_logger__lineEdit_1")
        self.DEPL_devision_name_of_logger__horizontalLayout_1.addWidget(self.DEPL_devision_name_of_logger__lineEdit_1)
        self.DEPL__verticalLayout_1.addLayout(self.DEPL_devision_name_of_logger__horizontalLayout_1)
        self.DEPL_team_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DEPL_team_name_of_logger__horizontalLayout_1.setObjectName("DEPL_team_name_of_logger__horizontalLayout_1")
        self.DEPL_team_name_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.DEPL_team_name_of_logger__label_1.setObjectName("DEPL_team_name_of_logger__label_1")
        self.DEPL_team_name_of_logger__horizontalLayout_1.addWidget(self.DEPL_team_name_of_logger__label_1)
        self.DEPL_team_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.DEPL_team_name_of_logger__lineEdit_1.setObjectName("DEPL_team_name_of_logger__lineEdit_1")
        self.DEPL_team_name_of_logger__horizontalLayout_1.addWidget(self.DEPL_team_name_of_logger__lineEdit_1)
        self.DEPL__verticalLayout_1.addLayout(self.DEPL_team_name_of_logger__horizontalLayout_1)
        self.DEPL_rank_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DEPL_rank_of_logger__horizontalLayout_1.setObjectName("DEPL_rank_of_logger__horizontalLayout_1")
        self.DEPL_rank_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.DEPL_rank_of_logger__label_1.setObjectName("DEPL_rank_of_logger__label_1")
        self.DEPL_rank_of_logger__horizontalLayout_1.addWidget(self.DEPL_rank_of_logger__label_1)
        self.DEPL_rank_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.DEPL_rank_of_logger__lineEdit_1.setObjectName("DEPL_rank_of_logger__lineEdit_1")
        self.DEPL_rank_of_logger__horizontalLayout_1.addWidget(self.DEPL_rank_of_logger__lineEdit_1)
        self.DEPL__verticalLayout_1.addLayout(self.DEPL_rank_of_logger__horizontalLayout_1)
        self.DEPL_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DEPL_name_of_logger__horizontalLayout_1.setObjectName("DEPL_name_of_logger__horizontalLayout_1")
        self.DEPL_name_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.DEPL_name_of_logger__label_1.setObjectName("DEPL_name_of_logger__label_1")
        self.DEPL_name_of_logger__horizontalLayout_1.addWidget(self.DEPL_name_of_logger__label_1)
        self.DEPL_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.DEPL_name_of_logger__lineEdit_1.setObjectName("DEPL_name_of_logger__lineEdit_1")
        self.DEPL_name_of_logger__horizontalLayout_1.addWidget(self.DEPL_name_of_logger__lineEdit_1)
        self.DEPL__verticalLayout_1.addLayout(self.DEPL_name_of_logger__horizontalLayout_1)
        self.gridLayout_16.addLayout(self.DEPL__verticalLayout_1, 0, 0, 1, 1)
        self.DEPL__scrollArea.setWidget(self.scrollAreaWidgetContents_12)
        self.gridLayout_17.addWidget(self.DEPL__scrollArea, 1, 0, 1, 4)
        self.DEPL_Digital_Evidence_Package_Log__label = QtWidgets.QLabel(self.DEPL_tab)
        self.DEPL_Digital_Evidence_Package_Log__label.setObjectName("DEPL_Digital_Evidence_Package_Log__label")
        self.gridLayout_17.addWidget(self.DEPL_Digital_Evidence_Package_Log__label, 0, 0, 1, 1)
        self.label_126 = QtWidgets.QLabel(self.DEPL_tab)
        self.label_126.setText("")
        self.label_126.setObjectName("label_126")
        self.gridLayout_17.addWidget(self.label_126, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.DEPL_tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_17.addWidget(self.line, 2, 0, 1, 1)
        self.tabWidget.addTab(self.DEPL_tab, "")
        self.gridLayout_8.addWidget(self.tabWidget, 1, 0, 1, 1)
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)


        self.DE_Gather_Info_File_List.append(self.gridLayout_18)  # 이거를 저장
        self.DE_Acquisition_Info_File_List.append(self.gridLayout_15)  # 이거를 저장
        self.DE_Other_Files_File_List.append(self.gridLayout_13)

        ### 초기 readonly
        self.DE_Gather_Info_gather_media_type__lineEdit_1.setReadOnly(True)
        self.DE_Gather_Info__gather_hash_type__lineEdit_1.setReadOnly(True)
        self.DE_Gather_Info_gather_hash__lineEdit_1.setReadOnly(True)
        self.DE_Gather_Info_gather_path__lineEdit_1.setReadOnly(True)

        self.DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1.setReadOnly(True)
        self.DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1.setReadOnly(True)
        self.DE_Acquisition_Info_hash_type__lineEdit_1.setReadOnly(True)
        self.DE_Acquisition_Info_hash_value__lineEdit_1.setReadOnly(True)

        self.AI_Reports_file_name__lineEdit_1.setReadOnly(True)
        self.AI_Reports_file_size__lineEdit_1.setReadOnly(True)
        self.AI_Reports_file_path__lineEdit_1.setReadOnly(True)
        self.AI_Reports_file_creation_datetime__lineEdit_1.setReadOnly(True)
        self.AI_Reports_file_hash_type__lineEdit_1.setReadOnly(True)
        self.AI_Reports_file_hash_value__lineEdit_1.setReadOnly(True)

        self.AI_other_files_type__lineEdit_1.setReadOnly(True)
        self.AI_other_files_file_size__lineEdit_1.setReadOnly(True)
        self.AI_other_files_file_path__lineEdit_1.setReadOnly(True)
        self.AI_other_files_file_hash_type__lineEdit_1.setReadOnly(True)
        self.AI_other_files_file_hash_value__lineEdit_1.setReadOnly(True)
        self.AI_other_files_file_metadata__lineEdit_1.setReadOnly(False)

        self.DEPL_log_datetime__lineEdit_1.setReadOnly(True)

        self.CI_List.append(self.case_management_id__lineEdit)
        self.CI_List.append(self.agency_case_no__lineEdit)
        self.CI_List.append(self.agency_organization_code__lineEdit)
        self.CI_List.append(self.agency_organization_name__lineEdit)
        self.CI_List.append(self.agency_organization_party_name__lineEdit)
        self.CI_List.append(self.contents_of_request__lineEdit)
        self.CI_List.append(self.case_summary__lineEdit)
        self.CI_List.append(self.case_description__lineEdit)
        self.CI_List.append(self.case_datetime__lineEdit)
        self.CI_List.append(self.ordering_datetime__lineEdit)

        # self.DE_AddAll_num = 1
        # self.DE_AddAll_List = list()
        tmp_list = list()
        tmp_list.append(self.DE_management_id__lineEdit_1)
        tmp_list.append(self.DE_digital_evidence_type__lineEdit_1)
        tmp_list.append(self.DE_evidences_gathering_type__ineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_name__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_management_id__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_MMSI__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_callsign__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_IMO__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_MRN__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_tonnage__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_length__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1)
        tmp_list.append(self.DE_Marines_Electronics_Info_device_management_id__lineEdit_1)
        tmp_list.append(self.DE_Marines_Electronics_Info_device_type__lineEdit_1)
        tmp_list.append(self.DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1)
        tmp_list.append(self.DE_Marines_Electronics_Info_device_model_name__lineEdit_1)
        tmp_list.append(self.DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1)
        tmp_list.append(self.DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1)
        tmp_list.append(self.DE_Marines_Electronics_Info_device_description__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_location__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_person_name__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_datetime__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_person_agency__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_person_rank__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_submitter_name__lineEdit_1)
        # Gather추가
        tmp_list.append(self.DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_path__lineEdit_1)

        tmp_list.append(self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_acquisition_location__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_acquisition_tool__lineEdit_1)
        # Acquisition 추가
        tmp_list.append(self.DE_Acquisition_Info_file_browse__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_hash_value__lineEdit_1)
        # 기타파일 추가
        tmp_list.append(self.DE_other_files_file_browse__lineEdit_1)
        tmp_list.append(self.DE_other_files_id__lineEdit_1)
        tmp_list.append(self.DE_other_files_type__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_size__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_path__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_hash_type__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_hash_value__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_description__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_metadata__lineEdit_1)
        self.DE_AddAll_List.append(tmp_list)

        # DE Gather_Info
        tmp_list = list()
        tmp_list.append(self.DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_path__lineEdit_1)
        self.DE_Gather_Info_List[0].append(tmp_list)

        # 버튼
        # self.DE_Button_num = 1
        # self.DE_Button_List.append()
        tmp_list = list()
        tmp_list.append(self.DE_Gather_Info__addButton_1)
        tmp_list.append(self.DE_Gather_Info_file__filebrowse__browseButton_1)
        tmp_list.append(self.DE_Gather_Info_file__filebrowse__enterButton_1)
        tmp_list.append(self.DE_Acquisition_Info__addButton_1)
        tmp_list.append(self.DE_Acquisition_Info_file_browse__browseButton_1)
        tmp_list.append(self.DE_Acquisition_Info_file_browse__enterButton_1)
        self.DE_Button_List.append(tmp_list)

        # DE Acquisition +누르면 add
        tmp_list = list()
        tmp_list.append(self.DE_Acquisition_Info_file_browse__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_hash_value__lineEdit_1)
        self.DE_Acquisition_Info_List[0].append(tmp_list)

        # DE 기타파일 +누르면 add
        tmp_list = list()
        tmp_list.append(self.DE_other_files_file_browse__lineEdit_1)
        tmp_list.append(self.DE_other_files_id__lineEdit_1)
        tmp_list.append(self.DE_other_files_type__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_size__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_path__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_hash_type__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_hash_value__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_description__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_metadata__lineEdit_1)
        self.DE_Other_Files_Info_List[0].append(tmp_list)

        # self.AIReports_num = 1
        # self.AIReports_List = list()
        # AI other files + 누르면 add
        tmp_list = list()
        tmp_list.append(self.AI_Reports_id__lineEdit_1)
        tmp_list.append(self.AI_Reports_type__lineEdit_1)
        tmp_list.append(self.AI_Reports_subtype__lineEdit_1)
        tmp_list.append(self.AI_Reports_mgmt_id__lineEdit_1)
        tmp_list.append(self.AI_Reports_submission_agency__lineEdit_1)
        tmp_list.append(self.AI_Reports_reprot_creation_datetime__lineEdit_1)
        tmp_list.append(self.AI_Reports_division_name_of_report_maker__lineEdit_1)
        tmp_list.append(self.AI_Reports_team_name_of_report_maker__lineEdit_1)
        tmp_list.append(self.AI_Reports_file_info__lineEdit_1)
        tmp_list.append(self.AI_Reports_file_name__lineEdit_1)
        tmp_list.append(self.AI_Reports_file_size__lineEdit_1)
        tmp_list.append(self.AI_Reports_file_path__lineEdit_1)
        tmp_list.append(self.AI_Reports_file_creation_datetime__lineEdit_1)
        tmp_list.append(self.AI_Reports_file_description__lineEdit_1)
        tmp_list.append(self.AI_Reports_file_hash_type__lineEdit_1)
        tmp_list.append(self.AI_Reports_file_hash_value__lineEdit_1)
        self.AIReports_List.append(tmp_list)

        # self.AIReports_Button_num = 1
        # self.AIReports_Button_List = list()
        tmp_list = list()
        tmp_list.append(self.AI_Reports_file_info__browseButton_1)
        tmp_list.append(self.AI_Reports_file_info__enterButton_1)
        self.AIReports_Button_List.append(tmp_list)

        # AI other files +누르면  add
        tmp_list = list()
        tmp_list.append(self.AI_other_files_file_browse__lineEdit_1)
        tmp_list.append(self.AI_other_files_id__lineEdit_1)
        tmp_list.append(self.AI_other_files_type__lineEdit_1)
        tmp_list.append(self.AI_other_files_file_size__lineEdit_1)
        tmp_list.append(self.AI_other_files_file_path__lineEdit_1)
        tmp_list.append(self.AI_other_files_file_hash_type__lineEdit_1)
        tmp_list.append(self.AI_other_files_file_hash_value__lineEdit_1)
        tmp_list.append(self.AI_other_files_file_description__lineEdit_1)
        tmp_list.append(self.AI_other_files_file_metadata__lineEdit_1)
        self.AI_List.append(tmp_list)

        ##self.AI_other_files_Button_num = 1
        ##self.AI_other_files_Button_List = list()
        tmp_list = list()
        tmp_list.append(self.AI_other_files_file_browse__browseButton_1)
        tmp_list.append(self.AI_other_files_file_browse__enterButton_1)
        self.AI_other_files_Button_List.append(tmp_list)

        ##EquipmentTraces
        tmp_list = list()
        tmp_list.append(self.AI_EquipmentTraces_id__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_type__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_description__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_mgmt_id__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_vessel_id__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_evidence_id__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1)
        tmp_list.append(self.AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1)
        self.AI_EquipmentTraces_List.append(tmp_list)

        tmp_list = list()

        # 추가
        datetime.datetime.today()
        datetime.datetime.now()
        now = datetime.datetime.now()

        tmp_list.append(self.DEPL_digital_evidence_package_management_id__lineEdit_1)
        tmp_list.append(now)
        tmp_list.append(self.DEPL_log_type__lineEdit_1)
        tmp_list.append(self.DEPL_log_description__lineEdit_1)
        tmp_list.append(self.DEPL_devision_name_of_logger__lineEdit_1)
        tmp_list.append(self.DEPL_team_name_of_logger__lineEdit_1)
        tmp_list.append(self.DEPL_rank_of_logger__lineEdit_1)
        tmp_list.append(self.DEPL_name_of_logger__lineEdit_1)
        self.DEPL_List.append(tmp_list)

        # DE +AddAll하고 Gather에서 Browse
        tmp_list = list()
        tmp_list.append(self.DE_Gather_Info_file__filebrowse__lineEdit_1)
        self.DE_AddAll_Gather_Browse_List.append(tmp_list)

        # DE에서 +AddAll하고 Acquisition에서 Browse
        tmp_list = list()
        tmp_list.append(self.DE_Acquisition_Info_file_browse__lineEdit_1)
        self.DE_AddAll_Acquisition_Browse_List.append(tmp_list)

        ##DE에서 +AddAll하고 Other에서 Browse
        tmp_list = list()
        tmp_list.append(self.DE_other_files_file_browse__lineEdit_1)
        self.DE_AddAll_Other_Files_Browse_List.append(tmp_list)

        ##DE에서 +AddAll하고 Gather에서 Enter
        tmp_list = list()
        tmp_list.append(self.DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_path__lineEdit_1)
        self.DE_AddAll_Gather_Enter_List.append(tmp_list)

        ##DE에서 +AddAll하고 Acquisition에서 Enter
        tmp_list = list()
        tmp_list.append(self.DE_Acquisition_Info_file_browse__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_hash_value__lineEdit_1)
        self.DE_AddAll_Acquisition_Enter_List.append(tmp_list)

        ##DE에서 +AddAll하고 Other에서 Enter
        tmp_list = list()
        tmp_list.append(self.DE_other_files_file_browse__lineEdit_1)
        tmp_list.append(self.DE_other_files_id__lineEdit_1)
        tmp_list.append(self.DE_other_files_type__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_size__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_path__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_hash_type__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_hash_value__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_description__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_metadata__lineEdit_1)
        self.DE_AddAll_Other_Files_Enter_List.append(tmp_list)

        ##Export버튼 누르면 json파일로 변환
        self.ExportButton.clicked.connect(self.ExportButton_exporttojsonfile)

        # <Digital Evidence>

        # 145 DE에서 +누르면 전체가 밑에 추가됨
        self.DE__addButton.clicked.connect(lambda: self.DE__addButton_AddDE(len(self.DE_AddAll_List)))

        # 322 DE gather +버튼 클릭하면 add
        self.DE_Gather_Info__addButton_1.clicked.connect(lambda: self.DE_Gather_Info__addButton_1_AddGatherInfoFile(0))

        ##DE_Gather_Info Browse버튼 클릭하면 파일 업로드
        self.DE_Gather_Info_file__filebrowse__browseButton_1.clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog(0, 0))

        ##DE gather enter버튼 클릭하면 계산
        self.DE_Gather_Info_file__filebrowse__enterButton_1.clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__enterButton_1_Calculate(0, 0))

        # DE 수집정보 +버튼 클릭하면 add
        self.DE_Acquisition_Info__addButton_1.clicked.connect(lambda: self.DE_Acquisition_Info__addButton_1_AddDEAquisitionFile(0))

        # DE Acquisition Info Browse버튼 클릭하면 파일 업로드
        self.DE_Acquisition_Info_file_browse__browseButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info_file_browse__browseButton_1_QFileDialog(0, 0))

        ## DE Acquisition Info Enter버튼 누르면 파일 계산
        self.DE_Acquisition_Info_file_browse__enterButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info_file_browse__enterButton_1_Calculate(0, 0))

        # DE Other File에서 +버튼 클릭하면 Add
        self.DE_other_files__addButton_1.clicked.connect(lambda: self.DE_other_files__addButton_1_AddDEOtherFiles(0))

        ##DE Other File에서 Browse누르면 파일 클릭하면 파일 업로드
        self.DE_other_files_file_browse__browseButton_1.clicked.connect(
            lambda: self.DE_other_files_file_browse__browseButton_1_QFileDialog(0, 0))

        ##DE Other File에서 Enter누르면 파일 계산
        self.DE_other_files_file_browse__EnterButton_1.clicked.connect(
            lambda: self.DE_other_files_file_browse__EnterButton_1_Calculate(0, 0))

        # <Analysis Info>

        ## AI 보고 +버튼 클릭하면 Add보고
        self.AI_Reports__addButton.clicked.connect(self.AI_Reports__addButton_AddAIReports)

        ## AI Report browse버튼 클릭하면 파일 업로드
        self.AI_Reports_file_info__browseButton_1.clicked.connect(
            lambda: self.AI_Reports_file_info__browseButton_1_QFileDialog(0))

        ## AI Report Enter 클릭하면 파일 계산
        self.AI_Reports_file_info__enterButton_1.clicked.connect(
            lambda: self.AI_Reports_file_info__enterButton_1_Calculate(0))

        ## AI 장비흔적 사용자 추적정보 +버튼 클릭하면 EquipmentTraces Add
        self.AI_EquipmentTraces__addButton.clicked.connect(self.AI_EquipmentTraces__addButton_AddAIEquipmentTraces)

        ## AI 기타파일 +버튼 클릭하면 파일add
        self.AI_other_files__addButton.clicked.connect(self.AI_other_files__addButton_AddAIotherfile)

        ## AI other file browse버튼 클릭하면 파일 업로드
        self.AI_other_files_file_browse__browseButton_1.clicked.connect(
            lambda: self.AI_other_files_file_browse__browseButton_1_QFileDialog(0))

        ## AI OtherFile Enter 클릭하면 파일 계산
        self.AI_other_files_file_browse__enterButton_1.clicked.connect(
            lambda: self.AI_other_files_file_browse__enterButton_1_Calculate(0))

        # <DEPL>

        # 1036 DEPL +누르면 DEPL전체 add.
        self.DEPL__addButton.clicked.connect(self.DEPL__addButton_AddDEPL)




    def ExportButton_exporttojsonfile(self):
        print("ExportButton_exporttojsonfile")

        dict_json = {}
        dict_json['Digital Evidence Package'] = {}

        ### Case Information ###
        dict_CI = dict()
        dict_json['Digital Evidence Package']['Case Info'] = {"case_management_id": self.CI_List[0].text(),
                                                              "agency_case_no.": self.CI_List[1].text(),
                                                              "agency_organization_code": self.CI_List[2].text(),
                                                              "agency_organization_name": self.CI_List[3].text(),
                                                              "agency_organization_party_name": self.CI_List[
                                                                  4].text(),
                                                              "contents_of_request": self.CI_List[5].text(),
                                                              "case_summary": self.CI_List[6].text(),
                                                              "case_description": self.CI_List[7].text(),
                                                              "case_datetime": self.CI_List[8].text(),
                                                              "ordering_datetime": self.CI_List[9].text()}

        ### Digital Evidence ###
        dict_DE = dict()
        list_DE = []
        list_DE_Gather_Info = []
        for i, list in enumerate(self.DE_AddAll_List):
            tmp_dict = {}
            tmp_dict['management_id'] = list[0].text()
            tmp_dict['digital_evidence_type'] = list[1].text()
            tmp_dict['evidences_gathering_type'] = list[2].text()
            tmp_dict['Vessel Info'] = {'vessel_name': list[3].text(), 'vessel_management_id': list[4].text(),
                                       'vessel_MMSI': list[5].text(), 'vessel_callsign': list[6].text(),
                                       'vessel_IMO': list[7].text(), 'vessel_MRN': list[8].text(),
                                       'vessel_tonnage': list[9].text(), 'vessel_length': list[10].text(),
                                       'total_number_of_equipment_with_track': list[11].text()}
            tmp_dict['Marine Electronics Info'] = {'device_management_id': list[12].text(),
                                                   'device_type': list[13].text(),
                                                   'device_manufacturer': list[14].text(),
                                                   'device_model_name': list[15].text(),
                                                   'device_model_serial_number': list[16].text(),
                                                   'device_os_firmware': list[17].text(),
                                                   'device_description': list[18].text()}

            ##Gather Info 반복
            tmp_dict['Gather Info'] = {'gather_location': list[19].text(), 'gather_person_name': list[20].text(),
                                       'gather_datetime': list[21].text(),
                                       'gather_person_agency': list[22].text(),
                                       'gather_person_rank': list[23].text(), 'submitter_name': list[24].text()}
            tmp_list = []

            for gather_list in self.DE_Gather_Info_List[i]:
                tmp_list.append(
                    {'gather_media_type': gather_list[1].text(), 'gather_hash_type': gather_list[2].text(),
                     'gather_hash': gather_list[3].text(), 'gather_path': gather_list[4].text()})
            tmp_dict['Gather Info']['Gather Info Media File'] = tmp_list
            ##Gather Info 반복 끝

            ##Acquisition Info반복
            tmp_dict['Acquisition Info'] = {'aquisition_person_name': list[29].text(),
                                            'acquisition_datetime': list[30].text(),
                                            'acquisition_location': list[31].text(),
                                            'acquisition_tool': list[32].text()}
            tmp_list = []
            for acquisition_list in self.DE_Acquisition_Info_List[i]:
                tmp_list.append({'digital_evidence_file_name': acquisition_list[1].text(),
                                 'digital_evidence_file_path': acquisition_list[2].text(),
                                 'hash_type': acquisition_list[3].text(), 'hash_value': acquisition_list[4].text()})
            tmp_dict['Acquisition Info']['Acquisition Digital Info File'] = tmp_list
            ##Acquisition Info 반복 끝

            ##DE Other Info 시작
            list_DE_Other_Files = []
            for list in self.DE_Other_Files_Info_List:
                list_DE_Other_Files.append(
                    {'other_files_id': list[1].text(), 'other_files_type': list[2].text(),
                     'other_files_size': list[3].text(), 'other_files_path': list[4].text(),
                     'other_files_hash_type': list[5].text(), 'other_files_hash_value': list[6].text(),
                     'other_files_file_description': list[7].text(), 'other_files_file_metadata': list[8].text()})
            tmp_dict['Other Files']['Other Digital Info File'] = tmp_list
            ##DE Other Info 끝



        ### Analysis Information other files###
        dict_AI = dict()
        dict_json['Digital Evidence Package']["Analysis Info"] = dict()
        list_AIOtherFiles = []
        for list in self.AI_List:
            list_AIOtherFiles.append(
                {"id": list[1].text(), "type": list[2].text(), "file_size": list[3].text(),
                 "file_path": list[4].text(),
                 "file_hash_type": list[5].text(), "file_hash_value": list[6].text(),
                 "file_description": list[7].text(), "file_metadata": list[8].text()})
        dict_json['Digital Evidence Package']['Analysis Info']['Other Files'] = list_AIOtherFiles

        # AI Report###
        list_AIReports = []
        for list in self.AIReports_List:
            list_AIReports.append(
                {'id': list[0].text(), 'type': list[1].text(), 'subtype': list[2].text(),
                 'mgmt_id': list[3].text(), 'submission_agency': list[4].text(),
                 'report_creation_datetime': list[5].text(), 'division_name_of_report_maker': list[6].text(),
                 'team_name_of_report_maker': list[7].text(), 'file_name': list[9].text(),
                 'file_size': list[10].text(), 'file_path': list[11].text(),
                 'file_creation_datetime': list[12].text(),
                 'file_description': list[13].text(), 'hash_type': list[14].text(), 'hash_value': list[15].text()
                 })
        dict_json['Digital Evidence Package']['Analysis Info']['Reports'] = list_AIReports

        # AI Equipment Traces##
        list_AIEquipmentTraces = []
        for list in self.AI_EquipmentTraces_List:
            list_AIEquipmentTraces.append(
                {'id': list[0].text(), 'type': list[1].text(), 'description': list[2].text(),
                 'mgmt_id': list[3].text(), 'vessel_id': list[4].text(), 'evidence_id': list[5].text(),
                 'power_on_time': list[6].text(), 'track_extraction_description': list[7].text(),
                 'system_info_description': list[8].text(), 'operation_status': list[9].text(),
                 'power_off_time': list[10].text(), 'track_recording_period': list[11].text(),
                 'track_deletion_trace': list[12].text(), 'trace_notes': list[13].text()}
            )
        dict_json['Digital Evidence Package']['Analysis Info']['Equipment Traces'] = list_AIEquipmentTraces

        # DEPL
        list_DEPL = []
        for list in self.DEPL_List:
            list_DEPL.append(
                {'digital_evidence_package_management_id': list[0].text(),
                 'log_datetime': str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))),
                 'log_type': list[2].text(), 'log_description': list[3].text(),
                 'devision_name_of_logger': list[4].text(),
                 'team_name_of_logger': list[5].text(), 'rank_of_logger': list[6].text(),
                 'name_of_logger': list[7].text(),
                 }
            )
        dict_json['Digital Evidence Package Log'] = list_DEPL

        with open(self.file_path, "w", encoding='utf-8') as json_file:
            json_file.write(json.dumps(dict_json, ensure_ascii=False))

        self.MessageBox("증거팩 파일 생성이 완료되었습니다.")

        '''file_path = self.DE_Gather_Info_List[a][0].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\디지털 증거\\채증 정보\\" + file_name
        if os.path.isdir(".\\디지털 증거\\채증 정보") == False:
            os.makedirs(".\\디지털 증거\\채증 정보")
        copyfile(file_path, copy_file_path)
        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)
        self.DE_Gather_Info_List[a][1].setText(file_name[file_name.rfind(".") + 1:])
        self.DE_Gather_Info_List[a][2].setText("SHA-256")
        self.DE_Gather_Info_List[a][3].setText(sha256.hexdigest())
        self.DE_Gather_Info_List[a][4].setText(copy_file_path)'''

    def MessageBox(self, str):
        msg = QMessageBox()
        msg.setText(str)
        msg.setWindowTitle("완료")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    # DE전체 +버튼 누르면 전체 추가
    def DE__addButton_AddDE(self,a):
        self.DE_AddAll_num += 2

        tmp_DE_AddAll__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_AddAll__verticalLayout_1.setObjectName("DE_AddAll__verticalLayout_1")

        tmp = QtWidgets.QFrame(self.DE__scrollAreaWidgetContents)
        tmp.setFrameShape(QtWidgets.QFrame.HLine)
        tmp.setFrameShadow(QtWidgets.QFrame.Sunken)
        tmp_DE_AddAll__verticalLayout_1.addWidget(tmp)

        tmp_DE_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_management_id__horizontalLayout_1.setObjectName("DE_management_id__horizontalLayout_1")
        tmp_DE_management_id__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        tmp_DE_management_id__label_1.setObjectName("DE_management_id__label_1")
        tmp_DE_management_id__horizontalLayout_1.addWidget(tmp_DE_management_id__label_1)
        tmp_DE_management_id__lineEdit_1 = QtWidgets.QLineEdit(self.DE__scrollAreaWidgetContents)
        tmp_DE_management_id__lineEdit_1.setObjectName("DE_management_id__lineEdit_1")
        tmp_DE_management_id__horizontalLayout_1.addWidget(tmp_DE_management_id__lineEdit_1)
        tmp_DE_AddAll__verticalLayout_1.addLayout(tmp_DE_management_id__horizontalLayout_1)
        tmp_DE_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_digital_evidence_type__horizontalLayout_1.setObjectName("DE_digital_evidence_type__horizontalLayout_1")
        tmp_DE_digital_evidence_type__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        tmp_DE_digital_evidence_type__label_1.setObjectName("DE_digital_evidence_type__label_1")
        tmp_DE_digital_evidence_type__horizontalLayout_1.addWidget(tmp_DE_digital_evidence_type__label_1)
        tmp_DE_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE__scrollAreaWidgetContents)
        tmp_DE_digital_evidence_type__lineEdit_1.setObjectName("DE_digital_evidence_type__lineEdit_1")
        tmp_DE_digital_evidence_type__horizontalLayout_1.addWidget(tmp_DE_digital_evidence_type__lineEdit_1)
        tmp_DE_AddAll__verticalLayout_1.addLayout(tmp_DE_digital_evidence_type__horizontalLayout_1)
        tmp_DE_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_evidences_gathering_type__horizontalLayout_1.setObjectName("DE_evidences_gathering_type__horizontalLayout_1")
        tmp_DE_evidences_gathering_type__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        tmp_DE_evidences_gathering_type__label_1.setObjectName("DE_evidences_gathering_type__label_1")
        tmp_DE_evidences_gathering_type__horizontalLayout_1.addWidget(tmp_DE_evidences_gathering_type__label_1)
        tmp_DE_evidences_gathering_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE__scrollAreaWidgetContents)
        tmp_DE_evidences_gathering_type__lineEdit_1.setObjectName("DE_evidences_gathering_type__ineEdit_1")
        tmp_DE_evidences_gathering_type__horizontalLayout_1.addWidget(tmp_DE_evidences_gathering_type__lineEdit_1)
        tmp_DE_AddAll__verticalLayout_1.addLayout(tmp_DE_evidences_gathering_type__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1")
        tmp_DE_Vessel_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info__horizontalLayout_1.setObjectName("DE_Vessel_Info__horizontalLayout_1")
        tmp_DE_Vessel_Info__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        tmp_DE_Vessel_Info__label_1.setObjectName("DE_Vessel_Info__label_1")
        tmp_DE_Vessel_Info__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info__label_1)
        tmp_DE_Vessel_Info__blanklabel_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        tmp_DE_Vessel_Info__blanklabel_1.setText("")
        tmp_DE_Vessel_Info__blanklabel_1.setObjectName("DE_Vessel_Info__blanklabel_1")
        tmp_DE_Vessel_Info__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info__blanklabel_1)
        tmp_DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1.addLayout(tmp_DE_Vessel_Info__horizontalLayout_1)
        tmp_DE_Marine_Electronics_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marine_Electronics_Info__horizontalLayout_1.setObjectName("DE_Marine_Electronics_Info__horizontalLayout_1")
        tmp_DE_Marine_Electronics_Info__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        tmp_DE_Marine_Electronics_Info__label_1.setObjectName("DE_Marine_Electronics_Info__label_1")
        tmp_DE_Marine_Electronics_Info__horizontalLayout_1.addWidget(tmp_DE_Marine_Electronics_Info__label_1)
        tmp_label_5 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        tmp_label_5.setText("")
        tmp_label_5.setObjectName("label_5")
        tmp_DE_Marine_Electronics_Info__horizontalLayout_1.addWidget(tmp_label_5)
        tmp_DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1.addLayout(tmp_DE_Marine_Electronics_Info__horizontalLayout_1)
        tmp_DE_other_files__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files__horizontalLayout_1.setObjectName("DE_other_files__horizontalLayout_1")
        tmp_DE_other_files__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        tmp_DE_other_files__label_1.setObjectName("DE_other_files__label_1")
        tmp_DE_other_files__horizontalLayout_1.addWidget(tmp_DE_other_files__label_1)
        tmp_DE_other_files__addButton_1 = QtWidgets.QPushButton(self.DE__scrollAreaWidgetContents)
        tmp_DE_other_files__addButton_1.setObjectName("DE_other_files__addButton_1")
        tmp_DE_other_files__horizontalLayout_1.addWidget(tmp_DE_other_files__addButton_1)
        tmp_DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1.addLayout(tmp_DE_other_files__horizontalLayout_1)
        tmp_DE_AddAll__verticalLayout_1.addLayout(tmp_DE_Marines_Electronics_Info_Vessel_Info_Other_Files__horizontalLayout_1)
        tmp_DE_sub__scrollArea_1 = QtWidgets.QScrollArea(self.DE__scrollAreaWidgetContents)
        tmp_DE_sub__scrollArea_1.setWidgetResizable(True)
        tmp_DE_sub__scrollArea_1.setObjectName("DE_sub__scrollArea_1")
        tmp_DE_sub__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_sub__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 770, 254))
        tmp_DE_sub__scrollAreaWidgetContents_1.setObjectName("DE_sub__scrollAreaWidgetContents_1")
        tmp_gridLayout_5 = QtWidgets.QGridLayout(tmp_DE_sub__scrollAreaWidgetContents_1)
        tmp_gridLayout_5.setObjectName("gridLayout_5")
        tmp_DE_Gather_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info__horizontalLayout_1.setObjectName("DE_Gather_Info__horizontalLayout_1")
        tmp_DE_Gather_Info__label_1 = QtWidgets.QLabel(tmp_DE_sub__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__label_1.setObjectName("DE_Gather_Info__label_1")
        tmp_DE_Gather_Info__horizontalLayout_1.addWidget(tmp_DE_Gather_Info__label_1)
        tmp_gridLayout_5.addLayout(tmp_DE_Gather_Info__horizontalLayout_1, 3, 0, 1, 1)
        tmp_DE_Gather_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE_sub__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Gather_Info__scrollArea_1.setObjectName("DE_Gather_Info__scrollArea_1")
        tmp_DE_Gather_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Gather_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 251, 330))
        tmp_DE_Gather_Info__scrollAreaWidgetContents_1.setObjectName("DE_Gather_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_3 = QtWidgets.QGridLayout(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_3.setObjectName("gridLayout_3")
        tmp_DE_Gather_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Gather_Info__verticalLayout_1.setObjectName("DE_Gather_Info__verticalLayout_1")
        tmp_DE_Gather_Info_gather_location__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_location__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_location__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_location__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_location__label_1.setObjectName("DE_Gather_Info_gather_location__label_1")
        tmp_DE_Gather_Info_gather_location__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_location__label_1)
        tmp_DE_Gather_Info_gather_location__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_location__lineEdit_1.setObjectName("DE_Gather_Info_gather_location__lineEdit_1")
        tmp_DE_Gather_Info_gather_location__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_location__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_location__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_person_name__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_person_name__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_name__label_1.setObjectName("DE_Gather_Info_gather_person_name__label_1")
        tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_person_name__label_1)
        tmp_DE_Gather_Info_gather_person_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_name__lineEdit_1.setObjectName("DE_Gather_Info_gather_person_name__lineEdit_1")
        tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_person_name__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_datetime__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_datetime__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_datetime__label_1.setObjectName("DE_Gather_Info_gather_datetime__label_1")
        tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_datetime__label_1)
        tmp_DE_Gather_Info_gather_datetime__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_datetime__lineEdit_1.setObjectName("DE_Gather_Info_gather_datetime__lineEdit_1")
        tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_datetime__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_person_agency__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_person_agency__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_agency__label_1.setObjectName("DE_Gather_Info_gather_person_agency__label_1")
        tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_person_agency__label_1)
        tmp_DE_Gather_Info_gather_person_agency__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_agency__lineEdit_1.setObjectName("DE_Gather_Info_gather_person_agency__lineEdit_1")
        tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_person_agency__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_person_rank__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_person_rank__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_rank__label_1.setObjectName("DE_Gather_Info_gather_person_rank__label_1")
        tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_person_rank__label_1)
        tmp_DE_Gather_Info_gather_person_rank__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_rank__lineEdit_1.setObjectName("DE_Gather_Info_gather_person_rank__lineEdit_1")
        tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_person_rank__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1)
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1.setObjectName("DE_Gather_Info_submitter_name__horizontalLayout_1")
        tmp_DE_Gather_Info_submitter_name__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_submitter_name__label_1.setObjectName("DE_Gather_Info_submitter_name__label_1")
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_submitter_name__label_1)
        tmp_DE_Gather_Info_submitter_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_submitter_name__lineEdit_1.setObjectName("DE_Gather_Info_submitter_name__lineEdit_1")
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_submitter_name__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_submitter_name__horizontalLayout_1)
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1.setObjectName("DE_Gather_Info_file_addButton__horizontalLayout_1")
        tmp_DE_Gather_Info_file__blanklabel_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__blanklabel_1.setText("")
        tmp_DE_Gather_Info_file__blanklabel_1.setObjectName("DE_Gather_Info_file__blanklabel_1")
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__blanklabel_1)
        tmp_DE_Gather_Info__addButton_1 = QtWidgets.QPushButton(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__addButton_1.setObjectName("DE_Gather_Info__addButton_1")
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1.addWidget(tmp_DE_Gather_Info__addButton_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_file_addButton__horizontalLayout_1)
        tmp_DE_Gather_Info_file__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file__horizontalLayout_1.setObjectName("DE_Gather_Info_file__horizontalLayout_1")
        tmp_DE_Gather_Info_file__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Gather_Info_file__scrollArea_1.setObjectName("DE_Gather_Info_file__scrollArea_1")
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 344, 174))
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1.setObjectName("DE_Gather_Info_file__scrollAreaWidgetContents_1")
        tmp_gridLayout_18 = QtWidgets.QGridLayout(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_gridLayout_18.setObjectName("gridLayout_18")
        tmp_DE_Gather_Info_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Gather_Info_file__verticalLayout_1.setObjectName("DE_Gather_Info_file__verticalLayout_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.setObjectName("DE_Gather_Info_file__filebrowse__horizontalLayout_1")
        tmp_DE_Gather_Info_file__filebrowse__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__label_1.setObjectName("DE_Gather_Info_file__filebrowse__label_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__filebrowse__label_1)
        tmp_DE_Gather_Info_file__filebrowse__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__lineEdit_1.setObjectName("DE_Gather_Info_file__filebrowse__lineEdit_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1 = QtWidgets.QPushButton(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.setObjectName("DE_Gather_Info_file__filebrowse__browseButton_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__filebrowse__browseButton_1)
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1 = QtWidgets.QPushButton(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.setObjectName("DE_Gather_Info_file__filebrowse__enterButton_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__filebrowse__enterButton_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_media_type__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_media_type__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_media_type__label_1.setObjectName("DE_Gather_Info_gather_media_type__label_1")
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_media_type__label_1)
        tmp_DE_Gather_Info_gather_media_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_media_type__lineEdit_1.setObjectName("DE_Gather_Info_gather_media_type__lineEdit_1")
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_hash_type__horizontalLayout_1")
        tmp_DE_Gather_Info__gather_hash_type__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__gather_hash_type__label_1.setObjectName("DE_Gather_Info__gather_hash_type__label_1")
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(tmp_DE_Gather_Info__gather_hash_type__label_1)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1.setObjectName("DE_Gather_Info__gather_hash_type__lineEdit_1")
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_hash__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_hash__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_hash__label_1.setObjectName("DE_Gather_Info_gather_hash__label_1")
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_hash__label_1)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1.setObjectName("DE_Gather_Info_gather_hash__lineEdit_1")
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_hash__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_path__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_path__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_path__label_1.setObjectName("DE_Gather_Info_gather_path__label_1")
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_path__label_1)
        tmp_DE_Gather_Info_gather_path__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_path__lineEdit_1.setObjectName("DE_Gather_Info_gather_path__lineEdit_1")
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_path__horizontalLayout_1)
        tmp_gridLayout_18.addLayout(tmp_DE_Gather_Info_file__verticalLayout_1, 1, 0, 1, 1)
        tmp_DE_Gather_Info_file__scrollArea_1.setWidget(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__scrollArea_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_file__horizontalLayout_1)
        tmp_gridLayout_3.addLayout(tmp_DE_Gather_Info__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Gather_Info__scrollArea_1.setWidget(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_5.addWidget(tmp_DE_Gather_Info__scrollArea_1, 4, 0, 1, 1)
        tmp_DE_Acquisition_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE_sub__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Acquisition_Info__scrollArea_1.setObjectName("DE_Acquisition_Info__scrollArea_1")
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 249, 268))
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1.setObjectName("DE_Acquisition_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_4 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_4.setObjectName("gridLayout_4")
        tmp_DE_Acquisition_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__verticalLayout_1.setObjectName("DE_Acquisition_Info__verticalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.setObjectName("DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1.setObjectName("DE_Acquisition_Info_acquisition_person_name__label_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_person_name__label_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_person_name__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.setObjectName("DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1.setObjectName("DE_Acquisition_Info_acquisition_date_time__label_1")
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_date_time__label_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_date_time__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1)
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.setObjectName("DE_Acquisiton_Info_acquisition_location__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_location__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_location__label_1.setObjectName("DE_Acquisition_Info_acquisition_location__label_1")
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_location__label_1)
        tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_location__lineEdit_1")
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1)
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.setObjectName("DE_Acquisition_Info_acquisition_tool__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_tool__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool__label_1.setObjectName("DE_Acquisition_Info_acquisition_tool__label_1")
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_tool__label_1)
        tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_tool__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1)
        tmp_DE_Acquisition_Info_addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_addButton__horizontalLayout_1.setObjectName("DE_Acquisition_Info_addButton__horizontalLayout_1")
        tmp_DE_Acquisition_Info__blanklabel_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info__blanklabel_1.setText("")
        tmp_DE_Acquisition_Info__blanklabel_1.setObjectName("DE_Acquisition_Info__blanklabel_1")
        tmp_DE_Acquisition_Info_addButton__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info__blanklabel_1)
        tmp_DE_Acquisition_Info__addButton_1 = QtWidgets.QPushButton(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info__addButton_1.setObjectName("DE_Acquisition_Info__addButton_1")
        tmp_DE_Acquisition_Info_addButton__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info__addButton_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_addButton__horizontalLayout_1)
        tmp_DE_Acquisition_Info_file__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setObjectName("DE_Acquisition_Info_file__scrollArea_1")
        tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 344, 174))
        tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1.setObjectName("DE_Aquisition_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_15 = QtWidgets.QGridLayout(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_15.setObjectName("gridLayout_15")
        tmp_DE_Aquisition_Info_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Aquisition_Info_file__verticalLayout_1.setObjectName("DE_Aquisition_Info_file__verticalLayout_1")
        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.setObjectName("DE_Aquisition_Info_file_browse_horizontalLayout_1")
        tmp_DE_Acquisition_Info_file_browse__label_1 = QtWidgets.QLabel(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_file_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        tmp_DE_Acquisition_Info_file_browse__label_1.setObjectName("DE_Acquisition_Info_file_browse__label_1")
        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_file_browse__label_1)
        tmp_DE_Acquisition_Info_file_browse__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_file_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_file_browse__lineEdit_1")
        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_file_browse__lineEdit_1)
        tmp_DE_Acquisition_Info_file_browse__browseButton_1 = QtWidgets.QPushButton(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_file_browse__browseButton_1.setObjectName("DE_Acquisition_Info_file_browse__browseButton_1")
        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_file_browse__browseButton_1)
        tmp_DE_Acquisition_Info_file_browse__enterButton_1 = QtWidgets.QPushButton(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_file_browse__enterButton_1.setObjectName("DE_Acquisition_Info_file_browse__enterButton_1")
        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_file_browse__enterButton_1)
        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1)
        tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1.setObjectName("DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_digital_evidence_file_name__label_1 = QtWidgets.QLabel(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_name__label_1.setObjectName( "DE_Acquisition_Info_digital_evidence_file_name__label_1")
        tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_digital_evidence_file_name__label_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1.setObjectName("DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1")
        tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1)
        tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1.setObjectName("DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1")
        tmp_DE_Acquisition_Info_digital_evidence_file_path__label_1 = QtWidgets.QLabel(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_path__label_1.setObjectName("DE_Acquisition_Info_digital_evidence_file_path__label_1")
        tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_digital_evidence_file_path__label_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1.setObjectName("DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1")
        tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1)
        tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_hash_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_hash_type__label_1 = QtWidgets.QLabel(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_hash_type__label_1.setObjectName("DE_Acquisition_Info_hash_type__label_1")
        tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_hash_type__label_1)
        tmp_DE_Acquisition_Info_hash_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_hash_type__lineEdit_1.setObjectName("DE_Acquisition_Info_hash_type__lineEdit_1")
        tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_hash_type__lineEdit_1)
        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1.setObjectName("DE_Acquisition_Info_hash_value__horizontalLayout_1")
        tmp_DE_Acquisition_Info_hash_value__label_1 = QtWidgets.QLabel(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_hash_value__label_1.setObjectName("DE_Acquisition_Info_hash_value__label_1")
        tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_hash_value__label_1)
        tmp_DE_Acquisition_Info_hash_value__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_hash_value__lineEdit_1.setObjectName("DE_Acquisition_Info_hash_value__lineEdit_1")
        tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_hash_value__lineEdit_1)
        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1)
        tmp_gridLayout_15.addLayout(tmp_DE_Aquisition_Info_file__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidget(tmp_DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addWidget(tmp_DE_Acquisition_Info_file__scrollArea_1)
        tmp_gridLayout_4.addLayout(tmp_DE_Acquisition_Info__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Acquisition_Info__scrollArea_1.setWidget(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_5.addWidget(tmp_DE_Acquisition_Info__scrollArea_1, 4, 1, 1, 1)
        tmp_DE_Vessel_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE_sub__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Vessel_Info__scrollArea_1.setObjectName("DE_Vessel_Info__scrollArea_1")
        tmp_DE_Vessel_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Vessel_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 251, 287))
        tmp_DE_Vessel_Info__scrollAreaWidgetContents_1.setObjectName("DE_Vessel_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_20 = QtWidgets.QGridLayout(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_20.setObjectName("gridLayout_20")
        tmp_DE_Vessel_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Vessel_Info__verticalLayout_1.setObjectName("DE_Vessel_Info__verticalLayout_1")
        tmp_DE_Veseel_Info_vessel_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Veseel_Info_vessel_name__horizontalLayout_1.setObjectName("DE_Veseel_Info_vessel_name__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_name__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_name__label_1.setObjectName("DE_Vessel_Info_vessel_name__label_1")
        tmp_DE_Veseel_Info_vessel_name__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_name__label_1)
        tmp_DE_Vessel_Info_vessel_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_name__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_name__lineEdit_1")
        tmp_DE_Veseel_Info_vessel_name__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_name__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Veseel_Info_vessel_name__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_management_id__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_management_id__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_management_id__label_1.setObjectName("DE_Vessel_Info_vessel_management_id__label_1")
        tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_management_id__label_1)
        tmp_DE_Vessel_Info_vessel_management_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_management_id__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_management_id__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_management_id__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_MMSI__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_MMSI__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_MMSI__label_1.setObjectName("DE_Vessel_Info_vessel_MMSI__label_1")
        tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_MMSI__label_1)
        tmp_DE_Vessel_Info_vessel_MMSI__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_MMSI__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_MMSI__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_MMSI__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_callsign__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_callsign__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_callsign__label_1.setObjectName("DE_Vessel_Info_vessel_callsign__label_1")
        tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_callsign__label_1)
        tmp_DE_Vessel_Info_vessel_callsign__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_callsign__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_callsign__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_callsign__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_IMO__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_IMO__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_IMO__label_1.setObjectName("DE_Vessel_Info_vessel_IMO__label_1")
        tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_IMO__label_1)
        tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_IMO__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_MRN__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_MRN__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_MRN__label_1.setObjectName("DE_Vessel_Info_vessel_MRN__label_1")
        tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_MRN__label_1)
        tmp_DE_Vessel_Info_vessel_MRN__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_MRN__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_MRN__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_MRN__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_tonnage__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_tonnage__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_tonnage__label_1.setObjectName("DE_Vessel_Info_vessel_tonnage__label_1")
        tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_tonnage__label_1)
        tmp_DE_Vessel_Info_vessel_tonnage__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_tonnage__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_tonnage__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_tonnage__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_length__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_length__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_length__label_1.setObjectName("DE_Vessel_Info_vessel_length__label_1")
        tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_length__label_1)
        tmp_DE_Vessel_Info_vessel_length__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_length__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_length__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_length__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.setObjectName("DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1.setObjectName("DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1")
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1)
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1)
        tmp_gridLayout_20.addLayout(tmp_DE_Vessel_Info__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Vessel_Info__scrollArea_1.setWidget(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_5.addWidget(tmp_DE_Vessel_Info__scrollArea_1, 2, 0, 1, 1)
        tmp_DE_Acquisition_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info__horizontalLayout_1.setObjectName("DE_Acquisition_Info__horizontalLayout_1")
        tmp_DE_Acquisition_Info__label_1 = QtWidgets.QLabel(tmp_DE_sub__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info__label_1.setObjectName("DE_Acquisition_Info__label_1")
        tmp_DE_Acquisition_Info__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info__label_1)
        tmp_gridLayout_5.addLayout(tmp_DE_Acquisition_Info__horizontalLayout_1, 3, 1, 1, 1)
        tmp_DE_Marines_Electronics_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE_sub__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Marines_Electronics_Info__scrollArea_1.setObjectName("DE_Marines_Electronics_Info__scrollArea_1")
        tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 249, 227))
        tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1.setObjectName("DE_Marines_Electronics_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_6 = QtWidgets.QGridLayout(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_6.setObjectName("gridLayout_6")
        tmp_DE_Marines_Electronics_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.setObjectName("DE_Marines_Electronics_Info__verticalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_management_id__label_1 = QtWidgets.QLabel(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_management_id__label_1.setObjectName("DE_Marines_Electronics_Info_device_management_id__label_1")
        tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_management_id__label_1)
        tmp_DE_Marines_Electronics_Info_device_management_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_management_id__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_management_id__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_management_id__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_type__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_type__label_1 = QtWidgets.QLabel(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_type__label_1.setObjectName("DE_Marines_Electronics_Info_device_type__label_1")
        tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_type__label_1)
        tmp_DE_Marines_Electronics_Info_device_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_type__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_type__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_type__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_manufacturer__label_1 = QtWidgets.QLabel(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_manufacturer__label_1.setObjectName("DE_Marines_Electronics_Info_device_manufacturer__label_1")
        tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_manufacturer__label_1)
        tmp_DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_model_name__label_1 = QtWidgets.QLabel(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_model_name__label_1.setObjectName("DE_Marines_Electronics_Info_device_model_name__label_1")
        tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_model_name__label_1)
        tmp_DE_Marines_Electronics_Info_device_model_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_model_name__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_model_name__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_model_name__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__label_1 = QtWidgets.QLabel(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__label_1.setObjectName("DE_Marines_Electronics_Info_device_model_serial_number__label_1")
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_model_serial_number__label_1)
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.setObjectName(    "DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_os_firmware__label_1 = QtWidgets.QLabel(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_os_firmware__label_1.setObjectName("DE_Marines_Electronics_Info_device_os_firmware__label_1")
        tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_os_firmware__label_1)
        tmp_DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_description__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_description__label_1 = QtWidgets.QLabel(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_description__label_1.setObjectName("DE_Marines_Electronics_Info_device_description__label_1")
        tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_description__label_1)
        tmp_DE_Marines_Electronics_Info_device_description__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_description__lineEdit_1.setObjectName("DE_Marines_Electronics_Info_device_description__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1.addWidget(tmp_DE_Marines_Electronics_Info_device_description__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1)
        tmp_gridLayout_6.addLayout(tmp_DE_Marines_Electronics_Info__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Marines_Electronics_Info__scrollArea_1.setWidget(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_5.addWidget(tmp_DE_Marines_Electronics_Info__scrollArea_1, 2, 1, 1, 1)
        tmp_DE_other_files__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE_sub__scrollAreaWidgetContents_1)
        tmp_DE_other_files__scrollArea_1.setWidgetResizable(True)
        tmp_DE_other_files__scrollArea_1.setObjectName("DE_other_files__scrollArea_1")
        tmp_DE_other_files__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_other_files__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 349, 294))
        tmp_DE_other_files__scrollAreaWidgetContents_1.setObjectName("DE_other_files__scrollAreaWidgetContents_1")
        tmp_gridLayout_13 = QtWidgets.QGridLayout(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_gridLayout_13.setObjectName("gridLayout_13")

        tmp_DE_other_files__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_other_files__verticalLayout_1.setObjectName("DE_other_files__verticalLayout_1")
        tmp_DE_other_files_file_browse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_browse__horizontalLayout_1.setObjectName("DE_other_files_file_browse__horizontalLayout_1")
        tmp_DE_other_files_file_browse__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__label_1.setObjectName("DE_other_files_file_browse__label_1")
        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__label_1)
        tmp_DE_other_files_file_browse__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__lineEdit_1.setObjectName("DE_other_files_file_browse__lineEdit_1")
        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__lineEdit_1)
        tmp_DE_other_files_file_browse__browseButton_1 = QtWidgets.QPushButton(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__browseButton_1.setObjectName("DE_other_files_file_browse__browseButton_1")
        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__browseButton_1)
        tmp_DE_other_files_file_browse__EnterButton_1 = QtWidgets.QPushButton(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__EnterButton_1.setObjectName("DE_other_files_file_browse__EnterButton_1")
        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__EnterButton_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_browse__horizontalLayout_1)
        tmp_DE_other_files_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_id__horizontalLayout_1.setObjectName("DE_other_files_id__horizontalLayout_1")
        tmp_DE_other_files_id__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_id__label_1.setObjectName("DE_other_files_id__label_1")
        tmp_DE_other_files_id__horizontalLayout_1.addWidget(tmp_DE_other_files_id__label_1)
        tmp_DE_other_files_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_id__lineEdit_1.setObjectName("DE_other_files_id__lineEdit_1")
        tmp_DE_other_files_id__horizontalLayout_1.addWidget(tmp_DE_other_files_id__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_id__horizontalLayout_1)
        tmp_DE_other_files_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_type__horizontalLayout_1.setObjectName("DE_other_files_type__horizontalLayout_1")
        tmp_DE_other_files_type__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_type__label_1.setObjectName("DE_other_files_type__label_1")
        tmp_DE_other_files_type__horizontalLayout_1.addWidget(tmp_DE_other_files_type__label_1)
        tmp_DE_other_files_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_type__lineEdit_1.setObjectName("DE_other_files_type__lineEdit_1")
        tmp_DE_other_files_type__horizontalLayout_1.addWidget(tmp_DE_other_files_type__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_type__horizontalLayout_1)
        tmp_DE_other_files_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_size__horizontalLayout_1.setObjectName("DE_other_files_file_size__horizontalLayout_1")
        tmp_DE_other_files_file_size__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_size__label_1.setObjectName("DE_other_files_file_size__label_1")
        tmp_DE_other_files_file_size__horizontalLayout_1.addWidget(tmp_DE_other_files_file_size__label_1)
        tmp_DE_other_files_file_size__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_size__lineEdit_1.setObjectName("DE_other_files_file_size__lineEdit_1")
        tmp_DE_other_files_file_size__horizontalLayout_1.addWidget(tmp_DE_other_files_file_size__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_size__horizontalLayout_1)
        tmp_DE_other_files_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_path__horizontalLayout_1.setObjectName("DE_other_files_file_path__horizontalLayout_1")
        tmp_DE_other_files_file_path__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_path__label_1.setObjectName("DE_other_files_file_path__label_1")
        tmp_DE_other_files_file_path__horizontalLayout_1.addWidget(tmp_DE_other_files_file_path__label_1)
        tmp_DE_other_files_file_path__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_path__lineEdit_1.setObjectName("DE_other_files_file_path__lineEdit_1")
        tmp_DE_other_files_file_path__horizontalLayout_1.addWidget(tmp_DE_other_files_file_path__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_path__horizontalLayout_1)
        tmp_DE_other_files_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_hash_type__horizontalLayout_1.setObjectName("DE_other_files_file_hash_type__horizontalLayout_1")
        tmp_DE_other_files_file_hash_type__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_type__label_1.setObjectName("DE_other_files_file_hash_type__label_1")
        tmp_DE_other_files_file_hash_type__horizontalLayout_1.addWidget(tmp_DE_other_files_file_hash_type__label_1)
        tmp_DE_other_files_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_type__lineEdit_1.setObjectName("DE_other_files_file_hash_type__lineEdit_1")
        tmp_DE_other_files_file_hash_type__horizontalLayout_1.addWidget(tmp_DE_other_files_file_hash_type__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_hash_type__horizontalLayout_1)
        tmp_DE_other_files_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_hash_value__horizontalLayout_1.setObjectName("DE_other_files_file_hash_value__horizontalLayout_1")
        tmp_DE_other_files_file_hash_value__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_value__label_1.setObjectName("DE_other_files_file_hash_value__label_1")
        tmp_DE_other_files_file_hash_value__horizontalLayout_1.addWidget(tmp_DE_other_files_file_hash_value__label_1)
        tmp_DE_other_files_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_value__lineEdit_1.setObjectName("DE_other_files_file_hash_value__lineEdit_1")
        tmp_DE_other_files_file_hash_value__horizontalLayout_1.addWidget(tmp_DE_other_files_file_hash_value__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_hash_value__horizontalLayout_1)
        tmp_DE_other_files_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_description__horizontalLayout_1.setObjectName("DE_other_files_file_description__horizontalLayout_1")
        tmp_DE_other_files_file_description__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_description__label_1.setObjectName("DE_other_files_file_description__label_1")
        tmp_DE_other_files_file_description__horizontalLayout_1.addWidget(tmp_DE_other_files_file_description__label_1)
        tmp_DE_other_files_file_description__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_description__lineEdit_1.setObjectName("DE_other_files_file_description__lineEdit_1")
        tmp_DE_other_files_file_description__horizontalLayout_1.addWidget(tmp_DE_other_files_file_description__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_description__horizontalLayout_1)
        tmp_DE_other_files_file_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_metadata__horizontalLayout_1.setObjectName("DE_other_files_file_metadata__horizontalLayout_1")
        tmp_DE_other_files_file_metadata__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_metadata__label_1.setObjectName("DE_other_files_file_metadata__label_1")
        tmp_DE_other_files_file_metadata__horizontalLayout_1.addWidget(tmp_DE_other_files_file_metadata__label_1)
        tmp_DE_other_files_file_metadata__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_metadata__lineEdit_1.setObjectName("DE_other_files_file_metadata__lineEdit_1")
        tmp_DE_other_files_file_metadata__horizontalLayout_1.addWidget(tmp_DE_other_files_file_metadata__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_metadata__horizontalLayout_1)
        tmp_gridLayout_13.addLayout(tmp_DE_other_files__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_other_files__scrollArea_1.setWidget(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_gridLayout_5.addWidget(tmp_DE_other_files__scrollArea_1, 2, 2, 3, 1)
        tmp_DE_sub__scrollArea_1.setWidget(tmp_DE_sub__scrollAreaWidgetContents_1)

        tmp_DE_AddAll__verticalLayout_1.addWidget(tmp_DE_sub__scrollArea_1)
        self.gridLayout_7.addLayout(tmp_DE_AddAll__verticalLayout_1, self.DE_AddAll_num, 0, 1, 1)

        self.DE_Gather_Info_File_List.append(tmp_gridLayout_18)  # 이거를 저장
        self.DE_Acquisition_Info_File_List.append(tmp_gridLayout_15)  # 이거를 저장
        self.DE_Other_Files_File_List.append(tmp_gridLayout_13) # 이거를 저장
        tmp_list = list()
        tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        self.DE_Gather_Info_List.append(list())
        self.DE_Gather_Info_List[a].append(tmp_list)
        tmp_list = list()
        tmp_list.append(tmp_DE_Acquisition_Info_file_browse__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_hash_value__lineEdit_1)
        self.DE_Acquisition_Info_List.append(list())
        self.DE_Acquisition_Info_List[a].append(tmp_list)
        tmp_list = list()
        tmp_list.append(tmp_DE_other_files_file_browse__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_id__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_type__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_size__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_hash_value__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_description__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_metadata__lineEdit_1)
        self.DE_Other_Files_Info_List.append(list())
        self.DE_Other_Files_Info_List[a].append(tmp_list)


        tmp_DE_management_id__label_1.setText("관리 번호: ")
        tmp_DE_digital_evidence_type__label_1.setText("디지털 증거 유형: ")
        tmp_DE_evidences_gathering_type__label_1.setText("증거 채증 유형: ")
        tmp_DE_Vessel_Info__label_1.setText("선박 정보: ")
        tmp_DE_Marine_Electronics_Info__label_1.setText("해양 장비 정보: ")
        tmp_DE_other_files__label_1.setText("기타 파일(jpg, mp3, mp4, txt, avi 등")
        tmp_DE_other_files__addButton_1.setText("+")
        tmp_DE_Marines_Electronics_Info_device_management_id__label_1.setText("장비 관리 고유 번호: ")
        tmp_DE_Marines_Electronics_Info_device_type__label_1.setText("장비 유형: ")
        tmp_DE_Marines_Electronics_Info_device_manufacturer__label_1.setText("장비 제조사: ")
        tmp_DE_Marines_Electronics_Info_device_model_name__label_1.setText("장비 모델명: ")
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__label_1.setText("장비 모델 시리얼 넘버: ")
        tmp_DE_Marines_Electronics_Info_device_os_firmware__label_1.setText("장비 os firmware: ")
        tmp_DE_Marines_Electronics_Info_device_description__label_1.setText("장비 설명: ")
        tmp_DE_Gather_Info__label_1.setText("채증 정보: ")
        tmp_DE_Gather_Info_gather_location__label_1.setText("채증 장소: ")
        tmp_DE_Gather_Info_gather_person_name__label_1.setText("채증 담당자: ")
        tmp_DE_Gather_Info_gather_datetime__label_1.setText("채증 시간: ")
        tmp_DE_Gather_Info_gather_person_agency__label_1.setText("채증 기관: ")
        tmp_DE_Gather_Info_gather_person_rank__label_1.setText("채증 담당자 계급: ")
        tmp_DE_Gather_Info_submitter_name__label_1.setText("피압수자: ")
        tmp_DE_Gather_Info__addButton_1.setText("+")
        tmp_DE_Gather_Info_file__filebrowse__label_1.setText("파일 입력: ")
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.setText("Browse...")
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.setText("Enter")
        tmp_DE_Gather_Info_gather_media_type__label_1.setText("채증 미디어 유형: ")
        tmp_DE_Gather_Info__gather_hash_type__label_1.setText("채증 해시 종류: ")
        tmp_DE_Gather_Info_gather_hash__label_1.setText("채증 미디어 해시값: ")
        tmp_DE_Gather_Info_gather_path__label_1.setText("채증 미디어 경로: ")
        tmp_DE_Acquisition_Info__label_1.setText("수집 정보")
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1.setText("수집자명: ")
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1.setText("수집 시간: ")
        tmp_DE_Acquisition_Info_acquisition_location__label_1.setText("수집 장소: ")
        tmp_DE_Acquisition_Info_acquisition_tool__label_1.setText("수집 도구: ")
        tmp_DE_Acquisition_Info__addButton_1.setText("+")
        tmp_DE_Acquisition_Info_file_browse__label_1.setText("파일입력: ")
        tmp_DE_Acquisition_Info_file_browse__browseButton_1.setText("Browse...")
        tmp_DE_Acquisition_Info_file_browse__enterButton_1.setText("Enter")
        tmp_DE_Acquisition_Info_digital_evidence_file_name__label_1.setText("디지털 증거 파일 이름: ")
        tmp_DE_Acquisition_Info_digital_evidence_file_path__label_1.setText("디지털 증거 파일 경로: ")
        tmp_DE_Acquisition_Info_hash_type__label_1.setText("해시 종류: ")
        tmp_DE_Acquisition_Info_hash_value__label_1.setText("해시값: ")
        tmp_DE_Vessel_Info_vessel_name__label_1.setText("선박 이름: ")
        tmp_DE_Vessel_Info_vessel_management_id__label_1.setText("선박 관리 고유 번호: ")
        tmp_DE_Vessel_Info_vessel_MMSI__label_1.setText("선박 MMSI: ")
        tmp_DE_Vessel_Info_vessel_callsign__label_1.setText("선박 callsign: ")
        tmp_DE_Vessel_Info_vessel_IMO__label_1.setText("선박 IMO: ")
        tmp_DE_Vessel_Info_vessel_MRN__label_1.setText("선박 MRN: ")
        tmp_DE_Vessel_Info_vessel_tonnage__label_1.setText("선박 톤수: ")
        tmp_DE_Vessel_Info_vessel_length__label_1.setText("선박 길이: ")
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1.setText("항적 분석 장비 수: ")
        tmp_DE_other_files_file_browse__label_1.setText("파일 입력: ")
        tmp_DE_other_files_file_browse__browseButton_1.setText("Browse...")
        tmp_DE_other_files_file_browse__EnterButton_1.setText("Enter")
        tmp_DE_other_files_id__label_1.setText("고유번호: ")
        tmp_DE_other_files_type__label_1.setText("파일 유형: ")
        tmp_DE_other_files_file_size__label_1.setText("파일 크기: ")
        tmp_DE_other_files_file_path__label_1.setText("파일 경로: ")
        tmp_DE_other_files_file_hash_type__label_1.setText("해시 종류: ")
        tmp_DE_other_files_file_hash_value__label_1.setText("해시값: ")
        tmp_DE_other_files_file_description__label_1.setText("파일 설명: ")
        tmp_DE_other_files_file_metadata__label_1.setText("파일 메타데이터: ")

        a = len(self.DE_AddAll_List)
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog2(a))

        a = len(self.DE_AddAll_List)
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__enterButton_1_Calculate2(a))

        a = len(self.DE_AddAll_List)
        tmp_DE_Gather_Info__addButton_1.clicked.connect(
            lambda: self.DE_Gather_Info__addButton_1_AddGatherInfoFile(a))

        ##
        a = len(self.DE_AddAll_List)
        tmp_DE_Acquisition_Info_file_browse__browseButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info_file_browse__browseButton_1_QFileDialog2(a))

        a = len(self.DE_AddAll_List)
        tmp_DE_Acquisition_Info_file_browse__enterButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info_file_browse__enterButton_1_Calculate2(a))

        a = len(self.DE_AddAll_List)
        tmp_DE_Acquisition_Info__addButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info__addButton_1_AddDEAquisitionFile(a))


        ##
        a = len(self.DE_AddAll_List)
        tmp_DE_other_files_file_browse__browseButton_1.clicked.connect(
            lambda: self.DE_other_files_file_browse__browseButton_1_QFileDialog2(a))

        a = len(self.DE_AddAll_List)
        tmp_DE_other_files_file_browse__EnterButton_1.clicked.connect(
            lambda: self.DE_other_files_file_browse__EnterButton_1_Calculate2(a))

        a = len(self.DE_AddAll_List)
        tmp_DE_other_files__addButton_1.clicked.connect(
            lambda: self.DE_other_files__addButton_1_AddDEOtherFiles(a))


        tmp_list = list()
        tmp_list.append(tmp_DE_management_id__lineEdit_1)
        tmp_list.append(tmp_DE_digital_evidence_type__lineEdit_1)
        tmp_list.append(tmp_DE_evidences_gathering_type__lineEdit_1)

        tmp_list.append(tmp_DE_Vessel_Info_vessel_name__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_management_id__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_MMSI__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_callsign__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_MRN__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_tonnage__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_length__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1)

        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_management_id__lineEdit_1)
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_type__lineEdit_1)
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1)
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_model_name__lineEdit_1)
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1)
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1)
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_description__lineEdit_1)

        tmp_list.append(tmp_DE_Gather_Info_gather_location__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_person_name__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_datetime__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_person_agency__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_person_rank__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_submitter_name__lineEdit_1)
        # Gather +
        tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_path__lineEdit_1)

        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1)
        # Acquisition +
        tmp_list.append(tmp_DE_Acquisition_Info_file_browse__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_hash_value__lineEdit_1)
        # Other Files +
        tmp_list.append(tmp_DE_other_files_file_browse__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_id__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_type__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_size__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_hash_value__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_description__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_metadata__lineEdit_1)
        self.DE_AddAll_List.append(tmp_list)

        # 버튼
        # self.DE_Button_num = 1
        # self.DE_Button_List = list()
        tmp_list = list()
        tmp_list.append(tmp_DE_Gather_Info__addButton_1)
        tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__browseButton_1)
        tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__enterButton_1)
        tmp_list.append(tmp_DE_Acquisition_Info__addButton_1)
        tmp_list.append(tmp_DE_Acquisition_Info_file_browse__browseButton_1)
        tmp_list.append(tmp_DE_Acquisition_Info_file_browse__enterButton_1)
        tmp_list.append(tmp_DE_other_files__addButton_1)
        tmp_list.append(tmp_DE_other_files_file_browse__browseButton_1)
        tmp_list.append(tmp_DE_other_files_file_browse__EnterButton_1)
        self.DE_Button_List.append(tmp_list)

        # DE +AddAll 하고 Browse
        tmp_list = list()
        tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        self.DE_AddAll_Gather_Browse_List.append(tmp_list)

        tmp_list = list()
        tmp_list.append(tmp_DE_Acquisition_Info_file_browse__lineEdit_1)
        self.DE_AddAll_Acquisition_Browse_List.append(tmp_list)

        tmp_list = list()
        tmp_list.append(tmp_DE_other_files_file_browse__lineEdit_1)
        self.DE_AddAll_Other_Files_Browse_List.append(tmp_list)

        # DE +AddAll 하고 Enter
        tmp_list = list()
        tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        self.DE_AddAll_Gather_Enter_List.append(tmp_list)

        tmp_list = list()
        tmp_list.append(tmp_DE_Acquisition_Info_file_browse__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_hash_value__lineEdit_1)
        self.DE_AddAll_Acquisition_Enter_List.append(tmp_list)

        tmp_list = list()
        tmp_list.append(tmp_DE_other_files_file_browse__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_id__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_type__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_size__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_hash_value__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_description__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_metadata__lineEdit_1)
        self.DE_AddAll_Other_Files_Enter_List.append(tmp_list)

        tmp_DE_Gather_Info_gather_media_type__lineEdit_1.setReadOnly(True)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1.setReadOnly(True)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1.setReadOnly(True)
        tmp_DE_Gather_Info_gather_path__lineEdit_1.setReadOnly(True)

        tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1.setReadOnly(True)
        tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1.setReadOnly(True)
        tmp_DE_Acquisition_Info_hash_type__lineEdit_1.setReadOnly(True)
        tmp_DE_Acquisition_Info_hash_value__lineEdit_1.setReadOnly(True)

        tmp_DE_other_files_id__lineEdit_1.setReadOnly(True)
        tmp_DE_other_files_type__lineEdit_1.setReadOnly(True)
        tmp_DE_other_files_file_size__lineEdit_1.setReadOnly(True)
        tmp_DE_other_files_file_path__lineEdit_1.setReadOnly(True)
        tmp_DE_other_files_file_hash_type__lineEdit_1.setReadOnly(True)
        tmp_DE_other_files_file_hash_value__lineEdit_1.setReadOnly(True)

    # DE 전체 +버튼 누르고 gather browse
    def DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog2(self, a):
        file_name = QFileDialog.getOpenFileName()
        self.DE_AddAll_Gather_Browse_List[a][0].setText(file_name[0])

    # DE  전체 +버튼 누르고 gather Enter
    def DE_Gather_Info_file__filebrowse__enterButton_1_Calculate2(self, a):
        file_path = self.DE_AddAll_Gather_Enter_List[a][0].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\디지털 증거\\채증 정보\\" + file_name
        if os.path.isdir(".\\디지털 증거\\채증 정보") == False:
            os.makedirs(".\\디지털 증거\\채증 정보")
        copyfile(file_path, copy_file_path)

        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)

        self.DE_AddAll_Gather_Enter_List[a][1].setText(file_name[file_name.rfind(".") + 1:])
        self.DE_AddAll_Gather_Enter_List[a][2].setText("SHA-256")
        self.DE_AddAll_Gather_Enter_List[a][3].setText(sha256.hexdigest())
        self.DE_AddAll_Gather_Enter_List[a][4].setText(copy_file_path)

    # DE 전체 + 버튼 누르고 Acquisition browse
    def DE_Acquisition_Info_file_browse__browseButton_1_QFileDialog2(self, a):
        file_name = QFileDialog.getOpenFileName()
        self.DE_AddAll_Acquisition_Browse_List[a][0].setText(file_name[0])

    # DE 전체 + 버튼 누르고 Acquisition Enter
    def DE_Acquisition_Info_file_browse__enterButton_1_Calculate2(self, a):
        file_path = self.DE_AddAll_Acquisition_Enter_List[a][0].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\디지털 증거\\수집 정보\\" + file_name
        if os.path.isdir(".\\디지털 증거\\수집 정보") == False:
            os.makedirs(".\\디지털 증거\\수집 정보")
        copyfile(file_path, copy_file_path)

        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)

        self.DE_AddAll_Acquisition_Enter_List[a][1].setText(file_name)
        self.DE_AddAll_Acquisition_Enter_List[a][2].setText(copy_file_path)
        self.DE_AddAll_Acquisition_Enter_List[a][3].setText("SHA-256")
        self.DE_AddAll_Acquisition_Enter_List[a][4].setText(sha256.hexdigest())

    # DE 전체 + 버튼 누르고 Other Enter
    def DE_other_files_file_browse__EnterButton_1_Calculate2(self, a):
        file_path = self.DE_AddAll_Other_Files_Enter_List[a][0].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\디지털 증거\\기타 파일\\" + file_name
        if os.path.isdir(".\\디지털 증거\\기타 파일") == False:
            os.makedirs(".\\디지털 증거\\기타 파일")
        copyfile(file_path, copy_file_path)

        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)

            file_size = os.path.getsize(copy_file_path)

            # 0                                                  #파일 입력
            # 1                                                  #고유번호
        self.DE_AddAll_Other_Files_Enter_List[a][2].setText(file_name[file_name.rfind(".") + 1:])  # 파일 유형
        self.DE_AddAll_Other_Files_Enter_List[a][3].setText(str(file_size))  # 파일 크기
        self.DE_AddAll_Other_Files_Enter_List[a][4].setText(copy_file_path)  # 파일 경로
        self.DE_AddAll_Other_Files_Enter_List[a][5].setText("SHA-256")  # 해시 종류
        self.DE_AddAll_Other_Files_Enter_List[a][6].setText(sha256.hexdigest())  # 해시값

    # DE Gather_Info +클릭하면 Add
    def DE_Gather_Info__addButton_1_AddGatherInfoFile(self, a):
        self.DE_Gather_Info_num += 1

        #
        tmp_DE_Gather_Info_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Gather_Info_file__verticalLayout_1.setObjectName(
            "DE_Gather_Info_file__verticalLayout_" + str(self.DE_Gather_Info_num))

        tmp = QtWidgets.QFrame(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp.setFrameShape(QtWidgets.QFrame.HLine)
        tmp.setFrameShadow(QtWidgets.QFrame.Sunken)
        tmp_DE_Gather_Info_file__verticalLayout_1.addWidget(tmp)

        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__horizontalLayout_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_file__filebrowse__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__label_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__label_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_file__filebrowse__label_1.setText("파일 입력: ")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__label_1)
        tmp_DE_Gather_Info_file__filebrowse__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__lineEdit_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__lineEdit_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)

        tmp_DE_Gather_Info_file__filebrowse__browseButton_1 = QtWidgets.QPushButton(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__browseButton_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.setText("Browse...")

        b = len(self.DE_Gather_Info_List[a])
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog(a, b))

        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__browseButton_1)

        tmp_DE_Gather_Info_file__filebrowse__enterButton_1 = QtWidgets.QPushButton(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__enterButton_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.setText("Enter")
        b = len(self.DE_Gather_Info_List[a])
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__enterButton_1_Calculate(a, b))
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__enterButton_1)

        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_media_type__horizontalLayout_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_media_type__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_media_type__label_1.setObjectName(
            "DE_Gather_Info_gather_media_type__label_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_media_type__label_1.setText("채증 미디어 유형: ")
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_media_type__label_1)
        tmp_DE_Gather_Info_gather_media_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_media_type__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_media_type__lineEdit_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(
            tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_media_type__lineEdit_1.setReadOnly(True)
        ##self.DE_Gather_Info_gather_media_type__lineEdit_1.setReadOnly(True)

        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_hash_type__horizontalLayout_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info__gather_hash_type__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__gather_hash_type__label_1.setObjectName(
            "DE_Gather_Info__gather_hash_type__label_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info__gather_hash_type__label_1.setText("채증 미디어 해시 종류: ")
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info__gather_hash_type__label_1)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1.setObjectName(
            "DE_Gather_Info__gather_hash_type__lineEdit_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1.setReadOnly(True)
        ##self.DE_Gather_Info__gather_hash_type__lineEdit_1.setReadOnly(True)

        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_hash__horizontalLayout_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_hash__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_hash__label_1.setObjectName(
            "DE_Gather_Info_gather_hash__label_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_hash__label_1.setText("채증 미디어 해시 값: ")
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_hash__label_1)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_hash__lineEdit_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_hash__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1.setReadOnly(True)
        ##self.DE_Gather_Info_gather_hash__lineEdit_1.setReadOnly(True)

        tmp_DE_Gather_Info_gather_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_path__horizontalLayout_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_path__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_path__label_1.setObjectName(
            "DE_Gather_Info_gather_path__label_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_path__label_1.setText("채증 미디어 경로: ")
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_path__label_1)
        tmp_DE_Gather_Info_gather_path__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_path__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_path__lineEdit_" + str(self.DE_Gather_Info_num))
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        tmp_DE_Gather_Info_gather_path__lineEdit_1.setReadOnly(True)
        ##self.DE_Gather_Info_gather_path__lineEdit_1.setReadOnly(True)

        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_path__horizontalLayout_1)
        self.DE_Gather_Info_File_List[a].addLayout(tmp_DE_Gather_Info_file__verticalLayout_1, self.DE_Gather_Info_num, 0, 1, 1)

        tmp_list = list()
        tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        self.DE_Gather_Info_List[a].append(tmp_list)

    # DE Gather Info Browse버튼 클릭하면 파일 입력
    def DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog(self, a, b):
        file_name = QFileDialog.getOpenFileName()
        self.DE_Gather_Info_List[a][b][0].setText(file_name[0])

    # DE Gather enter버튼 클릭하면 계산
    def DE_Gather_Info_file__filebrowse__enterButton_1_Calculate(self, a, b):
        file_path = self.DE_Gather_Info_List[a][b][0].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\디지털 증거\\채증 정보\\" + file_name
        if os.path.isdir(".\\디지털 증거\\채증 정보") == False:
            os.makedirs(".\\디지털 증거\\채증 정보")
        copyfile(file_path, copy_file_path)

        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)

        self.DE_Gather_Info_List[a][b][1].setText(file_name[file_name.rfind(".") + 1:])
        self.DE_Gather_Info_List[a][b][2].setText("SHA-256")
        self.DE_Gather_Info_List[a][b][3].setText(sha256.hexdigest())
        self.DE_Gather_Info_List[a][b][4].setText(copy_file_path)

    ##DE Acquisition_Info +버튼 클릭하면 파일add
    def DE_Acquisition_Info__addButton_1_AddDEAquisitionFile(self, a):
        self.DE_Acquisition_Info_num += 1

        tmp_DE_Aquisition_Info_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Aquisition_Info_file__verticalLayout_1.setObjectName(
            "DE_Aquisition_Info_file__verticalLayout_" + str(self.DE_Acquisition_Info_num))

        tmp = QtWidgets.QFrame(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp.setFrameShape(QtWidgets.QFrame.HLine)
        tmp.setFrameShadow(QtWidgets.QFrame.Sunken)
        tmp_DE_Aquisition_Info_file__verticalLayout_1.addWidget(tmp)

        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.setObjectName(
            "DE_Aquisition_Info_file_browse_horizontalLayout_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_file_browse__label_1 = QtWidgets.QLabel(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_file_browse__label_1.setText("파일입력: ")
        tmp_DE_Acquisition_Info_file_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        tmp_DE_Acquisition_Info_file_browse__label_1.setObjectName(
            "DE_Acquisition_Info_file_browse__label_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_file_browse__label_1)
        tmp_DE_Acquisition_Info_file_browse__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_file_browse__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_file_browse__lineEdit_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_file_browse__lineEdit_1)

        tmp_DE_Acquisition_Info_file_browse__browseButton_1 = QtWidgets.QPushButton(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_file_browse__browseButton_1.setObjectName(
            "DE_Acquisition_Info_file_browse__browseButton_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_file_browse__browseButton_1.setText("Browse...")

        b = len(self.DE_Acquisition_Info_List[a])
        tmp_DE_Acquisition_Info_file_browse__browseButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info_file_browse__browseButton_1_QFileDialog(a, b))

        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_file_browse__browseButton_1)

        tmp_DE_Acquisition_Info_file_browse__enterButton_1 = QtWidgets.QPushButton(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_file_browse__enterButton_1.setObjectName(
            "DE_Acquisition_Info_file_browse__enterButton_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_file_browse__enterButton_1.setText("Enter")

        b = len(self.DE_Acquisition_Info_List[a])
        tmp_DE_Acquisition_Info_file_browse__enterButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info_file_browse__enterButton_1_Calculate(a, b))

        tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_file_browse__enterButton_1)

        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(
            tmp_DE_Aquisition_Info_file_browse_horizontalLayout_1)

        tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_" + str(
                self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_digital_evidence_file_name__label_1 = QtWidgets.QLabel(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_name__label_1.setObjectName(
            "DE_Acquisition_Info_digital_evidence_file_name__label_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_digital_evidence_file_name__label_1.setText("디지털 증거 파일 이름: ")
        tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_digital_evidence_file_name__label_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_digital_evidence_file_name__lineEdit_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Infro_file_digital_evidence_file_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1.setReadOnly(True)

        ##self.DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1.setReadOnly(True)

        tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1.setObjectName(
            "DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_digital_evidence_file_path__label_1 = QtWidgets.QLabel(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_path__label_1.setObjectName(
            "DE_Acquisition_Info_digital_evidence_file_path__label_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_digital_evidence_file_path__label_1.setText("디지털 증거 파일 경로: ")
        tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_digital_evidence_file_path__label_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_digital_evidence_file_path__lineEdit_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1.setReadOnly(True)
        ##self.DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1.setReadOnly(True)

        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(
            tmp_DE_Aquisition_Info_digital_evidence_file_path__horizontalLayout_1)
        tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_hash_type__horizontalLayout_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_hash_type__label_1 = QtWidgets.QLabel(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_hash_type__label_1.setObjectName(
            "DE_Acquisition_Info_hash_type__label_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_hash_type__label_1.setText("해시 종류: ")
        tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_hash_type__label_1)
        tmp_DE_Acquisition_Info_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_hash_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_hash_type__lineEdit_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_hash_type__lineEdit_1)
        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_hash_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_hash_type__lineEdit_1.setReadOnly(True)
        ##self.DE_Acquisition_Info_hash_type__lineEdit_1.setReadOnly(True)

        tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_hash_value__horizontalLayout_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_hash_value__label_1 = QtWidgets.QLabel(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_hash_value__label_1.setObjectName(
            "DE_Acquisition_Info_hash_value__label_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_hash_value__label_1.setText("해시값: ")
        tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_hash_value__label_1)
        tmp_DE_Acquisition_Info_hash_value__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Aquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_hash_value__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_hash_value__lineEdit_" + str(self.DE_Acquisition_Info_num))
        tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_hash_value__lineEdit_1)
        tmp_DE_Acquisition_Info_hash_value__lineEdit_1.setReadOnly(True)
        ##self.DE_Acquisition_Info_hash_value__lineEdit_1.setReadOnly(True)

        tmp_DE_Aquisition_Info_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_hash_value__horizontalLayout_1)
        self.DE_Acquisition_Info_File_List[a].addLayout(tmp_DE_Aquisition_Info_file__verticalLayout_1, self.DE_Acquisition_Info_num, 0, 1, 1)


        tmp_list = list()
        tmp_list.append(tmp_DE_Acquisition_Info_file_browse__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_hash_value__lineEdit_1)
        self.DE_Acquisition_Info_List[a].append(tmp_list)

    ##DE Acquisition_Info Browse버튼 클릭하면 파일 업로드
    def DE_Acquisition_Info_file_browse__browseButton_1_QFileDialog(self, a, b):
        file_name = QFileDialog.getOpenFileName()
        self.DE_Acquisition_Info_List[a][b][0].setText(file_name[0])

    ## DE_Acquisition Enter 버튼 누르면 파일 계산
    def DE_Acquisition_Info_file_browse__enterButton_1_Calculate(self, a, b):
        file_path = self.DE_Acquisition_Info_List[a][b][0].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\디지털 증거\\수집 정보\\" + file_name
        if os.path.isdir(".\\디지털 증거\\수집 정보") == False:
            os.makedirs(".\\디지털 증거\\수집 정보")
        copyfile(file_path, copy_file_path)

        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)

        self.DE_Acquisition_Info_List[a][b][1].setText(file_name)  # 디지털 증거 파일 이름
        self.DE_Acquisition_Info_List[a][b][2].setText(copy_file_path)  # 디지털 증거 파일 경로
        self.DE_Acquisition_Info_List[a][b][3].setText("SHA-256")  # 해시 종류
        self.DE_Acquisition_Info_List[a][b][4].setText(sha256.hexdigest())  # 해시 값

        # <Analysis Info>

    # DE Other Files +누르면 add
    def DE_other_files__addButton_1_AddDEOtherFiles(self, a):
        print("dsakjlhadps")
        self.DE_Other_Files_num += 1

        tmp_DE_other_files__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_other_files__verticalLayout_1.setObjectName("DE_other_files__verticalLayout_1")

        tmp = QtWidgets.QFrame(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp.setFrameShape(QtWidgets.QFrame.HLine)
        tmp.setFrameShadow(QtWidgets.QFrame.Sunken)
        tmp_DE_other_files__verticalLayout_1.addWidget(tmp)

        tmp_DE_other_files_file_browse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_browse__horizontalLayout_1.setObjectName("DE_other_files_file_browse__horizontalLayout_1")
        tmp_DE_other_files_file_browse__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__label_1.setObjectName("DE_other_files_file_browse__label_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_browse__label_1.setText("파일 입력: ")

        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__label_1)
        tmp_DE_other_files_file_browse__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__lineEdit_1.setObjectName("DE_other_files_file_browse__lineEdit_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__lineEdit_1)
        tmp_DE_other_files_file_browse__browseButton_1 = QtWidgets.QPushButton(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__browseButton_1.setObjectName("DE_other_files_file_browse__browseButton_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_browse__browseButton_1.setText("Browse...")

        b = len(self.DE_Other_Files_Info_List[a])
        tmp_DE_other_files_file_browse__browseButton_1.clicked.connect(
            lambda: self.DE_other_files_file_browse__browseButton_1_QFileDialog(a, b))

        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__browseButton_1)

        tmp_DE_other_files_file_browse__EnterButton_1 = QtWidgets.QPushButton(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__EnterButton_1.setObjectName("DE_other_files_file_browse__EnterButton_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_browse__EnterButton_1.setText("Enter")

        b = len(self.DE_Other_Files_Info_List[a])
        tmp_DE_other_files_file_browse__EnterButton_1.clicked.connect(
            lambda: self.DE_other_files_file_browse__EnterButton_1_Calculate(a, b))

        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__EnterButton_1)

        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_browse__horizontalLayout_1)
        tmp_DE_other_files_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_id__horizontalLayout_1.setObjectName("DE_other_files_id__horizontalLayout_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_id__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_id__label_1.setObjectName("DE_other_files_id__label_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_id__label_1.setText("고유번호: ")
        tmp_DE_other_files_id__horizontalLayout_1.addWidget(tmp_DE_other_files_id__label_1)
        tmp_DE_other_files_id__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_id__lineEdit_1.setObjectName("DE_other_files_id__lineEdit_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_id__horizontalLayout_1.addWidget(tmp_DE_other_files_id__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_id__horizontalLayout_1)
        tmp_DE_other_files_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_type__horizontalLayout_1.setObjectName("DE_other_files_type__horizontalLayout_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_type__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_type__label_1.setObjectName("DE_other_files_type__label_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_type__label_1.setText("파일 유형: ")

        tmp_DE_other_files_type__horizontalLayout_1.addWidget(tmp_DE_other_files_type__label_1)
        tmp_DE_other_files_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_type__lineEdit_1.setObjectName("DE_other_files_type__lineEdit_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_type__horizontalLayout_1.addWidget(tmp_DE_other_files_type__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_type__horizontalLayout_1)
        tmp_DE_other_files_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_size__horizontalLayout_1.setObjectName("DE_other_files_file_size__horizontalLayout_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_size__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_size__label_1.setObjectName("DE_other_files_file_size__label_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_size__label_1.setText("파일 크기: ")

        tmp_DE_other_files_file_size__horizontalLayout_1.addWidget(tmp_DE_other_files_file_size__label_1)
        tmp_DE_other_files_file_size__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_size__lineEdit_1.setObjectName("DE_other_files_file_size__lineEdit_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_size__horizontalLayout_1.addWidget(tmp_DE_other_files_file_size__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_size__horizontalLayout_1)
        tmp_DE_other_files_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_path__horizontalLayout_1.setObjectName("DE_other_files_file_path__horizontalLayout_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_path__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_path__label_1.setObjectName("DE_other_files_file_path__label_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_path__label_1.setText("파일 경로: ")

        tmp_DE_other_files_file_path__horizontalLayout_1.addWidget(tmp_DE_other_files_file_path__label_1)
        tmp_DE_other_files_file_path__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_path__lineEdit_1.setObjectName("DE_other_files_file_path__lineEdit_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_path__horizontalLayout_1.addWidget(tmp_DE_other_files_file_path__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_path__horizontalLayout_1)
        tmp_DE_other_files_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_hash_type__horizontalLayout_1.setObjectName("DE_other_files_file_hash_type__horizontalLayout_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_hash_type__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_type__label_1.setObjectName("DE_other_files_file_hash_type__label_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_hash_type__label_1.setText("해시 종류: ")

        tmp_DE_other_files_file_hash_type__horizontalLayout_1.addWidget(tmp_DE_other_files_file_hash_type__label_1)
        tmp_DE_other_files_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_type__lineEdit_1.setObjectName("DE_other_files_file_hash_type__lineEdit_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_hash_type__horizontalLayout_1.addWidget(tmp_DE_other_files_file_hash_type__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_hash_type__horizontalLayout_1)
        tmp_DE_other_files_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_hash_value__horizontalLayout_1.setObjectName("DE_other_files_file_hash_value__horizontalLayout_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_hash_value__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_value__label_1.setObjectName("DE_other_files_file_hash_value__label_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_hash_value__label_1.setText("해시값: ")

        tmp_DE_other_files_file_hash_value__horizontalLayout_1.addWidget(tmp_DE_other_files_file_hash_value__label_1)
        tmp_DE_other_files_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_value__lineEdit_1.setObjectName("DE_other_files_file_hash_value__lineEdit_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_hash_value__horizontalLayout_1.addWidget(tmp_DE_other_files_file_hash_value__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_hash_value__horizontalLayout_1)
        tmp_DE_other_files_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_description__horizontalLayout_1.setObjectName("DE_other_files_file_description__horizontalLayout_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_description__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_description__label_1.setObjectName("DE_other_files_file_description__label_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_description__label_1.setText("파일 설명: ")

        tmp_DE_other_files_file_description__horizontalLayout_1.addWidget(tmp_DE_other_files_file_description__label_1)
        tmp_DE_other_files_file_description__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_description__lineEdit_1.setObjectName("DE_other_files_file_description__lineEdit_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_description__horizontalLayout_1.addWidget(tmp_DE_other_files_file_description__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_description__horizontalLayout_1)
        tmp_DE_other_files_file_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_metadata__horizontalLayout_1.setObjectName("DE_other_files_file_metadata__horizontalLayout_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_metadata__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_metadata__label_1.setObjectName("DE_other_files_file_metadata__label_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_metadata__label_1.setText("파일 메타데이터: ")

        tmp_DE_other_files_file_metadata__horizontalLayout_1.addWidget(tmp_DE_other_files_file_metadata__label_1)
        tmp_DE_other_files_file_metadata__lineEdit_1 = QtWidgets.QLineEdit(self.DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_metadata__lineEdit_1.setObjectName("DE_other_files_file_metadata__lineEdit_" + str(self.DE_Other_Files_num))
        tmp_DE_other_files_file_metadata__horizontalLayout_1.addWidget(tmp_DE_other_files_file_metadata__lineEdit_1)

        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_metadata__horizontalLayout_1)
        self.DE_Other_Files_File_List[a].addLayout(tmp_DE_other_files__verticalLayout_1, self.DE_Other_Files_num, 0, 1, 1)

        '''tmp_list = list()
        tmp_list.append(tmp_DE_other_files_file_browse__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_id__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_type__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_size__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_hash_value__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_description__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_metadata__lineEdit_1)
        self.DE_Other_Files_Info_List[a].append(tmp_list)'''


    # DE Other Files Browse누르면 파일 업로드
    def DE_other_files_file_browse__browseButton_1_QFileDialog(self, a, b):
        file_name = QFileDialog.getOpenFileName()
        self.DE_Other_Files_Info_List[a][b][0].setText(file_name[0])

    ## DE Other Files Enter 누르면 파일 계산
    def DE_other_files_file_browse__EnterButton_1_Calculate(self, a, b):
        file_path = self.DE_Other_Files_Info_List[a][b][0].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\디지털 증거\\기타 파일\\" + file_name
        if os.path.isdir(".\\디지털 증거\\기타 파일\\") == False:
            os.makedirs(".\\디지털 증거\\기타 파일")
        copyfile(file_path, copy_file_path)

        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)

            file_size = os.path.getsize(copy_file_path)



        input_file = file_path
        exe = "hachoir-metadata"
        process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   universal_newlines=True)
        out_list = []
        for output in process.stdout:
            if 'Metadata' in output:
                continue
            output = output.replace('\n', ', ')
            out_list.append(output)

        result = ""
        for i in out_list:
            result = result + i

        print(result)
            # 0
            # 1
        self.DE_Other_Files_Info_List[a][b][2].setText(file_name[file_name.rfind(".") + 1:])
        self.DE_Other_Files_Info_List[a][b][3].setText(str(file_size))
        self.DE_Other_Files_Info_List[a][b][4].setText(copy_file_path)
        self.DE_Other_Files_Info_List[a][b][5].setText("SHA-256")
        self.DE_Other_Files_Info_List[a][b][6].setText(sha256.hexdigest())
        self.DE_Other_Files_Info_List[a][b][8].setText(str(result))

    ##AI Report +버튼 클릭하면 add보고
    def AI_Reports__addButton_AddAIReports(self):
        self.AIReports_num += 1

        tmp_AI_Reports__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_AI_Reports__verticalLayout_1.setObjectName("AI_Reports__verticalLayout_1")

        tmp = QtWidgets.QFrame(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp.setFrameShape(QtWidgets.QFrame.HLine)
        tmp.setFrameShadow(QtWidgets.QFrame.Sunken)
        tmp_AI_Reports__verticalLayout_1.addWidget(tmp)

        tmp_AI_Reports_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_id__horizontalLayout_1.setObjectName(
            "AI_Reports_id__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_id__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_id__label_1.setObjectName(
            "AI_Reports_id__label_" + str(self.AIReports_num))
        tmp_AI_Reports_id__label_1.setText("고유번호: ")
        tmp_AI_Reports_id__horizontalLayout_1.addWidget(tmp_AI_Reports_id__label_1)

        tmp_AI_Reports_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_id__lineEdit_1.setObjectName(
            "AI_Reports_id__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_id__horizontalLayout_1.addWidget(tmp_AI_Reports_id__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_id__horizontalLayout_1)
        tmp_AI_Reports_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_type__horizontalLayout_1.setObjectName(
            "AI_Reports_type__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_type__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_type__label_1.setObjectName(
            "AI_Reports_type__label_" + str(self.AIReports_num))
        tmp_AI_Reports_type__label_1.setText("유형: ")
        tmp_AI_Reports_type__horizontalLayout_1.addWidget(tmp_AI_Reports_type__label_1)

        tmp_AI_Reports_type__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_type__lineEdit_1.setObjectName(
            "AI_Reports_type__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_type__horizontalLayout_1.addWidget(tmp_AI_Reports_type__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_type__horizontalLayout_1)
        tmp_AI_Reports_subtype__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_subtype__horizontalLayout_1.setObjectName(
            "AI_Reports_subtype__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_subtype__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_subtype__label_1.setObjectName(
            "AI_Reports_subtype__label_" + str(self.AIReports_num))
        tmp_AI_Reports_subtype__label_1.setText("하위유형: ")
        tmp_AI_Reports_subtype__horizontalLayout_1.addWidget(tmp_AI_Reports_subtype__label_1)

        tmp_AI_Reports_subtype__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_subtype__lineEdit_1.setObjectName(
            "AI_Reports_subtype__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_subtype__horizontalLayout_1.addWidget(tmp_AI_Reports_subtype__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_subtype__horizontalLayout_1)
        tmp_AI_Reports_mgmt_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_mgmt_id__horizontalLayout_1.setObjectName(
            "AI_Reports_mgmt_id__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_mgmt_id__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_mgmt_id__label_1.setObjectName(
            "AI_Reports_mgmt_id__label_" + str(self.AIReports_num))
        tmp_AI_Reports_mgmt_id__label_1.setText("장비 고유번호: ")
        tmp_AI_Reports_mgmt_id__horizontalLayout_1.addWidget(tmp_AI_Reports_mgmt_id__label_1)

        tmp_AI_Reports_mgmt_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_mgmt_id__lineEdit_1.setObjectName(
            "AI_Reports_mgmt_id__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_mgmt_id__horizontalLayout_1.addWidget(tmp_AI_Reports_mgmt_id__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_mgmt_id__horizontalLayout_1)
        tmp_AI_Reports_submission_agency__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_submission_agency__horizontalLayout_1.setObjectName(
            "AI_Reports_submission_agency__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_submission_agency__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_submission_agency__label_1.setObjectName(
            "AI_Reports_submission_agency__label_" + str(self.AIReports_num))
        tmp_AI_Reports_submission_agency__label_1.setText("제출 기관: ")
        tmp_AI_Reports_submission_agency__horizontalLayout_1.addWidget(tmp_AI_Reports_submission_agency__label_1)

        tmp_AI_Reports_submission_agency__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_submission_agency__lineEdit_1.setObjectName(
            "AI_Reports_submission_agency__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_submission_agency__horizontalLayout_1.addWidget(tmp_AI_Reports_submission_agency__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_submission_agency__horizontalLayout_1)
        tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1.setObjectName(
            "AI_Reports_reports_creation_datetime__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_reprot_creation_datetime__label_1 = QtWidgets.QLabel(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_reprot_creation_datetime__label_1.setObjectName(
            "AI_Reports_reprot_creation_datetime__label_" + str(self.AIReports_num))
        tmp_AI_Reports_reprot_creation_datetime__label_1.setText("보고서 작성 시간 :")
        tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1.addWidget(
            tmp_AI_Reports_reprot_creation_datetime__label_1)

        tmp_AI_Reports_reprot_creation_datetime__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_reprot_creation_datetime__lineEdit_1.setObjectName(
            "AI_Reports_reprot_creation_datetime__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1.addWidget(
            tmp_AI_Reports_reprot_creation_datetime__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1)
        tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1.setObjectName(
            "AI_Reports_division_name_of_report_maker__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_division_name_of_report_maker__label_1 = QtWidgets.QLabel(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_division_name_of_report_maker__label_1.setObjectName(
            "AI_Reports_division_name_of_report_maker__label_" + str(self.AIReports_num))
        tmp_AI_Reports_division_name_of_report_maker__label_1.setText("보고서 작성 부서명: ")
        tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1.addWidget(
            tmp_AI_Reports_division_name_of_report_maker__label_1)

        tmp_AI_Reports_division_name_of_report_maker__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_division_name_of_report_maker__lineEdit_1.setObjectName(
            "AI_Reports_division_name_of_report_maker__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1.addWidget(
            tmp_AI_Reports_division_name_of_report_maker__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1)
        tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1.setObjectName(
            "AI_Reports_team_name_of_report_maker__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_team_name_of_report_maker__label_1 = QtWidgets.QLabel(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_team_name_of_report_maker__label_1.setObjectName(
            "AI_Reports_team_name_of_report_maker__label_" + str(self.AIReports_num))
        tmp_AI_Reports_team_name_of_report_maker__label_1.setText("보고서 작성 팀명: ")
        tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1.addWidget(
            tmp_AI_Reports_team_name_of_report_maker__label_1)

        tmp_AI_Reports_team_name_of_report_maker__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_team_name_of_report_maker__lineEdit_1.setObjectName(
            "AI_Reports_team_name_of_report_maker__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1.addWidget(
            tmp_AI_Reports_team_name_of_report_maker__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1)
        tmp_AI_Reports_file_info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_info__horizontalLayout_1.setObjectName(
            "AI_Reports_file_info__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_file_info__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_info__label_1.setObjectName(
            "AI_Reports_file_info__label__" + str(self.AIReports_num))
        tmp_AI_Reports_file_info__label_1.setText("파일 입력: ")
        tmp_AI_Reports_file_info__horizontalLayout_1.addWidget(tmp_AI_Reports_file_info__label_1)

        tmp_AI_Reports_file_info__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_info__lineEdit_1.setObjectName(
            "AI_Reports_file_info__lineEdit__" + str(self.AIReports_num))
        tmp_AI_Reports_file_info__horizontalLayout_1.addWidget(tmp_AI_Reports_file_info__lineEdit_1)

        tmp_AI_Reports_file_info__browseButton_1 = QtWidgets.QPushButton(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_info__browseButton_1.setObjectName(
            "AI_Reports_file_info__browseButton__" + str(self.AIReports_num))
        tmp_AI_Reports_file_info__browseButton_1.setText("Browse...")
        a = len(self.AIReports_List)
        tmp_AI_Reports_file_info__browseButton_1.clicked.connect(
            lambda: self.AI_Reports_file_info__browseButton_1_QFileDialog(a))
        tmp_AI_Reports_file_info__horizontalLayout_1.addWidget(tmp_AI_Reports_file_info__browseButton_1)

        tmp_AI_Reports_file_info__enterButton_1 = QtWidgets.QPushButton(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_info__enterButton_1.setObjectName(
            "AI_Reports_file_info__enterButton__" + str(self.AIReports_num))
        tmp_AI_Reports_file_info__enterButton_1.setText("Enter")
        a = len(self.AIReports_List)
        tmp_AI_Reports_file_info__enterButton_1.clicked.connect(
            lambda: self.AI_Reports_file_info__enterButton_1_Calculate(a))
        tmp_AI_Reports_file_info__horizontalLayout_1.addWidget(tmp_AI_Reports_file_info__enterButton_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_info__horizontalLayout_1)
        tmp_AI_Reports_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_name__horizontalLayout_1.setObjectName(
            "AI_Reports_file_name__horizontalLayout__" + str(self.AIReports_num))

        tmp_AI_Reports_file_name__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_name__label_1.setObjectName("AI_Reports_file_name__label_" + str(self.AIReports_num))
        tmp_AI_Reports_file_name__label_1.setText("파일 이름: ")
        tmp_AI_Reports_file_name__horizontalLayout_1.addWidget(tmp_AI_Reports_file_name__label_1)

        tmp_AI_Reports_file_name__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_name__lineEdit_1.setObjectName(
            "AI_Reports_file_name__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_file_name__horizontalLayout_1.addWidget(
            tmp_AI_Reports_file_name__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_name__horizontalLayout_1)
        tmp_AI_Reports_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_size__horizontalLayout_1.setObjectName(
            "AI_Reports_file_size__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_file_size__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_size__label_1.setObjectName(
            "AI_Reports_file_size__label_" + str(self.AIReports_num))
        tmp_AI_Reports_file_size__label_1.setText("파일 크기: ")
        tmp_AI_Reports_file_size__horizontalLayout_1.addWidget(tmp_AI_Reports_file_size__label_1)

        tmp_AI_Reports_file_size__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_size__lineEdit_1.setObjectName(
            "AI_Reports_file_size__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_file_size__horizontalLayout_1.addWidget(tmp_AI_Reports_file_size__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_size__horizontalLayout_1)
        tmp_AI_Reports_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_path__horizontalLayout_1.setObjectName(
            "AI_Reports_file_path__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_file_path__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_path__label_1.setObjectName("AI_Reports_file_path__label_" + str(self.AIReports_num))
        tmp_AI_Reports_file_path__label_1.setText("파일 경로: ")
        tmp_AI_Reports_file_path__horizontalLayout_1.addWidget(tmp_AI_Reports_file_path__label_1)

        tmp_AI_Reports_file_path__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_path__lineEdit_1.setObjectName(
            "AI_Reports_file_path__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_file_path__horizontalLayout_1.addWidget(tmp_AI_Reports_file_path__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_path__horizontalLayout_1)
        tmp_AI_Reports_file_creation_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_creation_datetime__horizontalLayout_1.setObjectName(
            "AI_Reports_file_creation_datetime__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_file_creation_datetime__label_1 = QtWidgets.QLabel(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_creation_datetime__label_1.setObjectName(
            "AI_Reports_file_creation_datetime__label_" + str(self.AIReports_num))
        tmp_AI_Reports_file_creation_datetime__label_1.setText("파일 생성 날짜/시간: ")
        tmp_AI_Reports_file_creation_datetime__horizontalLayout_1.addWidget(
            tmp_AI_Reports_file_creation_datetime__label_1)

        tmp_AI_Reports_file_creation_datetime__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_creation_datetime__lineEdit_1.setObjectName(
            "AI_Reports_file_creation_datetime__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_file_creation_datetime__horizontalLayout_1.addWidget(
            tmp_AI_Reports_file_creation_datetime__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_creation_datetime__horizontalLayout_1)
        tmp_AI_Reports_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_description__horizontalLayout_1.setObjectName(
            "AI_Reports_file_description__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_file_description__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_description__label_1.setObjectName(
            "AI_Reports_file_description__label_" + str(self.AIReports_num))
        tmp_AI_Reports_file_description__label_1.setText("파일 설명: ")
        tmp_AI_Reports_file_description__horizontalLayout_1.addWidget(tmp_AI_Reports_file_description__label_1)

        tmp_AI_Reports_file_description__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_description__lineEdit_1.setObjectName(
            "AI_Reports_file_description__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_file_description__horizontalLayout_1.addWidget(tmp_AI_Reports_file_description__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_description__horizontalLayout_1)
        tmp_AI_Reports_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_hash_type__horizontalLayout_1.setObjectName(
            "AI_Reports_file_hash_type__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_file_hash_type__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_hash_type__label_1.setObjectName(
            "AI_Reports_file_hash_type__label_" + str(self.AIReports_num))
        tmp_AI_Reports_file_hash_type__label_1.setText("파일 해시 종류: ")
        tmp_AI_Reports_file_hash_type__horizontalLayout_1.addWidget(tmp_AI_Reports_file_hash_type__label_1)

        tmp_AI_Reports_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_hash_type__lineEdit_1.setObjectName(
            "AI_Reports_file_hash_type__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_file_hash_type__horizontalLayout_1.addWidget(tmp_AI_Reports_file_hash_type__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_hash_type__horizontalLayout_1)
        tmp_AI_Reports_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_hash_value__horizontalLayout_1.setObjectName(
            "AI_Reports_file_hash_value__horizontalLayout_" + str(self.AIReports_num))

        tmp_AI_Reports_file_hash_value__label_1 = QtWidgets.QLabel(self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_hash_value__label_1.setObjectName(
            "AI_Reports_file_hash_value__label_" + str(self.AIReports_num))
        tmp_AI_Reports_file_hash_value__label_1.setText("파일 해시 값: ")
        tmp_AI_Reports_file_hash_value__horizontalLayout_1.addWidget(tmp_AI_Reports_file_hash_value__label_1)

        tmp_AI_Reports_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_hash_value__lineEdit_1.setObjectName(
            "AI_Reports_file_hash_value__lineEdit_" + str(self.AIReports_num))
        tmp_AI_Reports_file_hash_value__horizontalLayout_1.addWidget(tmp_AI_Reports_file_hash_value__lineEdit_1)

        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_hash_value__horizontalLayout_1)
        self.gridLayout_12.addLayout(tmp_AI_Reports__verticalLayout_1, self.AIReports_num, 0, 1, 1)

        tmp_list = list()
        tmp_list.append(tmp_AI_Reports_id__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_type__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_subtype__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_mgmt_id__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_submission_agency__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_reprot_creation_datetime__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_division_name_of_report_maker__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_team_name_of_report_maker__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_file_info__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_file_name__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_file_size__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_file_path__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_file_creation_datetime__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_file_description__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_file_hash_type__lineEdit_1)
        tmp_list.append(tmp_AI_Reports_file_hash_value__lineEdit_1)
        self.AIReports_List.append(tmp_list)

        # self.AIReports_Button_num = 1
        # self.AIReports_Button_List = list()
        tmp_list = list()
        tmp_list.append(tmp_AI_Reports_file_info__browseButton_1)
        tmp_list.append(tmp_AI_Reports_file_info__enterButton_1)
        self.AIReports_Button_List.append(tmp_list)

        tmp_AI_Reports_file_name__lineEdit_1.setReadOnly(True)
        tmp_AI_Reports_file_size__lineEdit_1.setReadOnly(True)
        tmp_AI_Reports_file_path__lineEdit_1.setReadOnly(True)
        tmp_AI_Reports_file_creation_datetime__lineEdit_1.setReadOnly(True)
        tmp_AI_Reports_file_hash_type__lineEdit_1.setReadOnly(True)
        tmp_AI_Reports_file_hash_value__lineEdit_1.setReadOnly(True)

    ## AI Report Browse 버튼 클릭하면 파일 업로드
    def AI_Reports_file_info__browseButton_1_QFileDialog(self, a):
        file_name = QFileDialog.getOpenFileName()
        self.AIReports_List[a][8].setText(file_name[0])

    ## AI Report Enter 클릭하면 계산
    def AI_Reports_file_info__enterButton_1_Calculate(self, a):
        file_path = self.AIReports_List[a][8].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\분석 정보\\보고서\\" + file_name
        if os.path.isdir(".\\분석 정보\\보고서") == False:
            os.makedirs(".\\분석 정보\\보고서")
        copyfile(file_path, copy_file_path)

        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)

        file_size = os.path.getsize(copy_file_path)

        # file_date = os.path.getctime(file_path)

        new_file_date = str(datetime.datetime.fromtimestamp(os.path.getctime(file_path),
                                                            tz=datetime.timezone(datetime.timedelta(hours=9))))

        self.AIReports_List[a][9].setText(file_name)  # 파일 이름
        self.AIReports_List[a][10].setText(str(file_size))  # 파일 크기
        self.AIReports_List[a][11].setText(copy_file_path)  # 파일 경로
        self.AIReports_List[a][12].setText(new_file_date)  # 파일 생성 날짜/시간
        # 13                                      #파일 설명
        self.AIReports_List[a][14].setText("SHA-256")  # 파일 해시 종류
        self.AIReports_List[a][15].setText(sha256.hexdigest())  # 파일 해시 값

    ## AI other file +버튼 클릭하면 파일add
    def AI_other_files__addButton_AddAIotherfile(self):
        self.AI_num += 1

        tmp_AI_other_files__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_AI_other_files__verticalLayout_1.setObjectName("AI_other_files__verticalLayout_1")

        tmp = QtWidgets.QFrame(self.AI__scrollAreaWidgetContents)
        tmp.setFrameShape(QtWidgets.QFrame.HLine)
        tmp.setFrameShadow(QtWidgets.QFrame.Sunken)
        tmp_AI_other_files__verticalLayout_1.addWidget(tmp)

        tmp_AI_other_files_file_browse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_browse__horizontalLayout_1.setObjectName(
            "AI_other_files_file_browse__horizontalLayout_" + str(self.AI_num))

        tmp_AI_other_files_file_browse__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_browse__label_1.setObjectName(
            "AI_other_files_file_browse__label_" + str(self.AI_num))
        tmp_AI_other_files_file_browse__label_1.setText("파일 입력: ")
        tmp_AI_other_files_file_browse__horizontalLayout_1.addWidget(tmp_AI_other_files_file_browse__label_1)

        tmp_AI_other_files_file_browse__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_browse__lineEdit_1.setObjectName(
            "AI_other_files_file_browse__lineEdit_" + str(self.AI_num))
        tmp_AI_other_files_file_browse__horizontalLayout_1.addWidget(
            tmp_AI_other_files_file_browse__lineEdit_1)

        tmp_AI_other_files_file_browse__browseButton_1 = QtWidgets.QPushButton(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_browse__browseButton_1.setObjectName(
            "AI_other_files_file_browse__browseButton_1")
        tmp_AI_other_files_file_browse__browseButton_1.setText("Browse...")

        a = len(self.AI_List)
        tmp_AI_other_files_file_browse__browseButton_1.clicked.connect(
            lambda: self.AI_other_files_file_browse__browseButton_1_QFileDialog(a))

        tmp_AI_other_files_file_browse__horizontalLayout_1.addWidget(tmp_AI_other_files_file_browse__browseButton_1)
        tmp_AI_other_files_file_browse__enterButton_1 = QtWidgets.QPushButton(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_browse__enterButton_1.setObjectName("AI_other_files_file_browse__enterButton_1")
        tmp_AI_other_files_file_browse__enterButton_1.setText("Enter")

        a = len(self.AI_List)
        tmp_AI_other_files_file_browse__enterButton_1.clicked.connect(
            lambda: self.AI_other_files_file_browse__enterButton_1_Calculate(a))

        tmp_AI_other_files_file_browse__horizontalLayout_1.addWidget(tmp_AI_other_files_file_browse__enterButton_1)

        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_browse__horizontalLayout_1)
        tmp_AI_other_files_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_id__horizontalLayout_1.setObjectName(
            "AI_other_files_id__horizontalLayout_" + str(self.AI_num))

        tmp_AI_other_files_id__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_id__label_1.setObjectName("AI_other_files_id__label_" + str(self.AI_num))
        tmp_AI_other_files_id__label_1.setText("고유번호: ")
        tmp_AI_other_files_id__horizontalLayout_1.addWidget(tmp_AI_other_files_id__label_1)

        tmp_AI_other_files_id__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_id__lineEdit_1.setObjectName("AI_other_files_id__lineEdit_" + str(self.AI_num))
        tmp_AI_other_files_id__horizontalLayout_1.addWidget(tmp_AI_other_files_id__lineEdit_1)

        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_id__horizontalLayout_1)
        tmp_AI_other_files_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_type__horizontalLayout_1.setObjectName(
            "AI_other_files_type__horizontalLayout_" + str(self.AI_num))

        tmp_AI_other_files_type__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_type__label_1.setObjectName("AI_other_files_type__label_" + str(self.AI_num))
        tmp_AI_other_files_type__label_1.setText("파일 유형: ")
        tmp_AI_other_files_type__horizontalLayout_1.addWidget(tmp_AI_other_files_type__label_1)

        tmp_AI_other_files_type__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_type__lineEdit_1.setObjectName("AI_other_files_type__lineEdit_" + str(self.AI_num))
        tmp_AI_other_files_type__horizontalLayout_1.addWidget(tmp_AI_other_files_type__lineEdit_1)

        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_type__horizontalLayout_1)
        tmp_AI_other_files_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_size__horizontalLayout_1.setObjectName(
            "AI_other_files_file_size__horizontalLayout_" + str(self.AI_num))

        tmp_AI_other_files_file_size__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_size__label_1.setObjectName("AI_other_files_file_size__label_" + str(self.AI_num))
        tmp_AI_other_files_file_size__label_1.setText("파일 크기: ")
        tmp_AI_other_files_file_size__horizontalLayout_1.addWidget(tmp_AI_other_files_file_size__label_1)

        tmp_AI_other_files_file_size__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_size__lineEdit_1.setObjectName(
            "AI_other_files_file_size__lineEdit_" + str(self.AI_num))
        tmp_AI_other_files_file_size__horizontalLayout_1.addWidget(tmp_AI_other_files_file_size__lineEdit_1)

        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_size__horizontalLayout_1)
        tmp_AI_other_files_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_path__horizontalLayout_1.setObjectName(
            "AI_other_files_file_path__horizontalLayout_" + str(self.AI_num))

        tmp_AI_other_files_file_path__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_path__label_1.setObjectName(
            "AI_other_files_file_path__label_" + str(self.AI_num))
        tmp_AI_other_files_file_path__label_1.setText("파일 경로: ")
        tmp_AI_other_files_file_path__horizontalLayout_1.addWidget(tmp_AI_other_files_file_path__label_1)

        tmp_AI_other_files_file_path__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_path__lineEdit_1.setObjectName(
            "AI_other_files_file_path__lineEdit_" + str(self.AI_num))
        tmp_AI_other_files_file_path__horizontalLayout_1.addWidget(tmp_AI_other_files_file_path__lineEdit_1)

        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_path__horizontalLayout_1)
        tmp_AI_other_files_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_hash_type__horizontalLayout_1.setObjectName(
            "AI_other_files_file_hash_type__horizontalLayout_" + str(self.AI_num))

        tmp_AI_other_files_file_hash_type__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_hash_type__label_1.setObjectName(
            "AI_other_files_file_hash_type__label_" + str(self.AI_num))
        tmp_AI_other_files_file_hash_type__label_1.setText("해시 종류: ")
        tmp_AI_other_files_file_hash_type__horizontalLayout_1.addWidget(tmp_AI_other_files_file_hash_type__label_1)

        tmp_AI_other_files_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_hash_type__lineEdit_1.setObjectName(
            "AI_other_files_file_hash_type__lineEdit_" + str(self.AI_num))
        tmp_AI_other_files_file_hash_type__horizontalLayout_1.addWidget(
            tmp_AI_other_files_file_hash_type__lineEdit_1)

        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_hash_type__horizontalLayout_1)
        tmp_AI_other_files_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_hash_value__horizontalLayout_1.setObjectName(
            "AI_other_files_file_hash_value__horizontalLayout_" + str(self.AI_num))

        tmp_AI_other_files_file_hash_value__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_hash_value__label_1.setObjectName(
            "AI_other_files_file_hash_value__label_" + str(self.AI_num))
        tmp_AI_other_files_file_hash_value__label_1.setText("해시값: ")
        tmp_AI_other_files_file_hash_value__horizontalLayout_1.addWidget(
            tmp_AI_other_files_file_hash_value__label_1)

        tmp_AI_other_files_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_hash_value__lineEdit_1.setObjectName(
            "AI_other_files_file_hash_value__lineEdit_" + str(self.AI_num))
        tmp_AI_other_files_file_hash_value__horizontalLayout_1.addWidget(
            tmp_AI_other_files_file_hash_value__lineEdit_1)

        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_hash_value__horizontalLayout_1)
        tmp_AI_other_files_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_description__horizontalLayout_1.setObjectName(
            "AI_other_files_file_description__horizontalLayout_" + str(self.AI_num))

        tmp_AI_other_files_file_description__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_description__label_1.setObjectName(
            "AI_other_files_file_description__label_" + str(self.AI_num))
        tmp_AI_other_files_file_description__label_1.setText("파일 설명: ")
        tmp_AI_other_files_file_description__horizontalLayout_1.addWidget(
            tmp_AI_other_files_file_description__label_1)

        tmp_AI_other_files_file_description__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_description__lineEdit_1.setObjectName(
            "AI_other_files_file_description__lineEdit_" + str(self.AI_num))
        tmp_AI_other_files_file_description__horizontalLayout_1.addWidget(
            tmp_AI_other_files_file_description__lineEdit_1)

        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_description__horizontalLayout_1)
        tmp_AI_other_files_file_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_metadata__horizontalLayout_1.setObjectName(
            "AI_other_files_file_metadata__horizontalLayout_" + str(self.AI_num))

        tmp_AI_other_files_file_metadata__label_1 = QtWidgets.QLabel(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_metadata__label_1.setObjectName(
            "AI_other_files_file_metadata__label_" + str(self.AI_num))
        tmp_AI_other_files_file_metadata__label_1.setText("파일 메타데이터: ")
        tmp_AI_other_files_file_metadata__horizontalLayout_1.addWidget(tmp_AI_other_files_file_metadata__label_1)

        tmp_AI_other_files_file_metadata__lineEdit_1 = QtWidgets.QLineEdit(self.AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_metadata__lineEdit_1.setObjectName(
            "AI_other_files_file_metadata__lineEdit_" + str(self.AI_num))
        tmp_AI_other_files_file_metadata__horizontalLayout_1.addWidget(tmp_AI_other_files_file_metadata__lineEdit_1)

        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_metadata__horizontalLayout_1)
        self.gridLayout_11.addLayout(tmp_AI_other_files__verticalLayout_1, self.AI_num, 0, 1, 1)

        tmp_list = list()
        tmp_list.append(tmp_AI_other_files_file_browse__lineEdit_1)
        tmp_list.append(tmp_AI_other_files_id__lineEdit_1)
        tmp_list.append(tmp_AI_other_files_type__lineEdit_1)
        tmp_list.append(tmp_AI_other_files_file_size__lineEdit_1)
        tmp_list.append(tmp_AI_other_files_file_path__lineEdit_1)
        tmp_list.append(tmp_AI_other_files_file_hash_type__lineEdit_1)
        tmp_list.append(tmp_AI_other_files_file_hash_value__lineEdit_1)
        tmp_list.append(tmp_AI_other_files_file_description__lineEdit_1)
        tmp_list.append(tmp_AI_other_files_file_metadata__lineEdit_1)
        self.AI_List.append(tmp_list)

        ##self.AI_other_files_Button_num = 1
        ##self.AI_other_files_Button_List = list()
        tmp_list = list()
        tmp_list.append(tmp_AI_other_files_file_browse__browseButton_1)
        tmp_list.append(tmp_AI_other_files_file_browse__enterButton_1)
        self.AI_other_files_Button_List.append(tmp_list)

        tmp_AI_other_files_type__lineEdit_1.setReadOnly(True)
        tmp_AI_other_files_file_size__lineEdit_1.setReadOnly(True)
        tmp_AI_other_files_file_path__lineEdit_1.setReadOnly(True)
        tmp_AI_other_files_file_hash_type__lineEdit_1.setReadOnly(True)
        tmp_AI_other_files_file_hash_value__lineEdit_1.setReadOnly(True)
        tmp_AI_other_files_file_metadata__lineEdit_1.setReadOnly(False)

    ## AI other file Browse...버튼 클릭하면 파일 업로드
    def AI_other_files_file_browse__browseButton_1_QFileDialog(self, a):
        file_name = QFileDialog.getOpenFileName()
        self.AI_List[a][0].setText(file_name[0])

    ## AI other file Enter 클릭하면 파일 계산
    def AI_other_files_file_browse__enterButton_1_Calculate(self, a):
        file_path = self.AI_List[a][0].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\분석 정보\\기타 파일\\" + file_name
        if os.path.isdir(".\\분석 정보\\기타 파일") == False:
            os.makedirs(".\\분석 정보\\기타 파일")
        copyfile(file_path, copy_file_path)

        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)

            file_size = os.path.getsize(copy_file_path)

            #'"' + file_name + '"'

            image = Image.open(file_name)

            info = image._getexif();
            image.close()

            taglabel = {}

            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                taglabel[decoded] = value

            exifGPS = taglabel['GPSInfo']

            Latitude = "위도: " + str(int(exifGPS[2][0])) + "°" + str(int(exifGPS[2][1])) + "'" + str(int(exifGPS[2][2])) + exifGPS[1]
            Longtitude = "경도: " + str(int(exifGPS[4][0])) + "°" + str(int(exifGPS[4][1])) + "'" + str(int(exifGPS[4][2])) + exifGPS[3]

            Altitude = "고도: " + str(int(exifGPS[6]))

            # 해상도 단위
            Hesang = "해상도 단위: " + str(info[296])

            # 카메라 제조업체
            CamManufacturerer = "카메라 제조업체: " + str(info[271])

            # 카메라 모델
            CamModel = "카메라 모델: " + str(info[272])

            # 프로그램 이름
            Program_Name = "프로그램 이름: " + str(info[305])

            # 찍은 날짜
            Photo_Taken_Date = "찍은 날짜: " + str(info[306])



            # 수평 해상도
            Horizontal_Hesang = "수평 해상도: " + str(info[282])

            # 수직 해상도
            Vertical_Hesang = "수직 해상도: " + str(info[283])

            # EXIF 버젼
            EXIF_version = "EXIF 버젼: " + str(info[36864])

            # 조리개 최대 개방
            jori_max_open = "조리개 최대 개방: " + str(info[37378])

            # 노출 바이러스
            exposure_virus = "노출 바이러스: " + str(info[37379])

            # 밝기
            brightness = "밝기: " + str(info[37380])

            # 너비
            width = "너비: " + str(info[40962])

            # 높이
            height = "높이: " + str(info[40963])

            # F 스톱
            F_stop = "F 스톱: " + str(info[33437])

            # ISO 감도
            iso = "ISO 감도: " + str(info[34855])

            result = Latitude, Longtitude, Altitude, Hesang, CamManufacturerer, CamModel, Program_Name, Photo_Taken_Date, Horizontal_Hesang, Vertical_Hesang, EXIF_version, jori_max_open, exposure_virus, brightness, width, height, F_stop, iso



            # 0                                                  #파일 입력
            # 1                                                  #고유번호
        self.AI_List[a][2].setText(file_name[file_name.rfind(".") + 1:])  # 파일 유형
        self.AI_List[a][3].setText(str(file_size))  # 파일 크기
        self.AI_List[a][4].setText(copy_file_path)  # 파일 경로
        self.AI_List[a][5].setText("SHA-256")  # 해시 종류
        self.AI_List[a][6].setText(sha256.hexdigest())  # 해시값
        self.AI_List[a][8].setText(str(result)) # 메타데이터



    ## AI Equipment Traces +버튼 누르면 EquipmentTraces Add
    def AI_EquipmentTraces__addButton_AddAIEquipmentTraces(self):
        self.AI_EquipmentTraces_num += 2

        tmp_AI_EquipmentTraces__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_AI_EquipmentTraces__verticalLayout_1.setObjectName(
            "AI_EquipmentTraces__verticalLayout_" + str(self.AI_EquipmentTraces_num))

        tmp = QtWidgets.QFrame(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp.setFrameShape(QtWidgets.QFrame.HLine)
        tmp.setFrameShadow(QtWidgets.QFrame.Sunken)
        tmp_AI_EquipmentTraces__verticalLayout_1.addWidget(tmp)

        tmp_AI_EquipmentTraces_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_id__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_id__horizontalLayout_-" + str(self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_id__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_id__label_1.setObjectName(
            "AI_EquipmentTraces_id__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_id__label_1.setText("고유번호: ")
        tmp_AI_EquipmentTraces_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_id__label_1)

        tmp_AI_EquipmentTraces_id__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_EquipmentTraces__scrollAreaWidgetContents_1)

        tmp_AI_EquipmentTraces_id__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_id__lineEdit_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_id__lineEdit_1)

        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_id__horizontalLayout_1)
        tmp_AI_EquipmentTraces_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_type__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_type__horizontalLayout_-" + str(self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_type__label_1 = QtWidgets.QLabel(self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_type__label_1.setObjectName(
            "AI_EquipmentTraces_type__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_type__label_1.setText("유형: ")
        tmp_AI_EquipmentTraces_type__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_type__label_1)

        tmp_AI_EquipmentTraces_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_type__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_type__lineEdit_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_type__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_type__lineEdit_1)

        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_type__horizontalLayout_1)
        tmp_AI_EquipmentTraces_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_description__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_description__horizontalLayout_-" + str(self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_description__label_1 = QtWidgets.QLabel(
            self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_description__label_1.setObjectName(
            "AI_EquipmentTraces_description__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_description__label_1.setText("유형 설명: ")
        tmp_AI_EquipmentTraces_description__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_description__label_1)

        tmp_AI_EquipmentTraces_description__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_description__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_description__lineEdit_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_description__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_description__lineEdit_1)

        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_description__horizontalLayout_1)
        tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_mgmt_id__horizontalLayout_-" + str(self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_mgmt_id__label_1 = QtWidgets.QLabel(
            self.AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_mgmt_id__label_1.setObjectName(
            "AI_EquipmentTraces_mgmt_id__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_mgmt_id__label_1.setText("장비 아이디: ")
        tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_mgmt_id__label_1)

        tmp_AI_EquipmentTraces_mgmt_id__lineEdit_1 = QtWidgets.QLineEdit()
        tmp_AI_EquipmentTraces_mgmt_id__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_mgmt_id__lineEdit_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_mgmt_id__lineEdit_1)

        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1)
        tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_vessel_id__horizontalLayout_-" + str(self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_vessel_id__label_1 = QtWidgets.QLabel()
        tmp_AI_EquipmentTraces_vessel_id__label_1.setObjectName(
            "AI_EquipmentTraces_vessel_id__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_vessel_id__label_1.setText("선박 고유번호: ")
        tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_vessel_id__label_1)

        tmp_AI_EquipmentTraces_vessel_id__lineEdit_1 = QtWidgets.QLineEdit()
        tmp_AI_EquipmentTraces_vessel_id__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_vessel_id__lineEdit_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_vessel_id__lineEdit_1)

        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1)
        tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_evidence_id__horizontalLayout_-" + str(self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_evidence_id__label_1 = QtWidgets.QLabel()
        tmp_AI_EquipmentTraces_evidence_id__label_1.setObjectName(
            "AI_EquipmentTraces_evidence_id__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_evidence_id__label_1.setText("증거 고유번호: ")
        tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_evidence_id__label_1)

        tmp_AI_EquipmentTraces_evidence_id__lineEdit_1 = QtWidgets.QLineEdit()
        tmp_AI_EquipmentTraces_evidence_id__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_evidence_id__lineEdit_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_evidence_id__lineEdit_1)

        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info__horizontalLayout_-" + str(self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info__label_1 = QtWidgets.QLabel()
        tmp_AI_EquipmentTraces_user_trace_info__label_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info__label_1.setText("사용자 추적 정보")
        tmp_AI_EquipmentTraces_user_trace_info__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info__label_1)

        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_trace_info__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_-" + str(self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1 = QtWidgets.QScrollArea()
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1.setWidgetResizable(True)
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1.setObjectName(
            "AI_EquipmentTraces_user_traces_info_sub__scrollArea_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1 = QtWidgets.QWidget()

        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1.setGeometry(
            QtCore.QRect(0, 0, 371, 257))
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1.setObjectName(
            "AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_-" + str(
                self.AI_EquipmentTraces_num))
        tmp_gridLayout_14 = QtWidgets.QGridLayout(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_gridLayout_14.setObjectName("gridLayout_14")

        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_traces_info_sub__verticalLayout_-" + str(self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_-" + str(
                self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1 = QtWidgets.QLabel(
            self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_power_on_time__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1.setText("시스템 시작 시간: ")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1)

        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1 = QtWidgets.QLineEdit(
            self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_-" + str(
                self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1)

        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_-" + str(
                self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1 = QtWidgets.QLabel(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_-" + str(
                self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1.setText("항적 추출 방법: ")
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1)

        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_-" + str(
                self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1)

        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_-" + str(
                self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info_system_description__label_1 = QtWidgets.QLabel(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_description__label_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_description__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_system_description__label_1.setText("시스템 설명: ")
        tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_system_description__label_1)

        tmp_AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_description__lineEdit_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1)

        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_-" + str(
                self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__label_1 = QtWidgets.QLabel(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__label_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_operation_status__label_-" + str(
                self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__label_1.setText("시스템 운영 상태: ")
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__label_1)

        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_-" + str(
                self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1)

        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_-" + str(
                self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1 = QtWidgets.QLabel(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_power_off_time__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1.setText("시스템 종료 시간: ")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1)

        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_-" + str(
                self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1)

        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_-" + str(
                self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__label_1 = QtWidgets.QLabel(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__label_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_track_recording_period__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__label_1.setText("항적 기록 시간: ")
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__label_1)

        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_-" + str(
                self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1)

        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_-" + str(
                self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1 = QtWidgets.QLabel(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1.setText("항적 삭제 개수: ")
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1)

        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_-" + str(
                self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1)

        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_-" + str(
                self.AI_EquipmentTraces_num))

        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1 = QtWidgets.QLabel(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_user_trace_notes__label_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1.setText("비고: ")
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1)

        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1.setObjectName(
            "AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_-" + str(self.AI_EquipmentTraces_num))
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1)

        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1)
        tmp_gridLayout_14.addLayout(tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1, 0, 0, 1, 1)

        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1.setWidget(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1.addWidget(
            tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1)

        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(
            tmp_AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1)
        self.gridLayout_19.addLayout(tmp_AI_EquipmentTraces__verticalLayout_1, self.AI_EquipmentTraces_num, 0, 2, 2)

        tmp_list = list()
        tmp_list.append(tmp_AI_EquipmentTraces_id__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_type__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_description__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_mgmt_id__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_vessel_id__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_evidence_id__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1)
        tmp_list.append(tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1)
        self.AI_EquipmentTraces_List.append(tmp_list)

    ##<DEPL>

    ## DEPL +누르면 Add DEPL전체
    def DEPL__addButton_AddDEPL(self):
        self.DEPL_num += 1

        tmp_DEPL__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DEPL__verticalLayout_1.setObjectName("DEPL__verticalLayout_" + str(self.DEPL_num))

        tmp = QtWidgets.QFrame(self.scrollAreaWidgetContents_12)
        tmp.setFrameShape(QtWidgets.QFrame.HLine)
        tmp.setFrameShadow(QtWidgets.QFrame.Sunken)
        tmp_DEPL__verticalLayout_1.addWidget(tmp)

        tmp_DEPL_digital_evidence_package_management_id___horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DEPL_digital_evidence_package_management_id___horizontalLayout_1.setObjectName(
            "DEPL_digital_evidence_package_management_id___horizontalLayout_" + str(self.DEPL_num))
        tmp_DEPL_digital_evidence_package_management_id__label_1 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_12)
        tmp_DEPL_digital_evidence_package_management_id__label_1.setObjectName(
            "DEPL_digital_evidence_package_management_id__label_" + str(self.DEPL_num))
        tmp_DEPL_digital_evidence_package_management_id__label_1.setText("디지털 증거 패키지 고유번호: ")
        tmp_DEPL_digital_evidence_package_management_id___horizontalLayout_1.addWidget(
            tmp_DEPL_digital_evidence_package_management_id__label_1)
        tmp_DEPL_digital_evidence_package_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_12)
        tmp_DEPL_digital_evidence_package_management_id__lineEdit_1.setObjectName(
            "DEPL_digital_evidence_package_management_id__lineEdit_" + str(self.DEPL_num))
        tmp_DEPL_digital_evidence_package_management_id___horizontalLayout_1.addWidget(
            tmp_DEPL_digital_evidence_package_management_id__lineEdit_1)
        tmp_DEPL__verticalLayout_1.addLayout(tmp_DEPL_digital_evidence_package_management_id___horizontalLayout_1)
        tmp_DEPL_log_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DEPL_log_datetime__horizontalLayout_1.setObjectName(
            "DEPL_log_datetime__horizontalLayout_" + str(self.DEPL_num))
        tmp_DEPL_log_datetime__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        tmp_DEPL_log_datetime__label_1.setObjectName("DEPL_log_datetime__label_" + str(self.DEPL_num))
        tmp_DEPL_log_datetime__label_1.setText("이력 기록 시간: ")
        tmp_DEPL_log_datetime__horizontalLayout_1.addWidget(tmp_DEPL_log_datetime__label_1)
        tmp_DEPL_log_datetime__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        tmp_DEPL_log_datetime__lineEdit_1.setObjectName("DEPL_log_datetime__lineEdit_" + str(self.DEPL_num))
        tmp_DEPL_log_datetime__horizontalLayout_1.addWidget(tmp_DEPL_log_datetime__lineEdit_1)
        tmp_DEPL__verticalLayout_1.addLayout(tmp_DEPL_log_datetime__horizontalLayout_1)
        tmp_DEPL_log_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DEPL_log_type__horizontalLayout_1.setObjectName("DEPL_log_type__horizontalLayout_" + str(self.DEPL_num))
        tmp_DEPL_log_type__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        tmp_DEPL_log_type__label_1.setObjectName("DEPL_log_type__label_" + str(self.DEPL_num))
        tmp_DEPL_log_type__label_1.setText("이력 유형: ")
        tmp_DEPL_log_type__horizontalLayout_1.addWidget(tmp_DEPL_log_type__label_1)
        tmp_DEPL_log_type__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        tmp_DEPL_log_type__lineEdit_1.setObjectName("DEPL_log_type__lineEdit_" + str(self.DEPL_num))
        tmp_DEPL_log_type__horizontalLayout_1.addWidget(tmp_DEPL_log_type__lineEdit_1)
        tmp_DEPL__verticalLayout_1.addLayout(tmp_DEPL_log_type__horizontalLayout_1)
        tmp_DEPL_log_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DEPL_log_description__horizontalLayout_1.setObjectName(
            "DEPL_log_description__horizontalLayout_" + str(self.DEPL_num))
        tmp_DEPL_log_description__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        tmp_DEPL_log_description__label_1.setObjectName("DEPL_log_description__label_" + str(self.DEPL_num))
        tmp_DEPL_log_description__label_1.setText("이력 설명: ")
        tmp_DEPL_log_description__horizontalLayout_1.addWidget(tmp_DEPL_log_description__label_1)
        tmp_DEPL_log_description__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        tmp_DEPL_log_description__lineEdit_1.setObjectName("DEPL_log_description__lineEdit_" + str(self.DEPL_num))
        tmp_DEPL_log_description__horizontalLayout_1.addWidget(tmp_DEPL_log_description__lineEdit_1)
        tmp_DEPL__verticalLayout_1.addLayout(tmp_DEPL_log_description__horizontalLayout_1)
        tmp_DEPL_devision_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DEPL_devision_name_of_logger__horizontalLayout_1.setObjectName(
            "DEPL_devision_name_of_logger__horizontalLayout_" + str(self.DEPL_num))
        tmp_DEPL_devision_name_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        tmp_DEPL_devision_name_of_logger__label_1.setObjectName(
            "DEPL_devision_name_of_logger__label_" + str(self.DEPL_num))
        tmp_DEPL_devision_name_of_logger__label_1.setText("이력 분석 조직명: ")
        tmp_DEPL_devision_name_of_logger__horizontalLayout_1.addWidget(tmp_DEPL_devision_name_of_logger__label_1)
        tmp_DEPL_devision_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        tmp_DEPL_devision_name_of_logger__lineEdit_1.setObjectName(
            "DEPL_devision_name_of_logger__lineEdit_" + str(self.DEPL_num))
        tmp_DEPL_devision_name_of_logger__horizontalLayout_1.addWidget(tmp_DEPL_devision_name_of_logger__lineEdit_1)
        tmp_DEPL__verticalLayout_1.addLayout(tmp_DEPL_devision_name_of_logger__horizontalLayout_1)
        tmp_DEPL_team_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DEPL_team_name_of_logger__horizontalLayout_1.setObjectName(
            "DEPL_team_name_of_logger__horizontalLayout_" + str(self.DEPL_num))
        tmp_DEPL_team_name_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        tmp_DEPL_team_name_of_logger__label_1.setObjectName("DEPL_team_name_of_logger__label_" + str(self.DEPL_num))
        tmp_DEPL_team_name_of_logger__label_1.setText("이력 분석 팀명: ")
        tmp_DEPL_team_name_of_logger__horizontalLayout_1.addWidget(tmp_DEPL_team_name_of_logger__label_1)
        tmp_DEPL_team_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        tmp_DEPL_team_name_of_logger__lineEdit_1.setObjectName(
            "DEPL_team_name_of_logger__lineEdit_" + str(self.DEPL_num))
        tmp_DEPL_team_name_of_logger__horizontalLayout_1.addWidget(tmp_DEPL_team_name_of_logger__lineEdit_1)
        tmp_DEPL__verticalLayout_1.addLayout(tmp_DEPL_team_name_of_logger__horizontalLayout_1)
        tmp_DEPL_rank_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DEPL_rank_of_logger__horizontalLayout_1.setObjectName(
            "DEPL_rank_of_logger__horizontalLayout_" + str(self.DEPL_num))
        tmp_DEPL_rank_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        tmp_DEPL_rank_of_logger__label_1.setObjectName("DEPL_rank_of_logger__label_" + str(self.DEPL_num))
        tmp_DEPL_rank_of_logger__label_1.setText("이력 분석자 계급: ")
        tmp_DEPL_rank_of_logger__horizontalLayout_1.addWidget(tmp_DEPL_rank_of_logger__label_1)
        tmp_DEPL_rank_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        tmp_DEPL_rank_of_logger__lineEdit_1.setObjectName("DEPL_rank_of_logger__lineEdit_" + str(self.DEPL_num))
        tmp_DEPL_rank_of_logger__horizontalLayout_1.addWidget(tmp_DEPL_rank_of_logger__lineEdit_1)
        tmp_DEPL__verticalLayout_1.addLayout(tmp_DEPL_rank_of_logger__horizontalLayout_1)
        tmp_DEPL_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DEPL_name_of_logger__horizontalLayout_1.setObjectName(
            "DEPL_name_of_logger__horizontalLayout_" + str(self.DEPL_num))
        tmp_DEPL_name_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        tmp_DEPL_name_of_logger__label_1.setObjectName("DEPL_name_of_logger__label_" + str(self.DEPL_num))
        tmp_DEPL_name_of_logger__label_1.setText("이력 분석자명: ")
        tmp_DEPL_name_of_logger__horizontalLayout_1.addWidget(tmp_DEPL_name_of_logger__label_1)
        tmp_DEPL_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        tmp_DEPL_name_of_logger__lineEdit_1.setObjectName("DEPL_name_of_logger__lineEdit_" + str(self.DEPL_num))
        tmp_DEPL_name_of_logger__horizontalLayout_1.addWidget(tmp_DEPL_name_of_logger__lineEdit_1)
        tmp_DEPL__verticalLayout_1.addLayout(tmp_DEPL_name_of_logger__horizontalLayout_1)
        self.gridLayout_16.addLayout(tmp_DEPL__verticalLayout_1, self.DEPL_num, 0, 1, 1)

        tmp_list = list()
        tmp_list.append(tmp_DEPL_digital_evidence_package_management_id__lineEdit_1)
        tmp_list.append(tmp_DEPL_log_datetime__lineEdit_1)
        tmp_list.append(tmp_DEPL_log_type__lineEdit_1)
        tmp_list.append(tmp_DEPL_log_description__lineEdit_1)
        tmp_list.append(tmp_DEPL_devision_name_of_logger__lineEdit_1)
        tmp_list.append(tmp_DEPL_team_name_of_logger__lineEdit_1)
        tmp_list.append(tmp_DEPL_rank_of_logger__lineEdit_1)
        tmp_list.append(tmp_DEPL_name_of_logger__lineEdit_1)
        self.DEPL_List.append(tmp_list)

        tmp_DEPL_log_datetime__lineEdit_1.setReadOnly(True)



    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.ExportButton.setText(_translate("SecondWindow", "Export"))
        self.Digital_Evidence_Package.setText(_translate("SecondWindow", "Digital Evidence Package"))
        self.Case_Info.setText(_translate("SecondWindow", "사건 정보"))
        self.case_management_id__label.setText(_translate("SecondWindow", "사건 관리 번호:"))
        self.contents_of_request__label.setText(_translate("SecondWindow", "요청사항:"))
        self.agency_case_no__label.setText(_translate("SecondWindow", "기관 사건 번호:"))
        self.ordering_datetime__label.setText(_translate("SecondWindow", "사건 의뢰 시각:"))
        self.case_summary__label.setText(_translate("SecondWindow", "사건 요약:"))
        self.case_datetime__label.setText(_translate("SecondWindow", "사건 발생 시각:"))
        self.agency_organization_code__label.setText(_translate("SecondWindow", "기관 코드:"))
        self.agency_organization_name__labe.setText(_translate("SecondWindow", "기관명:"))
        self.case_description__label.setText(_translate("SecondWindow", "사건 설명:"))
        self.agency_organization_party_name__label.setText(_translate("SecondWindow", "부서명:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Case_Info_tab), _translate("SecondWindow", "Case Info"))
        self.DE__addButton.setText(_translate("SecondWindow", "+"))
        self.DE_Digitlal_Evidence__label.setText(_translate("SecondWindow", "디지털 증거"))
        self.DE_management_id__label_1.setText(_translate("SecondWindow", "관리 번호:"))
        self.DE_digital_evidence_type__label_1.setText(_translate("SecondWindow", "디지털 증거 유형:"))
        self.DE_evidences_gathering_type__label_1.setText(_translate("SecondWindow", "증거 채증 유형:"))
        self.DE_Vessel_Info__label_1.setText(_translate("SecondWindow", "   선박 정보"))
        self.DE_Marine_Electronics_Info__label_1.setText(_translate("SecondWindow", "   해양 장비 정보"))
        self.DE_other_files__label_1.setText(_translate("SecondWindow", "   기타 파일(jpg, mp3, mp4, txt, avi 등"))
        self.DE_other_files__addButton_1.setText(_translate("SecondWindow", "+"))
        self.DE_Gather_Info__label_1.setText(_translate("SecondWindow", " 채증 정보"))
        self.DE_Gather_Info_gather_location__label_1.setText(_translate("SecondWindow", "채증 장소:"))
        self.DE_Gather_Info_gather_person_name__label_1.setText(_translate("SecondWindow", "채증 담당자:"))
        self.DE_Gather_Info_gather_datetime__label_1.setText(_translate("SecondWindow", "채증 시간:"))
        self.DE_Gather_Info_gather_person_agency__label_1.setText(_translate("SecondWindow", "채증 기관:"))
        self.DE_Gather_Info_gather_person_rank__label_1.setText(_translate("SecondWindow", "채증 담당자 계급:"))
        self.DE_Gather_Info_submitter_name__label_1.setText(_translate("SecondWindow", "피압수자:"))
        self.DE_Gather_Info__addButton_1.setText(_translate("SecondWindow", "+"))
        self.DE_Gather_Info_file__filebrowse__label_1.setText(_translate("SecondWindow", "파일 입력"))
        self.DE_Gather_Info_file__filebrowse__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.DE_Gather_Info_file__filebrowse__enterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.DE_Gather_Info_gather_media_type__label_1.setText(_translate("SecondWindow", "채증 미디어 유형:"))
        self.DE_Gather_Info__gather_hash_type__label_1.setText(_translate("SecondWindow", "채증 미디어 해시 종류:"))
        self.DE_Gather_Info_gather_hash__label_1.setText(_translate("SecondWindow", "채증 미디어 해시값:"))
        self.DE_Gather_Info_gather_path__label_1.setText(_translate("SecondWindow", "채증 미디어 경로:"))
        self.DE_Acquisition_Info_acquisition_person_name__label_1.setText(_translate("SecondWindow", "수집자명:"))
        self.DE_Acquisition_Info_acquisition_date_time__label_1.setText(_translate("SecondWindow", "수집 시간:"))
        self.DE_Acquisition_Info_acquisition_location__label_1.setText(_translate("SecondWindow", "수집 장소:"))
        self.DE_Acquisition_Info_acquisition_tool__label_1.setText(_translate("SecondWindow", "수집 도구:"))
        self.DE_Acquisition_Info__addButton_1.setText(_translate("SecondWindow", "+"))
        self.DE_Acquisition_Info_file_browse__label_1.setText(_translate("SecondWindow", "파일입력:"))
        self.DE_Acquisition_Info_file_browse__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.DE_Acquisition_Info_file_browse__enterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.DE_Acquisition_Info_digital_evidence_file_name__label_1.setText(_translate("SecondWindow", "디지털 증거 파일 이름:"))
        self.DE_Acquisition_Info_digital_evidence_file_path__label_1.setText(_translate("SecondWindow", "디지털 증거 파일 경로:"))
        self.DE_Acquisition_Info_hash_type__label_1.setText(_translate("SecondWindow", "해시 종류:"))
        self.DE_Acquisition_Info_hash_value__label_1.setText(_translate("SecondWindow", "해시값:"))
        self.DE_Vessel_Info_vessel_name__label_1.setText(_translate("SecondWindow", "선박 이름:"))
        self.DE_Vessel_Info_vessel_management_id__label_1.setText(_translate("SecondWindow", "선박 관리 고유 번호:"))
        self.DE_Vessel_Info_vessel_MMSI__label_1.setText(_translate("SecondWindow", "선박 MMSI:"))
        self.DE_Vessel_Info_vessel_callsign__label_1.setText(_translate("SecondWindow", "선박 callsign:"))
        self.DE_Vessel_Info_vessel_IMO__label_1.setText(_translate("SecondWindow", "선박 IMO:"))
        self.DE_Vessel_Info_vessel_MRN__label_1.setText(_translate("SecondWindow", "선박 MRN:"))
        self.DE_Vessel_Info_vessel_tonnage__label_1.setText(_translate("SecondWindow", "선박 톤수:"))
        self.DE_Vessel_Info_vessel_length__label_1.setText(_translate("SecondWindow", "선박 길이:"))
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1.setText(_translate("SecondWindow", "항적 분석 장비 수:"))
        self.DE_Acquisition_Info__label_1.setText(_translate("SecondWindow", " 수집 정보"))
        self.DE_Marines_Electronics_Info_device_management_id__label_1.setText(_translate("SecondWindow", "장비 관리 고유 번호:"))
        self.DE_Marines_Electronics_Info_device_type__label_1.setText(_translate("SecondWindow", "장비 유형:"))
        self.DE_Marines_Electronics_Info_device_manufacturer__label_1.setText(_translate("SecondWindow", "장비 제조사:"))
        self.DE_Marines_Electronics_Info_device_model_name__label_1.setText(_translate("SecondWindow", "장비 모델명:"))
        self.DE_Marines_Electronics_Info_device_model_serial_number__label_1.setText(_translate("SecondWindow", "장비 모델 시리얼 넘버:"))
        self.DE_Marines_Electronics_Info_device_os_firmware__label_1.setText(_translate("SecondWindow", "장비 os firmware:"))
        self.DE_Marines_Electronics_Info_device_description__label_1.setText(_translate("SecondWindow", "장비 설명:"))
        self.DE_other_files_file_browse__label_1.setText(_translate("SecondWindow", "파일 입력:"))
        self.DE_other_files_file_browse__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.DE_other_files_file_browse__EnterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.DE_other_files_id__label_1.setText(_translate("SecondWindow", "고유번호:"))
        self.DE_other_files_type__label_1.setText(_translate("SecondWindow", "파일유형: "))
        self.DE_other_files_file_size__label_1.setText(_translate("SecondWindow", "파일크기: "))
        self.DE_other_files_file_path__label_1.setText(_translate("SecondWindow", "파일 경로: "))
        self.DE_other_files_file_hash_type__label_1.setText(_translate("SecondWindow", "해시 종류: "))
        self.DE_other_files_file_hash_value__label_1.setText(_translate("SecondWindow", "해시값: "))
        self.DE_other_files_file_description__label_1.setText(_translate("SecondWindow", "파일 설명: "))
        self.DE_other_files_file_metadata__label_1.setText(_translate("SecondWindow", "파일 메타데이터: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DE_tab), _translate("SecondWindow", "Digital Evidences"))
        self.AI_title__label.setText(_translate("SecondWindow", "분석 정보"))
        self.AI_Reports_id__label_1.setText(_translate("SecondWindow", "고유번호:"))
        self.AI_Reports_type__label_1.setText(_translate("SecondWindow", "유형:"))
        self.AI_Reports_subtype__label_1.setText(_translate("SecondWindow", "하위유형:"))
        self.AI_Reports_mgmt_id__label_1.setText(_translate("SecondWindow", "장비 고유번호:"))
        self.AI_Reports_submission_agency__label_1.setText(_translate("SecondWindow", "제출 기관:"))
        self.AI_Reports_reprot_creation_datetime__label_1.setText(_translate("SecondWindow", "보고서 작성 시간:"))
        self.AI_Reports_division_name_of_report_maker__label_1.setText(_translate("SecondWindow", "보고서 작성 부서명:"))
        self.AI_Reports_team_name_of_report_maker__label_1.setText(_translate("SecondWindow", "보고서 작성 팀명:"))
        self.AI_Reports_file_info__label_1.setText(_translate("SecondWindow", "파일 정보"))
        self.AI_Reports_file_info__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.AI_Reports_file_info__enterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.AI_Reports_file_name__label_1.setText(_translate("SecondWindow", "파일 이름:"))
        self.AI_Reports_file_size__label_1.setText(_translate("SecondWindow", "파일 크기:"))
        self.AI_Reports_file_path__label_1.setText(_translate("SecondWindow", "파일 경로:"))
        self.AI_Reports_file_creation_datetime__label_1.setText(_translate("SecondWindow", "파일 생성 날짜/시간"))
        self.AI_Reports_file_description__label_1.setText(_translate("SecondWindow", "파일 설명:"))
        self.AI_Reports_file_hash_type__label_1.setText(_translate("SecondWindow", "파일 해시 종류:"))
        self.AI_Reports_file_hash_value__label_1.setText(_translate("SecondWindow", "파일 해시 값:"))
        self.AI_other_files_file_browse__label_1.setText(_translate("SecondWindow", "파일 입력"))
        self.AI_other_files_file_browse__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.AI_other_files_file_browse__enterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.AI_other_files_id__label_1.setText(_translate("SecondWindow", "고유번호:"))
        self.AI_other_files_type__label_1.setText(_translate("SecondWindow", "파일유형:"))
        self.AI_other_files_file_size__label_1.setText(_translate("SecondWindow", "파일크기:"))
        self.AI_other_files_file_path__label_1.setText(_translate("SecondWindow", "파일 경로:"))
        self.AI_other_files_file_hash_type__label_1.setText(_translate("SecondWindow", "해시종류:"))
        self.AI_other_files_file_hash_value__label_1.setText(_translate("SecondWindow", "해시값:"))
        self.AI_other_files_file_description__label_1.setText(_translate("SecondWindow", "파일 설명:"))
        self.AI_other_files_file_metadata__label_1.setText(_translate("SecondWindow", "파일 메타데이터:"))
        self.AI_EquipmentTraces__label.setText(_translate("SecondWindow", "Equipment Traces (장비별로)"))
        self.AI_EquipmentTraces__addButton.setText(_translate("SecondWindow", "+"))
        self.AI_EquipmentTraces_id__label_1.setText(_translate("SecondWindow", "고유번호:"))
        self.AI_EquipmentTraces_type__label_1.setText(_translate("SecondWindow", "유형:"))
        self.AI_EquipmentTraces_description__label_1.setText(_translate("SecondWindow", "유형 설명:"))
        self.AI_EquipmentTraces_mgmt_id__label_1.setText(_translate("SecondWindow", "장비 아이디:"))
        self.AI_EquipmentTraces_vessel_id__label_1.setText(_translate("SecondWindow", "선박 고유번호:"))
        self.AI_EquipmentTraces_evidence_id__label_1.setText(_translate("SecondWindow", "증거 고유번호"))
        self.AI_EquipmentTraces_user_trace_info__label_1.setText(_translate("SecondWindow", "사용자 추적 정보"))
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1.setText(_translate("SecondWindow", "시스템 시작 시간:"))
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1.setText(_translate("SecondWindow", "항적 추출 방법:"))
        self.AI_EquipmentTraces_user_trace_info_system_description__label_1.setText(_translate("SecondWindow", "시스템 설명:"))
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__label_1.setText(_translate("SecondWindow", "시스템 운영 상태:"))
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1.setText(_translate("SecondWindow", "시스템 종료 시간:"))
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__label_1.setText(_translate("SecondWindow", "항적 기록 시간:"))
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1.setText(_translate("SecondWindow", "항적 삭제 개수:"))
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1.setText(_translate("SecondWindow", "비고:"))
        self.AI_other_files__label_1.setText(_translate("SecondWindow", "기타 파일(jpg. mp3, mp4, txt, avi 등)"))
        self.AI_other_files__addButton.setText(_translate("SecondWindow", "+"))
        self.AI_Report__label.setText(_translate("SecondWindow", "보고서"))
        self.AI_Reports__addButton.setText(_translate("SecondWindow", "+"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AI_tab), _translate("SecondWindow", "Analysis info"))
        self.DEPL__addButton.setText(_translate("SecondWindow", "+"))
        self.DEPL_digital_evidence_package_management_id__label_1.setText(_translate("SecondWindow", "디지털 증거 패키지 고유번호:"))
        self.DEPL_log_datetime__label_1.setText(_translate("SecondWindow", "이력 기록 시간:"))
        self.DEPL_log_type__label_1.setText(_translate("SecondWindow", "이력 유형:"))
        self.DEPL_log_description__label_1.setText(_translate("SecondWindow", "이력 설명:"))
        self.DEPL_devision_name_of_logger__label_1.setText(_translate("SecondWindow", "이력 분석 조직명:"))
        self.DEPL_team_name_of_logger__label_1.setText(_translate("SecondWindow", "이력 분석 팀명:"))
        self.DEPL_rank_of_logger__label_1.setText(_translate("SecondWindow", "이력 분석자 계급:"))
        self.DEPL_name_of_logger__label_1.setText(_translate("SecondWindow", "이력 분석자명:"))
        self.DEPL_Digital_Evidence_Package_Log__label.setText(_translate("SecondWindow", "디지털 증거 패키지 로그"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DEPL_tab), _translate("SecondWindow", "Digital Evidence Package Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())