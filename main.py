import sys
from PyQt5.uic import loadUi
import datetime
import hashlib
import json
import os, time
import random
from PIL import Image
from PIL.ExifTags import TAGS
from shutil import copyfile
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QDialog, QApplication, QTabWidget, QWidget, QFileDialog, QMessageBox
from xml.etree.ElementTree import Element, SubElement, ElementTree

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
        # self.DE_Gather_Info_num = 1
        # self.DE_Gather_Info_List = list()
        # self.DE_Gather_Info_List.append(list())

        self.DE_Gather_Info_List = list()
        self.DE_Gather_Info_List.append(list())
        self.DE_Gather_Info_Button_List = list()
        self.DE_Gather_Info_Button_List.append(list())
        self.DE_Gather_Info_Tab_Widget_List = list()

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

        # DE 수집

        self.DE_Acquisition_Info_DEF_List = 1
        self.DE_Acquisition_Info_DEF_List = list()
        self.DE_Acquisition_Info_DEF_List.append(list())


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

        # Log 전체 add
        self.Log_num = 1
        self.Log_List = list()

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
        SecondWindow.resize(1400, 843)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.Digital_Evidence_Package = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Digital_Evidence_Package.setFont(font)
        self.Digital_Evidence_Package.setObjectName("Digital_Evidence_Package")
        self.gridLayout_28.addWidget(self.Digital_Evidence_Package, 0, 0, 1, 1)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1340, 665))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CI_left__verticalLayout = QtWidgets.QVBoxLayout()
        self.CI_left__verticalLayout.setObjectName("CI_left__verticalLayout")
        self.case_management_id__horizontalLayout = QtWidgets.QHBoxLayout()
        self.case_management_id__horizontalLayout.setObjectName("case_management_id__horizontalLayout")
        self.case_management_id__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.case_management_id__label.setObjectName("case_management_id__label")
        self.case_management_id__horizontalLayout.addWidget(self.case_management_id__label)
        self.case_management_id__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.case_management_id__lineEdit.setObjectName("case_management_id__lineEdit")
        self.case_management_id__horizontalLayout.addWidget(self.case_management_id__lineEdit)
        self.CI_left__verticalLayout.addLayout(self.case_management_id__horizontalLayout)
        self.agency_case_no__horizontalLayout = QtWidgets.QHBoxLayout()
        self.agency_case_no__horizontalLayout.setObjectName("agency_case_no__horizontalLayout")
        self.agency_case_no__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.agency_case_no__label.setObjectName("agency_case_no__label")
        self.agency_case_no__horizontalLayout.addWidget(self.agency_case_no__label)
        self.agency_case_no__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.agency_case_no__lineEdit.setObjectName("agency_case_no__lineEdit")
        self.agency_case_no__horizontalLayout.addWidget(self.agency_case_no__lineEdit)
        self.CI_left__verticalLayout.addLayout(self.agency_case_no__horizontalLayout)
        self.agency_organization_code__horizontalLayout = QtWidgets.QHBoxLayout()
        self.agency_organization_code__horizontalLayout.setObjectName("agency_organization_code__horizontalLayout")
        self.agency_organization_code__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.agency_organization_code__label.setObjectName("agency_organization_code__label")
        self.agency_organization_code__horizontalLayout.addWidget(self.agency_organization_code__label)
        self.agency_organization_code__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.agency_organization_code__lineEdit.setObjectName("agency_organization_code__lineEdit")
        self.agency_organization_code__horizontalLayout.addWidget(self.agency_organization_code__lineEdit)
        self.CI_left__verticalLayout.addLayout(self.agency_organization_code__horizontalLayout)
        self.agency_organization_name__horizontalLayout = QtWidgets.QHBoxLayout()
        self.agency_organization_name__horizontalLayout.setObjectName("agency_organization_name__horizontalLayout")
        self.agency_organization_name__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.agency_organization_name__label.setObjectName("agency_organization_name__label")
        self.agency_organization_name__horizontalLayout.addWidget(self.agency_organization_name__label)
        self.agency_organization_name__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.agency_organization_name__lineEdit.setObjectName("agency_organization_name__lineEdit")
        self.agency_organization_name__horizontalLayout.addWidget(self.agency_organization_name__lineEdit)
        self.CI_left__verticalLayout.addLayout(self.agency_organization_name__horizontalLayout)
        self.agency_organization_party_name__horizontalLayout = QtWidgets.QHBoxLayout()
        self.agency_organization_party_name__horizontalLayout.setObjectName("agency_organization_party_name__horizontalLayout")
        self.agency_organization_party_name__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.agency_organization_party_name__label.setObjectName("agency_organization_party_name__label")
        self.agency_organization_party_name__horizontalLayout.addWidget(self.agency_organization_party_name__label)
        self.agency_organization_party_name__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.agency_organization_party_name__lineEdit.setObjectName("agency_organization_party_name__lineEdit")
        self.agency_organization_party_name__horizontalLayout.addWidget(self.agency_organization_party_name__lineEdit)
        self.CI_left__verticalLayout.addLayout(self.agency_organization_party_name__horizontalLayout)
        self.gridLayout_2.addLayout(self.CI_left__verticalLayout, 0, 0, 1, 1)
        self.CI_right__verticalLayout = QtWidgets.QVBoxLayout()
        self.CI_right__verticalLayout.setObjectName("CI_right__verticalLayout")
        self.contents_of_request__horizontalLayout = QtWidgets.QHBoxLayout()
        self.contents_of_request__horizontalLayout.setObjectName("contents_of_request__horizontalLayout")
        self.contents_of_request__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.contents_of_request__label.setObjectName("contents_of_request__label")
        self.contents_of_request__horizontalLayout.addWidget(self.contents_of_request__label)
        self.contents_of_request__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.contents_of_request__lineEdit.setObjectName("contents_of_request__lineEdit")
        self.contents_of_request__horizontalLayout.addWidget(self.contents_of_request__lineEdit)
        self.CI_right__verticalLayout.addLayout(self.contents_of_request__horizontalLayout)
        self.case_summary__horizontalLayout = QtWidgets.QHBoxLayout()
        self.case_summary__horizontalLayout.setObjectName("case_summary__horizontalLayout")
        self.case_summary__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.case_summary__label.setObjectName("case_summary__label")
        self.case_summary__horizontalLayout.addWidget(self.case_summary__label)
        self.case_summary__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.case_summary__lineEdit.setObjectName("case_summary__lineEdit")
        self.case_summary__horizontalLayout.addWidget(self.case_summary__lineEdit)
        self.CI_right__verticalLayout.addLayout(self.case_summary__horizontalLayout)
        self.case_description__horizontalLayout = QtWidgets.QHBoxLayout()
        self.case_description__horizontalLayout.setObjectName("case_description__horizontalLayout")
        self.case_description__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.case_description__label.setObjectName("case_description__label")
        self.case_description__horizontalLayout.addWidget(self.case_description__label)
        self.case_description__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.case_description__lineEdit.setObjectName("case_description__lineEdit")
        self.case_description__horizontalLayout.addWidget(self.case_description__lineEdit)
        self.CI_right__verticalLayout.addLayout(self.case_description__horizontalLayout)
        self.case_datetime__horizontalLayout = QtWidgets.QHBoxLayout()
        self.case_datetime__horizontalLayout.setObjectName("case_datetime__horizontalLayout")
        self.case_datetime__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.case_datetime__label.setObjectName("case_datetime__label")
        self.case_datetime__horizontalLayout.addWidget(self.case_datetime__label)
        self.case_datetime__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.case_datetime__lineEdit.setObjectName("case_datetime__lineEdit")
        self.case_datetime__horizontalLayout.addWidget(self.case_datetime__lineEdit)
        self.CI_right__verticalLayout.addLayout(self.case_datetime__horizontalLayout)
        self.ordering_datetime__horizontalLayout = QtWidgets.QHBoxLayout()
        self.ordering_datetime__horizontalLayout.setObjectName("ordering_datetime__horizontalLayout")
        self.ordering_datetime__label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ordering_datetime__label.setObjectName("ordering_datetime__label")
        self.ordering_datetime__horizontalLayout.addWidget(self.ordering_datetime__label)
        self.ordering_datetime__lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ordering_datetime__lineEdit.setObjectName("ordering_datetime__lineEdit")
        self.ordering_datetime__horizontalLayout.addWidget(self.ordering_datetime__lineEdit)
        self.CI_right__verticalLayout.addLayout(self.ordering_datetime__horizontalLayout)
        self.gridLayout_2.addLayout(self.CI_right__verticalLayout, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Case_Info_tab, "")
        self.DE_tab = QtWidgets.QWidget()
        self.DE_tab.setObjectName("DE_tab")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.DE_tab)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.DE__addButton = QtWidgets.QPushButton(self.DE_tab)
        self.DE__addButton.setObjectName("DE__addButton")
        self.gridLayout_21.addWidget(self.DE__addButton, 0, 0, 1, 1)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.DE_tab)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.DE_Digitlal_Evidence__label = QtWidgets.QLabel(self.tab_2)
        self.DE_Digitlal_Evidence__label.setObjectName("DE_Digitlal_Evidence__label")
        self.gridLayout_26.addWidget(self.DE_Digitlal_Evidence__label, 0, 0, 1, 1)
        self.DE__scrollArea_1 = QtWidgets.QScrollArea(self.tab_2)
        self.DE__scrollArea_1.setWidgetResizable(True)
        self.DE__scrollArea_1.setObjectName("DE__scrollArea_1")
        self.DE__scrollAreaWidgetContents = QtWidgets.QWidget()
        self.DE__scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1308, 571))
        self.DE__scrollAreaWidgetContents.setObjectName("DE__scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.DE__scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.DE_Gather_Info__scrollArea_1 = QtWidgets.QScrollArea(self.DE__scrollAreaWidgetContents)
        self.DE_Gather_Info__scrollArea_1.setWidgetResizable(True)
        self.DE_Gather_Info__scrollArea_1.setObjectName("DE_Gather_Info__scrollArea_1")
        self.DE_Gather_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Gather_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -176, 372, 544))
        self.DE_Gather_Info__scrollAreaWidgetContents_1.setObjectName("DE_Gather_Info__scrollAreaWidgetContents_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.DE_Gather_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Gather_Info__verticalLayout_1.setObjectName("DE_Gather_Info__verticalLayout_1")
        self.DE_Gather_Info_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_no__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_no__horizontalLayout_1")
        self.DE_Gather_Info_gather_no__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_no__label_1.setObjectName("DE_Gather_Info_gather_no__label_1")
        self.DE_Gather_Info_gather_no__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_no__label_1)
        self.DE_Gather_Info_gather_no__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_no__lineEdit_1.setObjectName("DE_Gather_Info_gather_no__lineEdit_1")
        self.DE_Gather_Info_gather_no__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_no__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_no__horizontalLayout_1)
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
        self.DE_Gather_Info_organization_code__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_organization_code__horizontalLayout_1.setObjectName("DE_Gather_Info_organization_code__horizontalLayout_1")
        self.DE_Gather_Info_organization_code__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_organization_code__label_1.setObjectName("DE_Gather_Info_organization_code__label_1")
        self.DE_Gather_Info_organization_code__horizontalLayout_1.addWidget(self.DE_Gather_Info_organization_code__label_1)
        self.DE_Gather_Info_organization_code__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_organization_code__lineEdit_1.setObjectName("DE_Gather_Info_organization_code__lineEdit_1")
        self.DE_Gather_Info_organization_code__horizontalLayout_1.addWidget(self.DE_Gather_Info_organization_code__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_organization_code__horizontalLayout_1)
        self.DE_Gather_Info_submitter_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_submitter_name__horizontalLayout_1.setObjectName("DE_Gather_Info_submitter_name__horizontalLayout_1")
        self.DE_Gather_Info_submitter_name__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_submitter_name__label_1.setObjectName("DE_Gather_Info_submitter_name__label_1")
        self.DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(self.DE_Gather_Info_submitter_name__label_1)
        self.DE_Gather_Info_submitter_name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_submitter_name__lineEdit_1.setObjectName("DE_Gather_Info_submitter_name__lineEdit_1")
        self.DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(self.DE_Gather_Info_submitter_name__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_submitter_name__horizontalLayout_1)
        self.DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1.setObjectName("DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1")
        self.DE_Gather_Inf_Gather_Source_Name__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Inf_Gather_Source_Name__label_1.setObjectName("DE_Gather_Inf_Gather_Source_Name__label_1")
        self.DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1.addWidget(self.DE_Gather_Inf_Gather_Source_Name__label_1)
        self.DE_Gather_Inf_Gather_Source_Name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Inf_Gather_Source_Name__lineEdit_1.setObjectName("DE_Gather_Inf_Gather_Source_Name__lineEdit_1")
        self.DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1.addWidget(self.DE_Gather_Inf_Gather_Source_Name__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1)
        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1.setObjectName("DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1")
        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1.setObjectName("DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1")
        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1.addWidget(self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1)
        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1.setObjectName("DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1")
        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1.addWidget(self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1)
        self.gridLayout_3.addLayout(self.DE_Gather_Info__verticalLayout_1, 0, 0, 1, 1)
        self.tabWidget_9 = QtWidgets.QTabWidget(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.tabWidget_9.setObjectName("tabWidget_9")

        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.DE_Gather_Info_file__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_file__horizontalLayout_1.setObjectName("DE_Gather_Info_file__horizontalLayout_1")
        self.DE_Gather_Info_file__scrollArea_1 = QtWidgets.QScrollArea(self.tab_8)
        self.DE_Gather_Info_file__scrollArea_1.setWidgetResizable(True)
        self.DE_Gather_Info_file__scrollArea_1.setObjectName("DE_Gather_Info_file__scrollArea_1")
        self.DE_Gather_Info_file__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Gather_Info_file__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -139, 381, 219))
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
        self.DE_Gather_Info_gather_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_metadata__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_metadata__horizontalLayout_1")
        self.DE_Gather_Info_gather_metadata__label_1 = QtWidgets.QLabel(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_metadata__label_1.setObjectName("DE_Gather_Info_gather_metadata__label_1")
        self.DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_metadata__label_1)
        self.DE_Gather_Info_gather_metadata__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_metadata__lineEdit_1.setObjectName("DE_Gather_Info_gather_metadata__lineEdit_1")
        self.DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_metadata__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_metadata__horizontalLayout_1)
        self.gridLayout_18.addLayout(self.DE_Gather_Info_file__verticalLayout_1, 1, 0, 1, 1)
        self.DE_Gather_Info_file__scrollArea_1.setWidget(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__horizontalLayout_1.addWidget(self.DE_Gather_Info_file__scrollArea_1)
        self.gridLayout_27.addLayout(self.DE_Gather_Info_file__horizontalLayout_1, 0, 0, 1, 1)
        self.tabWidget_9.addTab(self.tab_8, "")

        self.gridLayout_3.addWidget(self.tabWidget_9, 2, 0, 1, 1)
        self.DE_Gather_Info_file_addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_file_addButton__horizontalLayout_1.setObjectName("DE_Gather_Info_file_addButton__horizontalLayout_1")
        self.DE_Gather_Info_file__blanklabel_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__blanklabel_1.setObjectName("DE_Gather_Info_file__blanklabel_1")
        self.DE_Gather_Info_file_addButton__horizontalLayout_1.addWidget(self.DE_Gather_Info_file__blanklabel_1)
        self.DE_Gather_Info__addButton_1 = QtWidgets.QPushButton(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info__addButton_1.setObjectName("DE_Gather_Info__addButton_1")
        self.DE_Gather_Info_file_addButton__horizontalLayout_1.addWidget(self.DE_Gather_Info__addButton_1)
        self.gridLayout_3.addLayout(self.DE_Gather_Info_file_addButton__horizontalLayout_1, 1, 0, 1, 1)
        self.DE_Gather_Info__scrollArea_1.setWidget(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.gridLayout_7.addWidget(self.DE_Gather_Info__scrollArea_1, 3, 1, 1, 1)
        self.DE_Vessel_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info__horizontalLayout_1.setObjectName("DE_Vessel_Info__horizontalLayout_1")
        self.DE_Vessel_Info__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_Vessel_Info__label_1.setObjectName("DE_Vessel_Info__label_1")
        self.DE_Vessel_Info__horizontalLayout_1.addWidget(self.DE_Vessel_Info__label_1)
        self.gridLayout_7.addLayout(self.DE_Vessel_Info__horizontalLayout_1, 0, 1, 1, 1)
        self.DE_Vessel_Info__scrollArea_1 = QtWidgets.QScrollArea(self.DE__scrollAreaWidgetContents)
        self.DE_Vessel_Info__scrollArea_1.setWidgetResizable(True)
        self.DE_Vessel_Info__scrollArea_1.setObjectName("DE_Vessel_Info__scrollArea_1")
        self.DE_Vessel_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Vessel_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 372, 329))
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
        self.DE_Vessel_Info_vessel_IMO__lineEdit_1.setPlaceholderText("")
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
        self.DE_Vessel_Type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Type__horizontalLayout_1.setObjectName("DE_Vessel_Type__horizontalLayout_1")
        self.DE_Vessel_Type__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Type__label_1.setObjectName("DE_Vessel_Type__label_1")
        self.DE_Vessel_Type__horizontalLayout_1.addWidget(self.DE_Vessel_Type__label_1)
        self.DE_Vessel_Type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Type__lineEdit_1.setObjectName("DE_Vessel_Type__lineEdit_1")
        self.DE_Vessel_Type__horizontalLayout_1.addWidget(self.DE_Vessel_Type__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Type__horizontalLayout_1)
        self.gridLayout_20.addLayout(self.DE_Vessel_Info__verticalLayout_1, 0, 0, 1, 1)
        self.DE_Vessel_Info__scrollArea_1.setWidget(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.gridLayout_7.addWidget(self.DE_Vessel_Info__scrollArea_1, 1, 1, 1, 1)
        self.DE_Marines_Electronics_Info__scrollArea_1 = QtWidgets.QScrollArea(self.DE__scrollAreaWidgetContents)
        self.DE_Marines_Electronics_Info__scrollArea_1.setWidgetResizable(True)
        self.DE_Marines_Electronics_Info__scrollArea_1.setObjectName("DE_Marines_Electronics_Info__scrollArea_1")
        self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 404, 236))
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
        self.gridLayout_7.addWidget(self.DE_Marines_Electronics_Info__scrollArea_1, 1, 2, 1, 1)
        self.DE_Marine_Electronics_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marine_Electronics_Info__horizontalLayout_1.setObjectName("DE_Marine_Electronics_Info__horizontalLayout_1")
        self.DE_Marine_Electronics_Info__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_Marine_Electronics_Info__label_1.setObjectName("DE_Marine_Electronics_Info__label_1")
        self.DE_Marine_Electronics_Info__horizontalLayout_1.addWidget(self.DE_Marine_Electronics_Info__label_1)
        self.gridLayout_7.addLayout(self.DE_Marine_Electronics_Info__horizontalLayout_1, 0, 2, 1, 1)
        self.DE_Gather_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info__horizontalLayout_1.setObjectName("DE_Gather_Info__horizontalLayout_1")
        self.DE_Gather_Info__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_Gather_Info__label_1.setObjectName("DE_Gather_Info__label_1")
        self.DE_Gather_Info__horizontalLayout_1.addWidget(self.DE_Gather_Info__label_1)
        self.gridLayout_7.addLayout(self.DE_Gather_Info__horizontalLayout_1, 2, 1, 1, 1)
        self.DE_other_files__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files__horizontalLayout_1.setObjectName("DE_other_files__horizontalLayout_1")
        self.DE_other_files__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_other_files__label_1.setObjectName("DE_other_files__label_1")
        self.DE_other_files__horizontalLayout_1.addWidget(self.DE_other_files__label_1)
        self.DE_other_files__addButton_1 = QtWidgets.QPushButton(self.DE__scrollAreaWidgetContents)
        self.DE_other_files__addButton_1.setObjectName("DE_other_files__addButton_1")
        self.DE_other_files__horizontalLayout_1.addWidget(self.DE_other_files__addButton_1)
        self.gridLayout_7.addLayout(self.DE_other_files__horizontalLayout_1, 2, 2, 1, 1)
        self.tabWidget_7 = QtWidgets.QTabWidget(self.DE__scrollAreaWidgetContents)
        self.tabWidget_7.setObjectName("tabWidget_7")


        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.DE_other_files__scrollArea_1 = QtWidgets.QScrollArea(self.tab_4)
        self.DE_other_files__scrollArea_1.setWidgetResizable(True)
        self.DE_other_files__scrollArea_1.setObjectName("DE_other_files__scrollArea_1")
        self.DE_other_files__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_other_files__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 385, 312))
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
        self.gridLayout_9.addWidget(self.DE_other_files__scrollArea_1, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_4, "")


        self.gridLayout_7.addWidget(self.tabWidget_7, 3, 2, 1, 1)
        self.DE_Acquisition_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info__horizontalLayout_1.setObjectName("DE_Acquisition_Info__horizontalLayout_1")
        self.DE_Acquisition_Info__label_1 = QtWidgets.QLabel(self.DE__scrollAreaWidgetContents)
        self.DE_Acquisition_Info__label_1.setObjectName("DE_Acquisition_Info__label_1")
        self.DE_Acquisition_Info__horizontalLayout_1.addWidget(self.DE_Acquisition_Info__label_1)
        self.DE_Acquisition_Info__addButton_1 = QtWidgets.QPushButton(self.DE__scrollAreaWidgetContents)
        self.DE_Acquisition_Info__addButton_1.setObjectName("DE_Acquisition_Info__addButton_1")
        self.DE_Acquisition_Info__horizontalLayout_1.addWidget(self.DE_Acquisition_Info__addButton_1)
        self.gridLayout_7.addLayout(self.DE_Acquisition_Info__horizontalLayout_1, 0, 3, 1, 1)
        self.tabWidget_8 = QtWidgets.QTabWidget(self.DE__scrollAreaWidgetContents)
        self.tabWidget_8.setObjectName("tabWidget_8")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.DE_Acquisition_Info__scrollArea_1 = QtWidgets.QScrollArea(self.tab_6)
        self.DE_Acquisition_Info__scrollArea_1.setWidgetResizable(True)
        self.DE_Acquisition_Info__scrollArea_1.setObjectName("DE_Acquisition_Info__scrollArea_1")
        self.DE_Acquisition_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Acquisition_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -2, 372, 449))
        self.DE_Acquisition_Info__scrollAreaWidgetContents_1.setObjectName("DE_Acquisition_Info__scrollAreaWidgetContents_1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.DE_Acquisition_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Acquisition_Info__verticalLayout_1.setObjectName("DE_Acquisition_Info__verticalLayout_1")
        self.DE_Authentication_ID__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Authentication_ID__horizontalLayout_1.setObjectName("DE_Authentication_ID__horizontalLayout_1")
        self.DE_Authentication_ID__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Authentication_ID__label_1.setObjectName("DE_Authentication_ID__label_1")
        self.DE_Authentication_ID__horizontalLayout_1.addWidget(self.DE_Authentication_ID__label_1)
        self.DE_Authentication_ID__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Authentication_ID__lineEdit_1.setObjectName("DE_Authentication_ID__lineEdit_1")
        self.DE_Authentication_ID__horizontalLayout_1.addWidget(self.DE_Authentication_ID__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(self.DE_Authentication_ID__horizontalLayout_1)
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
        self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.setObjectName("DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_tool_version__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_tool_version__label_1.setObjectName("DE_Acquisition_Info_acquisition_tool_version__label_1")
        self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_tool_version__label_1)
        self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_tool_version__lineEdit_1")
        self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1)
        self.DE_Authentication_Person_Party_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Authentication_Person_Party_Name__horizontalLayout_1.setObjectName("DE_Authentication_Person_Party_Name__horizontalLayout_1")
        self.DE_Authentication_Person_Party_Name__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Authentication_Person_Party_Name__label_1.setObjectName("DE_Authentication_Person_Party_Name__label_1")
        self.DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(self.DE_Authentication_Person_Party_Name__label_1)
        self.DE_Authentication_Person_Party_Name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Authentication_Person_Party_Name__lineEdit_1.setObjectName("DE_Authentication_Person_Party_Name__lineEdit_1")
        self.DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(self.DE_Authentication_Person_Party_Name__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(self.DE_Authentication_Person_Party_Name__horizontalLayout_1)
        self.gridLayout_4.addLayout(self.DE_Acquisition_Info__verticalLayout_1, 0, 0, 1, 1)
        self.tabWidget_10 = QtWidgets.QTabWidget(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.tabWidget_10.setObjectName("tabWidget_10")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.DE_Acquisition_Info_file__scrollArea_1 = QtWidgets.QScrollArea(self.tab_9)
        self.DE_Acquisition_Info_file__scrollArea_1.setWidgetResizable(True)
        self.DE_Acquisition_Info_file__scrollArea_1.setObjectName("DE_Acquisition_Info_file__scrollArea_1")
        self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -356, 381, 436))
        self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setObjectName("DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.setObjectName("DE_Acquisition_Info__DEF_file__verticalLayout_1")
        self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_serial_no__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_serial_no__label_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__label_1")
        self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_serial_no__label_1)
        self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__lineEdit_1")
        self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_management_id__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_management_id__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_management_id__label_1.setObjectName("DE_Acquisition_Info_DEF_management_id__label_1")
        self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_management_id__label_1)
        self.DE_Acquisition_Info_DEF_management_id__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_management_id__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_management_id__lineEdit_1")
        self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_type__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__label_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_digital_evidence_type__label_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__label_1")
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_evidences_gathering_type__label_1)
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1")
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_gather_no__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_gather_no__label_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__label_1")
        self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_gather_no__label_1)
        self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__lineEdit_1")
        self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_browse__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        self.DE_Acquisition_Info_DEF_browse__label_1.setObjectName("DE_Acquisition_Info_DEF_browse__label_1")
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_browse__label_1)
        self.DE_Acquisition_Info_DEF_browse__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_browse__lineEdit_1")
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_browse__lineEdit_1)
        self.DE_Acquisition_Info_DEF_browse__browseButton_1 = QtWidgets.QPushButton(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_browse__browseButton_1.setObjectName("DE_Acquisition_Info_DEF_browse__browseButton_1")
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_browse__browseButton_1)
        self.DE_Acquisition_Info_DEF_browse__enterButton_1 = QtWidgets.QPushButton(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_browse__enterButton_1.setObjectName("DE_Acquisition_Info_DEF_browse__enterButton_1")
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_browse__enterButton_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_hash_type__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_hash_type__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__label_1")
        self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_hash_type__label_1)
        self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__lineEdit_1")
        self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_hash_value__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_hash_value__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__label_1")
        self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_hash_value__label_1)
        self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__lineEdit_1")
        self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_sector_size__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_sector_size__label_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__label_1")
        self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_sector_size__label_1)
        self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__lineEdit_1")
        self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_file_size__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_file_size__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_file_size__label_1.setObjectName("DE_Acquisition_Info_DEF_file_size__label_1")
        self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_file_size__label_1)
        self.DE_Acquisition_Info_DEF_file_size__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_file_size__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_file_size__lineEdit_1")
        self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF__metadata__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF__metadata__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF__metadata__label_1.setObjectName("DE_Acquisition_Info_DEF__metadata__label_1")
        self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF__metadata__label_1)
        self.DE_Acquisition_Info_DEF__metadata__lineEdit_1 = QtWidgets.QLineEdit(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF__metadata__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF__metadata__lineEdit_1")
        self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1)
        self.gridLayout_15.addLayout(self.DE_Acquisition_Info__DEF_file__verticalLayout_1, 0, 0, 1, 1)
        self.DE_Acquisition_Info_file__scrollArea_1.setWidget(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.gridLayout_17.addWidget(self.DE_Acquisition_Info_file__scrollArea_1, 0, 0, 1, 1)
        self.tabWidget_10.addTab(self.tab_9, "")
        self.gridLayout_4.addWidget(self.tabWidget_10, 2, 0, 1, 1)
        self.DE_Acquisition_Info_DEF__addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF__addButton__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF__label_1.setObjectName("DE_Acquisition_Info_DEF__label_1")
        self.DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF__label_1)
        self.DE_Acquisition_Info_DEF__addButton_1 = QtWidgets.QPushButton(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF__addButton_1.setObjectName("DE_Acquisition_Info_DEF__addButton_1")
        self.DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF__addButton_1)
        self.gridLayout_4.addLayout(self.DE_Acquisition_Info_DEF__addButton__horizontalLayout_1, 1, 0, 1, 1)
        self.DE_Acquisition_Info__scrollArea_1.setWidget(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.gridLayout_29.addWidget(self.DE_Acquisition_Info__scrollArea_1, 0, 0, 1, 1)
        self.tabWidget_8.addTab(self.tab_6, "")
        self.gridLayout_7.addWidget(self.tabWidget_8, 1, 3, 3, 1)
        self.DE__scrollArea_1.setWidget(self.DE__scrollAreaWidgetContents)
        self.gridLayout_26.addWidget(self.DE__scrollArea_1, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_2, "")
        self.gridLayout_21.addWidget(self.tabWidget_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.DE_tab, "")
        self.AI_tab = QtWidgets.QWidget()
        self.AI_tab.setObjectName("AI_tab")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.AI_tab)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.AI_title__label = QtWidgets.QLabel(self.AI_tab)
        self.AI_title__label.setObjectName("AI_title__label")
        self.gridLayout_25.addWidget(self.AI_title__label, 0, 0, 1, 1)
        self.AI_scrollArea = QtWidgets.QScrollArea(self.AI_tab)
        self.AI_scrollArea.setWidgetResizable(True)
        self.AI_scrollArea.setObjectName("AI_scrollArea")
        self.AI_scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.AI_scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 1340, 665))
        self.AI_scrollAreaWidgetContents_1.setObjectName("AI_scrollAreaWidgetContents_1")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.AI_scrollAreaWidgetContents_1)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.AI_EquipmentTraces__addButton = QtWidgets.QPushButton(self.AI_scrollAreaWidgetContents_1)
        self.AI_EquipmentTraces__addButton.setObjectName("AI_EquipmentTraces__addButton")
        self.gridLayout_24.addWidget(self.AI_EquipmentTraces__addButton, 2, 0, 1, 1)
        self.tabWidget_6 = QtWidgets.QTabWidget(self.AI_scrollAreaWidgetContents_1)
        self.tabWidget_6.setObjectName("tabWidget_6")

        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.AI_Report__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_Report__horizontalLayout_1.setObjectName("AI_Report__horizontalLayout_1")
        self.AI_Report__label_1 = QtWidgets.QLabel(self.tab_7)
        self.AI_Report__label_1.setObjectName("AI_Report__label_1")
        self.AI_Report__horizontalLayout_1.addWidget(self.AI_Report__label_1)
        self.gridLayout_23.addLayout(self.AI_Report__horizontalLayout_1, 0, 0, 1, 1)
        self.AI_Reports_scrollArea = QtWidgets.QScrollArea(self.tab_7)
        self.AI_Reports_scrollArea.setWidgetResizable(True)
        self.AI_Reports_scrollArea.setObjectName("AI_Reports_scrollArea")
        self.AI_Reports__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.AI_Reports__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 593, 529))
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
        self.AI_Reports_file_creation_datetime__lineEdit_1.setPlaceholderText("")
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
        self.gridLayout_23.addWidget(self.AI_Reports_scrollArea, 1, 0, 1, 1)
        self.tabWidget_6.addTab(self.tab_7, "")

        self.gridLayout_24.addWidget(self.tabWidget_6, 1, 0, 1, 1)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.AI_scrollAreaWidgetContents_1)
        self.tabWidget_4.setObjectName("tabWidget_4")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.AI_other_files__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_other_files__horizontalLayout_1.setObjectName("AI_other_files__horizontalLayout_1")
        self.AI_other_files__label_1 = QtWidgets.QLabel(self.tab_3)
        self.AI_other_files__label_1.setObjectName("AI_other_files__label_1")
        self.AI_other_files__horizontalLayout_1.addWidget(self.AI_other_files__label_1)
        self.gridLayout_10.addLayout(self.AI_other_files__horizontalLayout_1, 0, 0, 1, 1)
        self.AI_other_files__scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.AI_other_files__scrollArea.setWidgetResizable(True)
        self.AI_other_files__scrollArea.setObjectName("AI_other_files__scrollArea")
        self.AI__scrollAreaWidgetContents = QtWidgets.QWidget()
        self.AI__scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 618, 520))
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
        self.gridLayout_10.addWidget(self.AI_other_files__scrollArea, 1, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_3, "")

        self.gridLayout_24.addWidget(self.tabWidget_4, 1, 1, 3, 1)
        self.tabWidget_5 = QtWidgets.QTabWidget(self.AI_scrollAreaWidgetContents_1)
        self.tabWidget_5.setObjectName("tabWidget_5")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.AI_EquipmentTraces__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.AI_EquipmentTraces__horizontalLayout_1.setObjectName("AI_EquipmentTraces__horizontalLayout_1")
        self.AI_EquipmentTraces__label_1 = QtWidgets.QLabel(self.tab_5)
        self.AI_EquipmentTraces__label_1.setObjectName("AI_EquipmentTraces__label_1")
        self.AI_EquipmentTraces__horizontalLayout_1.addWidget(self.AI_EquipmentTraces__label_1)
        self.gridLayout_22.addLayout(self.AI_EquipmentTraces__horizontalLayout_1, 0, 0, 1, 1)
        self.AI_EquipmentTraces__scrollArea_1 = QtWidgets.QScrollArea(self.tab_5)
        self.AI_EquipmentTraces__scrollArea_1.setWidgetResizable(True)
        self.AI_EquipmentTraces__scrollArea_1.setObjectName("AI_EquipmentTraces__scrollArea_1")
        self.AI_EquipmentTraces__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.AI_EquipmentTraces__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 593, 346))
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
        self.AI_EquipmentTraces_id__lineEdit_1.setReadOnly(False)
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
        self.AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 535, 267))
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
        self.gridLayout_22.addWidget(self.AI_EquipmentTraces__scrollArea_1, 1, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_5, "")

        self.gridLayout_24.addWidget(self.tabWidget_5, 3, 0, 1, 1)
        self.AI_Reports__addButton = QtWidgets.QPushButton(self.AI_scrollAreaWidgetContents_1)
        self.AI_Reports__addButton.setObjectName("AI_Reports__addButton")
        self.gridLayout_24.addWidget(self.AI_Reports__addButton, 0, 0, 1, 1)
        self.AI_other_files__addButton = QtWidgets.QPushButton(self.AI_scrollAreaWidgetContents_1)
        self.AI_other_files__addButton.setObjectName("AI_other_files__addButton")
        self.gridLayout_24.addWidget(self.AI_other_files__addButton, 0, 1, 1, 1)
        self.AI_scrollArea.setWidget(self.AI_scrollAreaWidgetContents_1)
        self.gridLayout_25.addWidget(self.AI_scrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.AI_tab, "")
        self.Log_tab = QtWidgets.QWidget()
        self.Log_tab.setObjectName("Log_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Log_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Log__addButton = QtWidgets.QPushButton(self.Log_tab)
        self.Log__addButton.setObjectName("Log__addButton")
        self.gridLayout_8.addWidget(self.Log__addButton, 0, 1, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.Log_tab)
        self.tabWidget_2.setObjectName("tabWidget_2")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Log__scrollArea = QtWidgets.QScrollArea(self.tab)
        self.Log__scrollArea.setWidgetResizable(True)
        self.Log__scrollArea.setObjectName("Log__scrollArea")
        self.scrollAreaWidgetContents_12 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 1308, 592))
        self.scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_12)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.Log__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.Log__verticalLayout_1.setObjectName("Log__verticalLayout_1")
        self.Log_digital_evidence_package_management_id___horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.Log_digital_evidence_package_management_id___horizontalLayout_1.setObjectName("Log_digital_evidence_package_management_id___horizontalLayout_1")
        self.Log_digital_evidence_package_management_id__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.Log_digital_evidence_package_management_id__label_1.setObjectName("Log_digital_evidence_package_management_id__label_1")
        self.Log_digital_evidence_package_management_id___horizontalLayout_1.addWidget(self.Log_digital_evidence_package_management_id__label_1)
        self.Log_digital_evidence_package_management_id__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.Log_digital_evidence_package_management_id__lineEdit_1.setObjectName("Log_digital_evidence_package_management_id__lineEdit_1")
        self.Log_digital_evidence_package_management_id___horizontalLayout_1.addWidget(self.Log_digital_evidence_package_management_id__lineEdit_1)
        self.Log__verticalLayout_1.addLayout(self.Log_digital_evidence_package_management_id___horizontalLayout_1)

        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1.setObjectName("Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1")
        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1.setObjectName("Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1")
        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1.addWidget(self.Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1)
        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1.setObjectName("Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1")
        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1.addWidget(self.Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1)

        starttime = str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))))

        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1.setText(str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))))

        self.Log__verticalLayout_1.addLayout(self.Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1)
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1.setObjectName("Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1")
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__label_1.setObjectName("Log_Digital_Evidence_Pack_History_End_Date_Time__label_1")
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1.addWidget(self.Log_Digital_Evidence_Pack_History_End_Date_Time__label_1)
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1.setObjectName("Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1")
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1.addWidget(self.Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1)
        self.Log__verticalLayout_1.addLayout(self.Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1)
        self.Log_log_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.Log_log_type__horizontalLayout_1.setObjectName("Log_log_type__horizontalLayout_1")
        self.Log_log_type__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.Log_log_type__label_1.setObjectName("Log_log_type__label_1")
        self.Log_log_type__horizontalLayout_1.addWidget(self.Log_log_type__label_1)
        self.Log_log_type__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.Log_log_type__lineEdit_1.setObjectName("Log_log_type__lineEdit_1")
        self.Log_log_type__horizontalLayout_1.addWidget(self.Log_log_type__lineEdit_1)
        self.Log__verticalLayout_1.addLayout(self.Log_log_type__horizontalLayout_1)
        self.Log_log_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.Log_log_description__horizontalLayout_1.setObjectName("Log_log_description__horizontalLayout_1")
        self.Log_log_description__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.Log_log_description__label_1.setObjectName("Log_log_description__label_1")
        self.Log_log_description__horizontalLayout_1.addWidget(self.Log_log_description__label_1)
        self.Log_log_description__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.Log_log_description__lineEdit_1.setObjectName("Log_log_description__lineEdit_1")
        self.Log_log_description__horizontalLayout_1.addWidget(self.Log_log_description__lineEdit_1)
        self.Log__verticalLayout_1.addLayout(self.Log_log_description__horizontalLayout_1)
        self.Log_devision_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.Log_devision_name_of_logger__horizontalLayout_1.setObjectName("Log_devision_name_of_logger__horizontalLayout_1")
        self.Log_devision_name_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.Log_devision_name_of_logger__label_1.setObjectName("Log_devision_name_of_logger__label_1")
        self.Log_devision_name_of_logger__horizontalLayout_1.addWidget(self.Log_devision_name_of_logger__label_1)
        self.Log_devision_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.Log_devision_name_of_logger__lineEdit_1.setObjectName("Log_devision_name_of_logger__lineEdit_1")
        self.Log_devision_name_of_logger__horizontalLayout_1.addWidget(self.Log_devision_name_of_logger__lineEdit_1)
        self.Log__verticalLayout_1.addLayout(self.Log_devision_name_of_logger__horizontalLayout_1)
        self.Log_team_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.Log_team_name_of_logger__horizontalLayout_1.setObjectName("Log_team_name_of_logger__horizontalLayout_1")
        self.Log_team_name_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.Log_team_name_of_logger__label_1.setObjectName("Log_team_name_of_logger__label_1")
        self.Log_team_name_of_logger__horizontalLayout_1.addWidget(self.Log_team_name_of_logger__label_1)
        self.Log_team_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.Log_team_name_of_logger__lineEdit_1.setObjectName("Log_team_name_of_logger__lineEdit_1")
        self.Log_team_name_of_logger__horizontalLayout_1.addWidget(self.Log_team_name_of_logger__lineEdit_1)
        self.Log__verticalLayout_1.addLayout(self.Log_team_name_of_logger__horizontalLayout_1)
        self.Log_rank_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.Log_rank_of_logger__horizontalLayout_1.setObjectName("Log_rank_of_logger__horizontalLayout_1")
        self.Log_rank_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.Log_rank_of_logger__label_1.setObjectName("Log_rank_of_logger__label_1")
        self.Log_rank_of_logger__horizontalLayout_1.addWidget(self.Log_rank_of_logger__label_1)
        self.Log_rank_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.Log_rank_of_logger__lineEdit_1.setObjectName("Log_rank_of_logger__lineEdit_1")
        self.Log_rank_of_logger__horizontalLayout_1.addWidget(self.Log_rank_of_logger__lineEdit_1)
        self.Log__verticalLayout_1.addLayout(self.Log_rank_of_logger__horizontalLayout_1)
        self.Log_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.Log_name_of_logger__horizontalLayout_1.setObjectName("Log_name_of_logger__horizontalLayout_1")
        self.Log_name_of_logger__label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_12)
        self.Log_name_of_logger__label_1.setObjectName("Log_name_of_logger__label_1")
        self.Log_name_of_logger__horizontalLayout_1.addWidget(self.Log_name_of_logger__label_1)
        self.Log_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_12)
        self.Log_name_of_logger__lineEdit_1.setObjectName("Log_name_of_logger__lineEdit_1")
        self.Log_name_of_logger__horizontalLayout_1.addWidget(self.Log_name_of_logger__lineEdit_1)
        self.Log__verticalLayout_1.addLayout(self.Log_name_of_logger__horizontalLayout_1)
        self.gridLayout_16.addLayout(self.Log__verticalLayout_1, 0, 0, 1, 1)
        self.Log__scrollArea.setWidget(self.scrollAreaWidgetContents_12)
        self.gridLayout_5.addWidget(self.Log__scrollArea, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.gridLayout_8.addWidget(self.tabWidget_2, 1, 0, 1, 2)
        self.Log__label = QtWidgets.QLabel(self.Log_tab)
        self.Log__label.setObjectName("Log__label")
        self.gridLayout_8.addWidget(self.Log__label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Log_tab, "")
        self.gridLayout_28.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_14.addWidget(self.label_2)
        self.KSButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.KSButton.setFont(font)
        self.KSButton.setObjectName("KSButton")
        self.horizontalLayout_14.addWidget(self.KSButton)
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
        self.gridLayout_28.addLayout(self.horizontalLayout_14, 2, 0, 1, 1)
        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_9.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(0)
        self.tabWidget_10.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

        ### tabwidget 저장
        self.DE_Gather_Info_Tab_Widget_List.append(self.tabWidget_9)


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

        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1.setReadOnly(True)
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1.setReadOnly(True)

        # self.DE_AddAll_num = 1
        # self.DE_AddAll_List = list()
        tmp_list = list()
        tmp_list.append(self.DE_Vessel_Info_vessel_name__lineEdit_1)  # 0
        tmp_list.append(self.DE_Vessel_Info_vessel_management_id__lineEdit_1)  # 1
        tmp_list.append(self.DE_Vessel_Info_vessel_MMSI__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_callsign__lineEdit_1)  #
        tmp_list.append(self.DE_Vessel_Info_vessel_IMO__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_MRN__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_tonnage__lineEdit_1)
        tmp_list.append(self.DE_Vessel_Info_vessel_length__lineEdit_1)  # 7
        tmp_list.append(self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1)  # 8
        tmp_list.append(self.DE_Vessel_Type__lineEdit_1)  # 9

        tmp_list.append(self.DE_Marines_Electronics_Info_device_management_id__lineEdit_1)  # 10
        tmp_list.append(self.DE_Marines_Electronics_Info_device_type__lineEdit_1)  # 11
        tmp_list.append(self.DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1)  # 12
        tmp_list.append(self.DE_Marines_Electronics_Info_device_model_name__lineEdit_1)
        tmp_list.append(self.DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1)
        tmp_list.append(self.DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1)  # 15
        tmp_list.append(self.DE_Marines_Electronics_Info_device_description__lineEdit_1)  # 16

        tmp_list.append(self.DE_Gather_Info_gather_no__lineEdit_1)  # 17
        tmp_list.append(self.DE_Gather_Info_gather_location__lineEdit_1)  # 18
        tmp_list.append(self.DE_Gather_Info_gather_person_name__lineEdit_1)  # 19
        tmp_list.append(self.DE_Gather_Info_gather_datetime__lineEdit_1)  # 20
        tmp_list.append(self.DE_Gather_Info_gather_person_agency__lineEdit_1)  # 21
        tmp_list.append(self.DE_Gather_Info_gather_person_rank__lineEdit_1)  # 22
        tmp_list.append(self.DE_Gather_Info_organization_code__lineEdit_1) #23
        tmp_list.append(self.DE_Gather_Info_submitter_name__lineEdit_1) #24
        tmp_list.append(self.DE_Gather_Inf_Gather_Source_Name__lineEdit_1) #25
        tmp_list.append(self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1) #26

        # # Gather추가
        # gather_info_list = list()
        # gather_info_list.append(self.DE_Gather_Info_file__filebrowse__lineEdit_1)
        # gather_info_list.append(self.DE_Gather_Info_gather_media_type__lineEdit_1)
        # gather_info_list.append(self.DE_Gather_Info__gather_hash_type__lineEdit_1)
        # gather_info_list.append(self.DE_Gather_Info_gather_hash__lineEdit_1)
        # gather_info_list.append(self.DE_Gather_Info_gather_path__lineEdit_1)
        # gather_info_list.append(self.DE_Gather_Info_gather_metadata__lineEdit_1)
        # self.DE_Gather_Info_List[0].append(gather_info_list)
        #
        # tmp_list.append(self.DE_Gather_Info_file__filebrowse__lineEdit_1) #27
        # tmp_list.append(self.DE_Gather_Info_gather_media_type__lineEdit_1)  #28
        # tmp_list.append(self.DE_Gather_Info__gather_hash_type__lineEdit_1) #29
        # tmp_list.append(self.DE_Gather_Info_gather_hash__lineEdit_1) #30
        # tmp_list.append(self.DE_Gather_Info_gather_path__lineEdit_1) #31
        # tmp_list.append(self.DE_Gather_Info_gather_metadata__lineEdit_1)  #32

        # 기타파일 추가
        tmp_list.append(self.DE_other_files_file_browse__lineEdit_1)  #33
        tmp_list.append(self.DE_other_files_id__lineEdit_1) #34
        tmp_list.append(self.DE_other_files_type__lineEdit_1) #35
        tmp_list.append(self.DE_other_files_file_size__lineEdit_1) #36
        tmp_list.append(self.DE_other_files_file_path__lineEdit_1)  #37
        tmp_list.append(self.DE_other_files_file_hash_type__lineEdit_1) #38
        tmp_list.append(self.DE_other_files_file_hash_value__lineEdit_1) #39
        tmp_list.append(self.DE_other_files_file_description__lineEdit_1)
        tmp_list.append(self.DE_other_files_file_metadata__lineEdit_1)  #41

        tmp_list.append(self.DE_Authentication_ID__lineEdit_1)  #42
        tmp_list.append(self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1) #43
        tmp_list.append(self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1) #44
        tmp_list.append(self.DE_Acquisition_Info_acquisition_location__lineEdit_1)  # 45
        tmp_list.append(self.DE_Acquisition_Info_acquisition_tool__lineEdit_1) #46
        tmp_list.append(self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1) #47
        tmp_list.append(self.DE_Authentication_Person_Party_Name__lineEdit_1) #48


        # Acquisition 추가
        tmp_list.append(self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1)  #49
        tmp_list.append(self.DE_Acquisition_Info_DEF_management_id__lineEdit_1) #50
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)  #51
        tmp_list.append(self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1) #52
        tmp_list.append(self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1)  #53
        tmp_list.append(self.DE_Acquisition_Info_DEF_browse__lineEdit_1) #54
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)  #55
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1) #56
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1) #57
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1) #58
        tmp_list.append(self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1)  #59
        tmp_list.append(self.DE_Acquisition_Info_DEF_file_size__lineEdit_1) #60
        tmp_list.append(self.DE_Acquisition_Info_DEF__metadata__lineEdit_1) #61

        self.DE_AddAll_List.append(tmp_list)

        # DE Gather_Info
        tmp_list = list()
        tmp_list.append(self.DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_path__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_metadata__lineEdit_1)
        self.DE_Gather_Info_List[0].append(tmp_list)

        # DE 기타파일 +누르면 add
        tmp_list = list()
        tmp_list.append(self.DE_other_files_file_browse__lineEdit_1)  # 0
        tmp_list.append(self.DE_other_files_id__lineEdit_1)  # 1
        tmp_list.append(self.DE_other_files_type__lineEdit_1) #2
        tmp_list.append(self.DE_other_files_file_size__lineEdit_1) #3
        tmp_list.append(self.DE_other_files_file_path__lineEdit_1)  # 4
        tmp_list.append(self.DE_other_files_file_hash_type__lineEdit_1) #5
        tmp_list.append(self.DE_other_files_file_hash_value__lineEdit_1) #6
        tmp_list.append(self.DE_other_files_file_description__lineEdit_1) #7
        tmp_list.append(self.DE_other_files_file_metadata__lineEdit_1)  # 8
        self.DE_Other_Files_Info_List[0].append(tmp_list)

        # DE 수집 정보
        tmp_list = list()
        tmp_list.append(self.DE_Acquisition_Info_DEF_browse__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        self.DE_Acquisition_Info_DEF_List[0].append(tmp_list)

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

        tmp_list = list()

        # 추가
        datetime.datetime.today()
        datetime.datetime.now()
        now = datetime.datetime.now()

        tmp_list.append(self.Log_digital_evidence_package_management_id__lineEdit_1)
        tmp_list.append(self.Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1)
        tmp_list.append(now)
        tmp_list.append(self.Log_log_type__lineEdit_1)
        tmp_list.append(self.Log_log_description__lineEdit_1)
        tmp_list.append(self.Log_devision_name_of_logger__lineEdit_1)
        tmp_list.append(self.Log_team_name_of_logger__lineEdit_1)
        tmp_list.append(self.Log_rank_of_logger__lineEdit_1)
        tmp_list.append(self.Log_name_of_logger__lineEdit_1)

        self.Log_List.append(tmp_list)

        ##DE_Gather_Info Browse버튼 클릭하면 파일 업로드
        gather_info_button_list = list()
        gather_info_button_list.append(self.DE_Gather_Info_file__filebrowse__browseButton_1)
        gather_info_button_list.append(self.DE_Gather_Info_file__filebrowse__enterButton_1)
        self.DE_Gather_Info_Button_List[0].append(gather_info_button_list)

        self.DE_Gather_Info_Button_List[0][0][0].clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog(0, 0)
        )
        self.DE_Gather_Info_Button_List[0][0][1].clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__enterButton_1_Calculate(0, 0)
        )

        # self.DE_Gather_Info_file__filebrowse__browseButton_1.clicked.connect(
        #     lambda: self.DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog(0, 0))
        #
        # # DE gather에서 enter버튼 클릭하면 계산
        # self.DE_Gather_Info_file__filebrowse__enterButton_1.clicked.connect(
        #     lambda: self.DE_Gather_Info_file__filebrowse__enterButton_1_Calculate(0, 0))



        ##DE Other File에서 Browse누르면 파일 클릭하면 파일 업로드
        self.DE_other_files_file_browse__browseButton_1.clicked.connect(
            lambda: self.DE_other_files_file_browse__browseButton_1_QFileDialog(0, 0))

        self.DE_Acquisition_Info_DEF_browse__browseButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info_DEF_browse__browseButton_1_QFileDialog(0, 0))


        self.DE_other_files_file_browse__EnterButton_1.clicked.connect(
            lambda: self.DE_other_files_file_browse__EnterButton_1_Calculate(0, 0))

        # DE 수집에서 Enter누르면 계산
        self.DE_Acquisition_Info_DEF_browse__enterButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info_DEF_browse__enterButton_1_Calculate(0, 0))

        #DE Gather에서 addTab
        self.DE_Gather_Info__addButton_1.clicked.connect(
            lambda: self.DE_Gather_Info_AddTab(0))

        #DE Other에서 addTab
        self.DE_other_files__addButton_1.clicked.connect(
            self.DE_Other_Files_AddTab)

        #DE 수집에서 addTab
        self.DE_Acquisition_Info__addButton_1.clicked.connect(
            self.DE_Acquisition_Info_AddTab)

        # DE 수집 DEF에서 addTab
        self.DE_Acquisition_Info_DEF__addButton_1.clicked.connect(
            self.DE_Acquisition_Info_DEF_AddTab)

        # DE 전체 addTab
        self.DE__addButton.clicked.connect(
            self.DE_AddTab)




        # <Analysis Info>
        # AI Report browse버튼 클릭하면 파일 업로드
        self.AI_Reports_file_info__browseButton_1.clicked.connect(
            lambda: self.AI_Reports_file_info__browseButton_1_QFileDialog(0))

        ## AI Report Enter 클릭하면 파일 계산
        self.AI_Reports_file_info__enterButton_1.clicked.connect(
            lambda: self.AI_Reports_file_info__enterButton_1_Calculate(0))

        ## AI other file browse버튼 클릭하면 파일 업로드
        self.AI_other_files_file_browse__browseButton_1.clicked.connect(
            lambda: self.AI_other_files_file_browse__browseButton_1_QFileDialog(0))

        ## AI OtherFile Enter 클릭하면 파일 계산
        self.AI_other_files_file_browse__enterButton_1.clicked.connect(
            lambda: self.AI_other_files_file_browse__enterButton_1_Calculate(0))

        # AI Reports addTab
        self.AI_Reports__addButton.clicked.connect(self.AI_Reports__AddTab)

        # AI Equipment Traces addTab
        self.AI_EquipmentTraces__addButton.clicked.connect(self.AI_Equipment_Traces_AddTab)

        # AI Other Files AddTab
        self.AI_other_files__addButton.clicked.connect(self.AI_Other_Files_AddTab)


        # Log +버튼
        self.Log__addButton.clicked.connect(self.Log__addButton_AddTab)

        ##Export버튼 누르면 json파일로 변환
        self.ExportButton.clicked.connect(self.ExportButton_exporttojsonfile)

        #KS
        self.KSButton.clicked.connect(self.KS_ExportButton_export_to_xml_file)

        # load 처리
        if self.mode == 'load':
            with open(self.file_path, 'r', encoding="utf-8") as f:
                data = json.load(f)

                # Case Info
                case_management_id = data['Digital Evidence Package']['Case Info']['case_management_id']
                agency_case_no = data['Digital Evidence Package']['Case Info']['agency_case_no.']
                agency_organization_code = data['Digital Evidence Package']['Case Info']['agency_organization_code']
                agency_organization_name = data['Digital Evidence Package']['Case Info']['agency_organization_name']
                agency_organization_party_name = data['Digital Evidence Package']['Case Info'][
                    'agency_organization_party_name']
                contents_of_request = data['Digital Evidence Package']['Case Info']['contents_of_request']
                case_summary = data['Digital Evidence Package']['Case Info']['case_summary']
                case_description = data['Digital Evidence Package']['Case Info']['case_description']
                case_datetime = data['Digital Evidence Package']['Case Info']['case_datetime']
                ordering_datetime = data['Digital Evidence Package']['Case Info']['ordering_datetime']

                # Case Info
                self.case_management_id__lineEdit.setText(case_management_id)
                self.agency_case_no__lineEdit.setText(agency_case_no)
                self.agency_organization_code__lineEdit.setText(agency_organization_code)
                self.agency_organization_name__lineEdit.setText(agency_organization_name)
                self.agency_organization_party_name__lineEdit.setText(agency_organization_party_name)

                self.contents_of_request__lineEdit.setText(contents_of_request)
                self.case_summary__lineEdit.setText(case_summary)
                self.case_description__lineEdit.setText(case_description)
                self.case_datetime__lineEdit.setText(case_datetime)
                self.ordering_datetime__lineEdit.setText(ordering_datetime)

                ##############Digital Evidence 전체 부분###### Vessel Info + Marines Electronics + Gather_Info 윗부분
                len(data['Digital Evidence Package']['Digital Evidences'])

                for i in range(0, len(data['Digital Evidence Package']['Digital Evidences'])):

                    if i == 0:

                        vessel_management_id = data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                            'vessel_management_id']
                        vessel_name = data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                            'vessel_name']
                        vessel_MMSI = data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                            'vessel_MMSI']
                        vessel_callsign = data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                            'vessel_callsign']
                        vessel_IMO = data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                            'vessel_IMO']
                        vessel_MRN = data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                            'vessel_MRN']
                        vessel_tonnage = data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                            'vessel_tonnage']
                        vessel_length = data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                            'vessel_length']
                        total_number_of_equipment_with_track = \
                            data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                                'total_number_of_equipment_with_track']
                        vessel_type = data['Digital Evidence Package']['Digital Evidences'][i]['Vessel Info'][
                            'vessel_type']

                        self.DE_Vessel_Info_vessel_management_id__lineEdit_1.setText(vessel_management_id)
                        self.DE_Vessel_Info_vessel_name__lineEdit_1.setText(vessel_name)
                        self.DE_Vessel_Info_vessel_MMSI__lineEdit_1.setText(vessel_MMSI)
                        self.DE_Vessel_Info_vessel_callsign__lineEdit_1.setText(vessel_callsign)
                        self.DE_Vessel_Info_vessel_IMO__lineEdit_1.setText(vessel_IMO)
                        self.DE_Vessel_Info_vessel_MRN__lineEdit_1.setText(vessel_MRN)
                        self.DE_Vessel_Info_vessel_tonnage__lineEdit_1.setText(vessel_tonnage)
                        self.DE_Vessel_Info_vessel_length__lineEdit_1.setText(vessel_length)
                        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1.setText(
                            total_number_of_equipment_with_track)
                        self.DE_Vessel_Type__lineEdit_1.setText(vessel_type)

                        device_management_id = \
                            data['Digital Evidence Package']['Digital Evidences'][i]['Marine Electronics Info'][
                                'device_management_id']
                        device_type = \
                            data['Digital Evidence Package']['Digital Evidences'][i]['Marine Electronics Info'][
                                'device_type']
                        device_manufacturer = \
                            data['Digital Evidence Package']['Digital Evidences'][i]['Marine Electronics Info'][
                                'device_manufacturer']
                        device_model_name = \
                            data['Digital Evidence Package']['Digital Evidences'][i]['Marine Electronics Info'][
                                'device_model_name']
                        device_model_serial_number = \
                            data['Digital Evidence Package']['Digital Evidences'][i]['Marine Electronics Info'][
                                'device_model_serial_number']
                        device_os_firmware = \
                            data['Digital Evidence Package']['Digital Evidences'][i]['Marine Electronics Info'][
                                'device_os_firmware']
                        device_descripton = \
                            data['Digital Evidence Package']['Digital Evidences'][i]['Marine Electronics Info'][
                                'device_description']

                        self.DE_Marines_Electronics_Info_device_management_id__lineEdit_1.setText(device_management_id)
                        self.DE_Marines_Electronics_Info_device_type__lineEdit_1.setText(device_type)
                        self.DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1.setText(device_manufacturer)
                        self.DE_Marines_Electronics_Info_device_model_name__lineEdit_1.setText(device_model_name)
                        self.DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1.setText(
                            device_model_serial_number)
                        self.DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1.setText(device_os_firmware)
                        self.DE_Marines_Electronics_Info_device_description__lineEdit_1.setText(device_descripton)

                        gather_no = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'gather_no']
                        gather_location = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'gather_location']
                        gather_person_name = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'gather_person_name']
                        gather_datetime = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'gather_datetime']
                        gather_person_agency = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'gather_person_agency']
                        gather_person_rank = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'gather_person_rank']
                        gather_organization_code = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'gather_organization_code']
                        submitter_name = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'submitter_name']
                        gather_source_name = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'gather_source_name']
                        gather_relation_person_type_code = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                            'gather_relation_person_type_code']

                        self.DE_Gather_Info_gather_no__lineEdit_1.setText(gather_no)
                        self.DE_Gather_Info_gather_location__lineEdit_1.setText(gather_location)
                        self.DE_Gather_Info_gather_person_name__lineEdit_1.setText(gather_person_name)
                        self.DE_Gather_Info_gather_datetime__lineEdit_1.setText(gather_datetime)
                        self.DE_Gather_Info_gather_person_agency__lineEdit_1.setText(gather_person_agency)
                        self.DE_Gather_Info_gather_person_rank__lineEdit_1.setText(gather_person_rank)
                        self.DE_Gather_Info_organization_code__lineEdit_1.setText(gather_organization_code)
                        self.DE_Gather_Info_submitter_name__lineEdit_1.setText(submitter_name)
                        self.DE_Gather_Inf_Gather_Source_Name__lineEdit_1.setText(gather_source_name)
                        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1.setText(gather_relation_person_type_code)


                        ##################Gather Info _ Media File 부분####################
                        len(data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info']['Gather Info Media File'])

                        for j in range(0, len(data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                                                  'Gather Info Media File'])):

                            if j == 0:
                                gather_media_type = \
                                    data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info']['Gather Info Media File'][j]['gather_media_type']
                                gather_hash_type = \
                                    data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                                        'Gather Info Media File'][j]['gather_hash_type']
                                gather_hash = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                                    'Gather Info Media File'][j]['gather_hash']
                                gather_path = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info'][
                                    'Gather Info Media File'][j]['gather_path']
                                gather_metadata = data['Digital Evidence Package']['Digital Evidences'][i]['Gather Info']['Gather Info Media File'][j]['gather_metadata']

                                self.DE_Gather_Info_gather_media_type__lineEdit_1.setText(gather_media_type)
                                self.DE_Gather_Info__gather_hash_type__lineEdit_1.setText(gather_hash_type)
                                self.DE_Gather_Info_gather_hash__lineEdit_1.setText(gather_hash)
                                self.DE_Gather_Info_gather_path__lineEdit_1.setText(gather_path)
                                self.DE_Gather_Info_gather_metadata__lineEdit_1.setText(gather_metadata)

                            else:
                                print("Dadsf")

                    #############[Digital Evidence][Other Files]#######
                    len(data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'])

                    for j in range(0, len(data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'])):

                        if j == 0:

                            id = data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'][j][
                                'other_files_id']
                            type = data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'][j][
                                'other_files_type']
                            file_size = data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'][j][
                                'other_files_size']
                            file_path = data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'][j][
                                'other_files_path']
                            file_hash_type = data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'][j][
                                'other_files_hash_type']
                            file_hash_value = \
                                data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'][j][
                                    'other_files_hash_value']
                            file_description = \
                                data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'][j][
                                    'other_files_file_description']
                            file_metadata = data['Digital Evidence Package']['Digital Evidences'][i]['Other Files'][j][
                                'other_files_file_metadata']

                            self.DE_other_files_id__lineEdit_1.setText(id)
                            self.DE_other_files_type__lineEdit_1.setText(type)
                            self.DE_other_files_file_size__lineEdit_1.setText(file_size)
                            self.DE_other_files_file_path__lineEdit_1.setText(file_path)
                            self.DE_other_files_file_hash_type__lineEdit_1.setText(file_hash_type)
                            self.DE_other_files_file_hash_value__lineEdit_1.setText(file_hash_value)
                            self.DE_other_files_file_description__lineEdit_1.setText(file_description)
                            self.DE_other_files_file_metadata__lineEdit_1.setText(file_metadata)

                        else:
                            print("dsf")
                    #############[Digital Evidence][Authentication Info]
                    len(data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'])
                    for j in range (0, len(data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'])):

                        if j == 0:

                            authentication_id = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j][
                                'authentication_id']
                            authentication_person_name = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j][
                                'authentication_person_name']
                            authentication_date_time = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j][
                                'authentication_date_time']
                            authentication_location = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['authentication_location']
                            authentication_tool = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['authentication_tool']

                            authentication_tool_version = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['authentication_tool_version']

                            authentication_person_party_name = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['authentication_person_party_name']

                            self.DE_Authentication_ID__lineEdit_1.setText(authentication_id)
                            self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1.setText(authentication_person_name)
                            self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setText(authentication_date_time)
                            self.DE_Acquisition_Info_acquisition_location__lineEdit_1.setText(authentication_location)
                            self.DE_Acquisition_Info_acquisition_tool__lineEdit_1.setText(authentication_tool)
                            self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1.setText(authentication_tool_version)
                            self.DE_Authentication_Person_Party_Name__lineEdit_1.setText(authentication_person_party_name)

                        else:
                            print("fg")

                        ##################Authentication Info _ DEF 부분####################
                        len(data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'])

                        for k in range(0, len(data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'])):

                            if k == 0:

                                serial_no = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['serial_no']
                                management_id = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['management_id']
                                digital_evidence_type = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['digital_evidence_type']
                                evidences_gathering_type = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['evidences_gathering_type']
                                gather_no = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['gather_no']
                                DEF_file_name = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['file_name']
                                DEF_file_path = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['file_path']
                                hash_type = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['hash_type']
                                hash_value = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['hash_value']
                                sector_size = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['sector_size']
                                DEF_file_size = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['file_size']
                                metadata = data['Digital Evidence Package']['Digital Evidences'][i]['Authentication Info'][j]['Digital Evidence Files'][k]['metadata']


                                self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1.setText(serial_no)
                                self.DE_Acquisition_Info_DEF_management_id__lineEdit_1.setText(management_id)
                                self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1.setText(digital_evidence_type)
                                self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1.setText(evidences_gathering_type)
                                self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1.setText(gather_no)
                                self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1.setText(DEF_file_name)
                                self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1.setText(DEF_file_path)
                                self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1.setText(hash_type)
                                self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1.setText(hash_value)
                                self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1.setText(sector_size)
                                self.DE_Acquisition_Info_DEF_file_size__lineEdit_1.setText(DEF_file_size)
                                self.DE_Acquisition_Info_DEF__metadata__lineEdit_1.setText(metadata)



                            else:
                                print("dsf")


                #########Analysis Info 부분 ###############
                len(data['Digital Evidence Package']['Analysis Info']['Reports'])
                for i in range(0, len(data['Digital Evidence Package']['Analysis Info']['Reports'])):

                    if i == 0:
                        id = data['Digital Evidence Package']['Analysis Info']['Reports'][i]['id']
                        type = data['Digital Evidence Package']['Analysis Info']['Reports'][i]['type']
                        subtype = data['Digital Evidence Package']['Analysis Info']['Reports'][i]['subtype']
                        mgmt_id = data['Digital Evidence Package']['Analysis Info']['Reports'][i]['mgmt_id']
                        submission_agency = data['Digital Evidence Package']['Analysis Info']['Reports'][i][
                            'submission_agency']
                        report_creation_datetime = data['Digital Evidence Package']['Analysis Info']['Reports'][i][
                            'report_creation_datetime']
                        division_name_of_report_maker = data['Digital Evidence Package']['Analysis Info']['Reports'][i][
                            'division_name_of_report_maker']
                        team_name_of_report_maker = data['Digital Evidence Package']['Analysis Info']['Reports'][i][
                            'team_name_of_report_maker']
                        file_name = data['Digital Evidence Package']['Analysis Info']['Reports'][i]['file_name']
                        file_size = data['Digital Evidence Package']['Analysis Info']['Reports'][i]['file_size']
                        file_path = data['Digital Evidence Package']['Analysis Info']['Reports'][i]['file_path']
                        file_creation_datetime = data['Digital Evidence Package']['Analysis Info']['Reports'][i][
                            'file_creation_datetime']
                        file_description = data['Digital Evidence Package']['Analysis Info']['Reports'][i][
                            'file_description']
                        hash_type = data['Digital Evidence Package']['Analysis Info']['Reports'][i]['hash_type']
                        hash_value = data['Digital Evidence Package']['Analysis Info']['Reports'][i]['hash_value']

                        self.AI_Reports_id__lineEdit_1.setText(id)
                        self.AI_Reports_type__lineEdit_1.setText(type)
                        self.AI_Reports_subtype__lineEdit_1.setText(subtype)
                        self.AI_Reports_mgmt_id__lineEdit_1.setText(mgmt_id)
                        self.AI_Reports_submission_agency__lineEdit_1.setText(submission_agency)
                        self.AI_Reports_reprot_creation_datetime__lineEdit_1.setText(report_creation_datetime)
                        self.AI_Reports_division_name_of_report_maker__lineEdit_1.setText(division_name_of_report_maker)
                        self.AI_Reports_team_name_of_report_maker__lineEdit_1.setText(team_name_of_report_maker)
                        self.AI_Reports_file_name__lineEdit_1.setText(file_name)
                        self.AI_Reports_file_size__lineEdit_1.setText(file_size)
                        self.AI_Reports_file_path__lineEdit_1.setText(file_path)
                        self.AI_Reports_file_creation_datetime__lineEdit_1.setText(file_creation_datetime)
                        self.AI_Reports_file_description__lineEdit_1.setText(file_description)
                        self.AI_Reports_file_hash_type__lineEdit_1.setText(hash_type)
                        self.AI_Reports_file_hash_value__lineEdit_1.setText(hash_value)

                ############## Equipment Traces 부분 ########
                len(data['Digital Evidence Package']['Analysis Info']['Equipment Traces'])
                for i in range(0, len(data['Digital Evidence Package']['Analysis Info']['Equipment Traces'])):

                    if i == 0:
                        id = data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i]['id']
                        type = data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i]['type']
                        description = data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                            'description']
                        mgmt_id = data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                            'mgmt_id']
                        vessel_id = data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                            'vessel_id']
                        evidence_id = data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                            'evidence_id']
                        power_on_time = \
                            data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                                'power_on_time']
                        track_extraction_description = \
                            data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                                'track_extraction_description']
                        system_info_description = \
                            data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                                'system_info_description']
                        operation_status = \
                            data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                                'operation_status']
                        power_off_time = \
                            data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                                'power_off_time']
                        track_recording_period = \
                            data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                                'track_recording_period']
                        track_deletion_trace = \
                            data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                                'track_deletion_trace']
                        trace_notes = data['Digital Evidence Package']['Analysis Info']['Equipment Traces'][i][
                            'trace_notes']

                        self.AI_EquipmentTraces_id__lineEdit_1.setText(id)
                        self.AI_EquipmentTraces_type__lineEdit_1.setText(type)
                        self.AI_EquipmentTraces_description__lineEdit_1.setText(type)
                        self.AI_EquipmentTraces_mgmt_id__lineEdit_1.setText(mgmt_id)
                        self.AI_EquipmentTraces_vessel_id__lineEdit_1.setText(vessel_id)
                        self.AI_EquipmentTraces_evidence_id__lineEdit_1.setText(evidence_id)
                        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1.setText(
                            power_on_time)
                        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1.setText(
                            track_extraction_description)
                        self.AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1.setText(
                            system_info_description)
                        self.AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1.setText(
                            system_info_description)
                        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1.setText(
                            power_off_time)
                        self.AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1.setText(
                            track_recording_period)
                        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1.setText(
                            track_deletion_trace)
                        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1.setText(
                            trace_notes)

                len(data['Digital Evidence Package']['Analysis Info']['Other Files'])

                for i in range(0, len(data['Digital Evidence Package']['Analysis Info']['Other Files'])):

                    if i == 0:
                        id = data['Digital Evidence Package']['Analysis Info']['Other Files'][i]['id']
                        type = data['Digital Evidence Package']['Analysis Info']['Other Files'][i]['type']
                        file_size = data['Digital Evidence Package']['Analysis Info']['Other Files'][i]['file_size']
                        file_path = data['Digital Evidence Package']['Analysis Info']['Other Files'][i]['file_path']
                        file_hash_type = data['Digital Evidence Package']['Analysis Info']['Other Files'][i][
                            'file_hash_type']
                        file_hash_value = data['Digital Evidence Package']['Analysis Info']['Other Files'][i][
                            'file_hash_value']
                        file_description = data['Digital Evidence Package']['Analysis Info']['Other Files'][i][
                            'file_description']
                        file_metadata = data['Digital Evidence Package']['Analysis Info']['Other Files'][i][
                            'file_metadata']

                        self.AI_other_files_id__lineEdit_1.setText(id)
                        self.AI_other_files_type__lineEdit_1.setText(type)
                        self.AI_other_files_file_size__lineEdit_1.setText(file_size)
                        self.AI_other_files_file_path__lineEdit_1.setText(file_path)
                        self.AI_other_files_file_hash_type__lineEdit_1.setText(file_hash_type)
                        self.AI_other_files_file_hash_value__lineEdit_1.setText(file_hash_value)
                        self.AI_other_files_file_description__lineEdit_1.setText(file_description)
                        self.AI_other_files_file_metadata__lineEdit_1.setText(file_metadata)

                #########Log 부분########
                len(data['Log'])

                for i in range(0, len(data['Log'])):

                    if i == 0:
                        digital_evidence_package_management_id = data['Log'][i][
                            'digital_evidence_package_management_id']
                        log_datetime = data['Log'][i]['log_history_end_date_time']  # datetime으로 고쳤음
                        log_type = data['Log'][i]['log_type']
                        log_description = data['Log'][i]['log_description']
                        devision_name_of_logger = data['Log'][i]['devision_name_of_logger']
                        team_name_of_logger = data['Log'][i]['team_name_of_logger']
                        rank_of_logger = data['Log'][i]['rank_of_logger']
                        name_of_logger = data['Log'][i]['name_of_logger']

                        self.Log_digital_evidence_package_management_id__lineEdit_1.setText(
                            digital_evidence_package_management_id)
                        self.Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1.setText(log_datetime)
                        self.Log_log_type__lineEdit_1.setText(log_type)
                        self.Log_log_description__lineEdit_1.setText(log_description)
                        self.Log_devision_name_of_logger__lineEdit_1.setText(devision_name_of_logger)
                        self.Log_team_name_of_logger__lineEdit_1.setText(team_name_of_logger)
                        self.Log_rank_of_logger__lineEdit_1.setText(rank_of_logger)
                        self.Log_name_of_logger__lineEdit_1.setText(name_of_logger)

                    else:
                        self.Log_num += 1

                        tmp_tab = QtWidgets.QWidget()
                        tmp_tab.setObjectName("tab")
                        tmp_gridLayout_5 = QtWidgets.QGridLayout(tmp_tab)
                        tmp_gridLayout_5.setObjectName("gridLayout_5")
                        tmp_Log__scrollArea = QtWidgets.QScrollArea(tmp_tab)
                        tmp_Log__scrollArea.setWidgetResizable(True)
                        tmp_Log__scrollArea.setObjectName("Log__scrollArea")
                        tmp_scrollAreaWidgetContents_12 = QtWidgets.QWidget()
                        tmp_scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 1308, 592))
                        tmp_scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
                        tmp_gridLayout_16 = QtWidgets.QGridLayout(tmp_scrollAreaWidgetContents_12)
                        tmp_gridLayout_16.setObjectName("gridLayout_16")
                        tmp_Log__verticalLayout_1 = QtWidgets.QVBoxLayout()
                        tmp_Log__verticalLayout_1.setObjectName("Log__verticalLayout_1")
                        tmp_Log_digital_evidence_package_management_id___horizontalLayout_1 = QtWidgets.QHBoxLayout()
                        tmp_Log_digital_evidence_package_management_id___horizontalLayout_1.setObjectName(
                            "Log_digital_evidence_package_management_id___horizontalLayout_1")
                        tmp_Log_digital_evidence_package_management_id__label_1 = QtWidgets.QLabel(
                            tmp_scrollAreaWidgetContents_12)
                        tmp_Log_digital_evidence_package_management_id__label_1.setObjectName(
                            "Log_digital_evidence_package_management_id__label_1")
                        tmp_Log_digital_evidence_package_management_id___horizontalLayout_1.addWidget(
                            tmp_Log_digital_evidence_package_management_id__label_1)
                        tmp_Log_digital_evidence_package_management_id__lineEdit_1 = QtWidgets.QLineEdit(
                            tmp_scrollAreaWidgetContents_12)
                        tmp_Log_digital_evidence_package_management_id__lineEdit_1.setObjectName(
                            "Log_digital_evidence_package_management_id__lineEdit_1")
                        tmp_Log_digital_evidence_package_management_id___horizontalLayout_1.addWidget(
                            tmp_Log_digital_evidence_package_management_id__lineEdit_1)
                        tmp_Log__verticalLayout_1.addLayout(
                            tmp_Log_digital_evidence_package_management_id___horizontalLayout_1)
                        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
                        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1.setObjectName(
                            "Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1")
                        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1 = QtWidgets.QLabel(
                            tmp_scrollAreaWidgetContents_12)
                        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1.setObjectName(
                            "Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1")
                        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1.addWidget(
                            tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1)
                        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1 = QtWidgets.QLineEdit(
                            tmp_scrollAreaWidgetContents_12)
                        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1.setObjectName(
                            "Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1")
                        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1.addWidget(
                            tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1)
                        tmp_Log__verticalLayout_1.addLayout(
                            tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1)
                        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
                        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1.setObjectName(
                            "Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1")
                        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__label_1 = QtWidgets.QLabel(
                            tmp_scrollAreaWidgetContents_12)
                        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__label_1.setObjectName(
                            "Log_Digital_Evidence_Pack_History_End_Date_Time__label_1")
                        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1.addWidget(
                            tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__label_1)
                        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1 = QtWidgets.QLineEdit(
                            tmp_scrollAreaWidgetContents_12)
                        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1.setObjectName(
                            "Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1")
                        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1.addWidget(
                            tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1)
                        tmp_Log__verticalLayout_1.addLayout(
                            tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1)
                        tmp_Log_log_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
                        tmp_Log_log_type__horizontalLayout_1.setObjectName("Log_log_type__horizontalLayout_1")
                        tmp_Log_log_type__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_log_type__label_1.setObjectName("Log_log_type__label_1")
                        tmp_Log_log_type__horizontalLayout_1.addWidget(tmp_Log_log_type__label_1)
                        tmp_Log_log_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_log_type__lineEdit_1.setObjectName("Log_log_type__lineEdit_1")
                        tmp_Log_log_type__horizontalLayout_1.addWidget(tmp_Log_log_type__lineEdit_1)
                        tmp_Log__verticalLayout_1.addLayout(tmp_Log_log_type__horizontalLayout_1)
                        tmp_Log_log_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
                        tmp_Log_log_description__horizontalLayout_1.setObjectName(
                            "Log_log_description__horizontalLayout_1")
                        tmp_Log_log_description__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_log_description__label_1.setObjectName("Log_log_description__label_1")
                        tmp_Log_log_description__horizontalLayout_1.addWidget(tmp_Log_log_description__label_1)
                        tmp_Log_log_description__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_log_description__lineEdit_1.setObjectName("Log_log_description__lineEdit_1")
                        tmp_Log_log_description__horizontalLayout_1.addWidget(tmp_Log_log_description__lineEdit_1)
                        tmp_Log__verticalLayout_1.addLayout(tmp_Log_log_description__horizontalLayout_1)
                        tmp_Log_devision_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
                        tmp_Log_devision_name_of_logger__horizontalLayout_1.setObjectName(
                            "Log_devision_name_of_logger__horizontalLayout_1")
                        tmp_Log_devision_name_of_logger__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_devision_name_of_logger__label_1.setObjectName("Log_devision_name_of_logger__label_1")
                        tmp_Log_devision_name_of_logger__horizontalLayout_1.addWidget(
                            tmp_Log_devision_name_of_logger__label_1)
                        tmp_Log_devision_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(
                            tmp_scrollAreaWidgetContents_12)
                        tmp_Log_devision_name_of_logger__lineEdit_1.setObjectName(
                            "Log_devision_name_of_logger__lineEdit_1")
                        tmp_Log_devision_name_of_logger__horizontalLayout_1.addWidget(
                            tmp_Log_devision_name_of_logger__lineEdit_1)
                        tmp_Log__verticalLayout_1.addLayout(tmp_Log_devision_name_of_logger__horizontalLayout_1)
                        tmp_Log_team_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
                        tmp_Log_team_name_of_logger__horizontalLayout_1.setObjectName(
                            "Log_team_name_of_logger__horizontalLayout_1")
                        tmp_Log_team_name_of_logger__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_team_name_of_logger__label_1.setObjectName("Log_team_name_of_logger__label_1")
                        tmp_Log_team_name_of_logger__horizontalLayout_1.addWidget(tmp_Log_team_name_of_logger__label_1)
                        tmp_Log_team_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_team_name_of_logger__lineEdit_1.setObjectName("Log_team_name_of_logger__lineEdit_1")
                        tmp_Log_team_name_of_logger__horizontalLayout_1.addWidget(
                            tmp_Log_team_name_of_logger__lineEdit_1)
                        tmp_Log__verticalLayout_1.addLayout(tmp_Log_team_name_of_logger__horizontalLayout_1)
                        tmp_Log_rank_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
                        tmp_Log_rank_of_logger__horizontalLayout_1.setObjectName(
                            "Log_rank_of_logger__horizontalLayout_1")
                        tmp_Log_rank_of_logger__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_rank_of_logger__label_1.setObjectName("Log_rank_of_logger__label_1")
                        tmp_Log_rank_of_logger__horizontalLayout_1.addWidget(tmp_Log_rank_of_logger__label_1)
                        tmp_Log_rank_of_logger__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_rank_of_logger__lineEdit_1.setObjectName("Log_rank_of_logger__lineEdit_1")
                        tmp_Log_rank_of_logger__horizontalLayout_1.addWidget(tmp_Log_rank_of_logger__lineEdit_1)
                        tmp_Log__verticalLayout_1.addLayout(tmp_Log_rank_of_logger__horizontalLayout_1)
                        tmp_Log_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
                        tmp_Log_name_of_logger__horizontalLayout_1.setObjectName(
                            "Log_name_of_logger__horizontalLayout_1")
                        tmp_Log_name_of_logger__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_name_of_logger__label_1.setObjectName("Log_name_of_logger__label_1")
                        tmp_Log_name_of_logger__horizontalLayout_1.addWidget(tmp_Log_name_of_logger__label_1)
                        tmp_Log_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
                        tmp_Log_name_of_logger__lineEdit_1.setObjectName("Log_name_of_logger__lineEdit_1")
                        tmp_Log_name_of_logger__horizontalLayout_1.addWidget(tmp_Log_name_of_logger__lineEdit_1)
                        tmp_Log__verticalLayout_1.addLayout(tmp_Log_name_of_logger__horizontalLayout_1)
                        tmp_gridLayout_16.addLayout(tmp_Log__verticalLayout_1, 0, 0, 1, 1)
                        tmp_Log__scrollArea.setWidget(tmp_scrollAreaWidgetContents_12)
                        tmp_gridLayout_5.addWidget(tmp_Log__scrollArea, 0, 0, 1, 1)
                        self.tabWidget_2.addTab(tmp_tab, "Tab " + str(len(self.Log_List) + 1))

                        tmp_list = list()
                        tmp_list.append(tmp_Log_digital_evidence_package_management_id__lineEdit_1) #0
                        tmp_list.append(tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1) #1
                        tmp_list.append(tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1) #2
                        tmp_list.append(tmp_Log_log_type__lineEdit_1) #3
                        tmp_list.append(tmp_Log_log_description__lineEdit_1)
                        tmp_list.append(tmp_Log_devision_name_of_logger__lineEdit_1)
                        tmp_list.append(tmp_Log_team_name_of_logger__lineEdit_1)
                        tmp_list.append(tmp_Log_rank_of_logger__lineEdit_1)
                        tmp_list.append(tmp_Log_name_of_logger__lineEdit_1)
                        self.Log_List.append(tmp_list)

                        digital_evidence_package_management_id = data['Log'][i]['digital_evidence_package_management_id']
                        log_history_start_date_time = data['Log'][i]['log_history_start_date_time']
                        log_history_end_date_time = data['Log'][i]['log_history_end_date_time']
                        log_type = data['Log'][i]['log_type']
                        log_description = data['Log'][i]['log_description']
                        devision_name_of_logger = data['Log'][i]['devision_name_of_logger']
                        team_name_of_logger = data['Log'][i]['team_name_of_logger']
                        rank_of_logger = data['Log'][i]['rank_of_logger']
                        name_of_logger = data['Log'][i]['name_of_logger']

                        tmp_Log_digital_evidence_package_management_id__lineEdit_1.setText(digital_evidence_package_management_id)
                        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1.setText(log_history_start_date_time)
                        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1.setText(log_history_end_date_time)
                        tmp_Log_log_type__lineEdit_1.setText(log_type)
                        tmp_Log_log_description__lineEdit_1.setText(log_description)
                        tmp_Log_devision_name_of_logger__lineEdit_1.setText(devision_name_of_logger)
                        tmp_Log_team_name_of_logger__lineEdit_1.setText(team_name_of_logger)
                        tmp_Log_rank_of_logger__lineEdit_1.setText(rank_of_logger)
                        tmp_Log_name_of_logger__lineEdit_1.setText(name_of_logger)

    # def KS_ExportButton_export_to_xml_file(self):
    #     rootDigitalEvidencePack_Agency = Element('DigitalEvidencePack_Agency')
    #     SubElement(rootDigitalEvidencePack_Agency, 'DigitalEvidencePackAgencyIncidentNo').text = self.CI_List[1].text()
    #     SubElement(rootDigitalEvidencePack_Agency, 'DigitalEvidencePackAgencyOrganizationCode').text = self.CI_List[2].text()
    #     SubElement(rootDigitalEvidencePack_Agency, 'DigitalEvidencePackAgencyOrganizationName').text = self.CI_List[3].text()
    #     SubElement(rootDigitalEvidencePack_Agency, 'DigitalEvidencePackAgencyOrganizationPartyName').text = self.CI_List[4].text()
    #
    #     treeDigitalEvidencePack_Agency = ElementTree(rootDigitalEvidencePack_Agency)
    #     treeDigitalEvidencePack_Agency.write(self.file_path + '.DigitalEvidencePack_Agency.xml')

    def KS_ExportButton_export_to_xml_file(self):
        rootDigitalEvidencePack = Element('DigitalEvidencePack')

        rootManagement = Element('Management')
        DigitalEvidencePackManagementIdentifier = SubElement(rootManagement, 'DigitalEvidencePackManagementIdentifier')

        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz0123456789"
        number = ""

        for i in range(10):
            index = random.randrange(len(alphabet))
            number = number + alphabet[index]

        DigitalEvidencePackManagementIdentifier.text = 'DEP-' + number
        DigitalEvidencePackFormatVersion = SubElement(rootManagement, 'DigitalEvidencePackFormatVersion')
        DigitalEvidencePackFormatVersion.text = '0.1'
        DigitalEvidencePackSizeNumeric = SubElement(rootManagement, 'DigitalEvidencePackSizeNumeric')
        DigitalEvidencePackSizeNumeric.text = ' '

        rootAgency = Element('Agency')
        DigitalEvidencePackAgencyIncident = SubElement(rootAgency, 'DigitalEvidencePackAgencyIncident')
        DigitalEvidencePackAgencyIncident.text = self.CI_List[1].text()
        DigitalEvidencePackAgencyOrganizationCode = SubElement(rootAgency, 'DigitalEvidencePackAgencyOrganizationCode')
        DigitalEvidencePackAgencyOrganizationCode.text = self.CI_List[2].text()
        DigitalEvidencePackAgencyOrganizationName = SubElement(rootAgency, 'DigitalEvidencePackAgencyOrganizationName')
        DigitalEvidencePackAgencyOrganizationName.text = self.CI_List[3].text()
        DigitalEvidencePackAgencyOrganizationPartyName = SubElement(rootAgency,
                                                                    'DigitalEvidencePackAgencyOrganizationPartyName')
        DigitalEvidencePackAgencyOrganizationPartyName.text = self.CI_List[4].text()

        rootDigitalEvidence = Element('DigitalEvidence')
        Information = SubElement(rootDigitalEvidence, 'Information')
        DigitalEvidenceSerialNo = SubElement(Information, 'DigitalEvidenceSerialNo')
        DigitalEvidenceGather = SubElement(Information, 'DigitalEvidenceGather')
        DigitalEvidenceGatherInformation = SubElement(DigitalEvidenceGather, 'DigitalEvidenceGatherInformation')
        DateTime = SubElement(DigitalEvidenceGatherInformation, 'DateTime')
        Location = SubElement(DigitalEvidenceGatherInformation, 'Location')
        LocationName = SubElement(Location, 'LocationName')
        Person = SubElement(DigitalEvidenceGatherInformation, 'LocationName')
        GatherOrganizationPartyName = SubElement(Person, 'GatherOrganizationPartyName')
        GatherOrganizationCode = SubElement(Person, 'GatherOrganizationCode')
        GatherOrganizationName = SubElement(Person, 'GatherOrganizationName')
        Source = SubElement(DigitalEvidenceGatherInformation, 'Source')
        GatherSourceName = SubElement(Source, 'GatherSourceName')
        RelationPerson = SubElement(DigitalEvidenceGatherInformation, 'RelationPerson')
        GatherRelationPersonName = SubElement(RelationPerson, 'GatherRelationPersonName')
        GatherRelationPersonTypeCode = SubElement(RelationPerson, 'GatherRelationPersonTypeCode')
        GatherAuthentication = SubElement(DigitalEvidenceGatherInformation, 'GatherAuthentication')
        FileMeta_GatherAuthentication = SubElement(GatherAuthentication, 'FileMeta')
        Name_GatherAuthentication = SubElement(FileMeta_GatherAuthentication, 'Name')
        Name_GatherAuthentication.text = 'None'
        SizeNumeric_GatherAuthentication = SubElement(FileMeta_GatherAuthentication, 'SizeNumeric')
        SizeNumeric_GatherAuthentication.text = '0'
        DigitalEvidenceTypeCode = SubElement(Information, 'DigitalEvidenceTypeCode')
        DigitalEvidenceFile = SubElement(Information, 'DigitalEvidenceFile')
        FileMeta_DigitalEvidenceFile = SubElement(DigitalEvidenceFile, 'FileMeta')
        Name_DigitalEvidenceFile = SubElement(FileMeta_DigitalEvidenceFile, 'Name')
        Name_DigitalEvidenceFile.text = ' '
        SizeNumeric_DigitalEvidenceFile = SubElement(FileMeta_DigitalEvidenceFile, 'SizeNumeric')
        SizeNumeric_DigitalEvidenceFile.text = ' '


        for list in self.DE_AddAll_List:
            LocationName.text = list[18].text()
            GatherOrganizationPartyName.text = list[19].text()
            DateTime.text = list[20].text()
            GatherOrganizationName.text = list[21].text()
            GatherOrganizationCode.text = list[23].text()
            GatherRelationPersonName.text = list[24].text()
            GatherRelationPersonTypeCode.text = list[26].text()
            GatherSourceName.text = list[28].text()
            DigitalEvidenceSerialNo.text = list[50].text()
            DigitalEvidenceTypeCode.text = list[51].text()

        rootHistory = Element('History')
        DigitalEvidencePackHistoryTypeCode = SubElement(rootHistory, 'DigitalEvidencePackHistoryTypeCode')
        DigitalEvidencePackHistoryStartDateTime = SubElement(rootHistory, 'DigitalEvidencePackHistoryStartDateTime')
        DigitalEvidencePackHistoryStartDateTime.text = ' ' # 시작시간 체크
        DigitalEvidencePackHistoryEndDateTime = SubElement(rootHistory, 'DigitalEvidencePackHistoryEndDateTime')
        DigitalEvidencePackHistoryEndDateTime.text = ' '

        for list in self.Log_List:
            DigitalEvidencePackHistoryTypeCode.text = list[3].text() #encoding="utf-8"

        treeDigitalEvidence = ElementTree(rootDigitalEvidence)
        treeDigitalEvidence.write(self.file_path + '_' + DigitalEvidencePackManagementIdentifier.text + '.xml')

        DigitalEvidencePackSizeNumeric.text = str(os.path.getsize(self.file_path + '_' + DigitalEvidencePackManagementIdentifier.text + '.xml'))
        if os.path.isfile(self.file_path + '_' + DigitalEvidencePackManagementIdentifier.text + '.xml'):
            os.remove(self.file_path + '_' + DigitalEvidencePackManagementIdentifier.text + '.xml')

        rootDigitalEvidencePack.append(rootManagement)
        rootDigitalEvidencePack.append(rootAgency)
        rootDigitalEvidencePack.append(rootDigitalEvidence)
        rootDigitalEvidencePack.append(rootHistory)

        def indent(elem, level=0):
            i = "\n" + level * "   "
            if len(elem):
                if not elem.text or not elem.text.strip():
                    elem.text = i + "   "
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
                for elem in elem:
                    indent(elem, level + 1)
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
            else:
                if level and (not elem.tail or not elem.tail.strip()):
                    elem.tail = i

        indent(rootDigitalEvidencePack)

        treeDigitalEvidencePack = ElementTree(rootDigitalEvidencePack)
        treeDigitalEvidencePack.write(self.file_path + '.xml')

    def ExportButton_exporttojsonfile(self):

        q_number = [0]
        dict_json = {}
        dict_json['Digital Evidence Package'] = {}

        ### Case Information ###
        dict_CI = dict()
        dict_json['Digital Evidence Package']['Case Info'] = {"case_management_id": self.CI_List[0].text(),
                                                              "agency_case_no.": self.CI_List[1].text(),
                                                              "agency_organization_code": self.CI_List[2].text(),
                                                              "agency_organization_name": self.CI_List[3].text(),
                                                              "agency_organization_party_name": self.CI_List[4].text(),
                                                              "contents_of_request": self.CI_List[5].text(),
                                                              "case_summary": self.CI_List[6].text(),
                                                              "case_description": self.CI_List[7].text(),
                                                              "case_datetime": self.CI_List[8].text(),
                                                              "ordering_datetime": self.CI_List[9].text()}

        ### Digital Evidence ###
        dict_DE = dict()
        list_DE = []
        list_DE_Gather_Info = []
        for list in self.DE_AddAll_List:
            tmp_dict = {}

            #

            tmp_dict['Vessel Info'] = {'vessel_name': list[0].text(), 'vessel_management_id': list[1].text(),
                                       'vessel_MMSI': list[2].text(), 'vessel_callsign': list[3].text(),
                                       'vessel_IMO': list[4].text(), 'vessel_MRN': list[5].text(),
                                       'vessel_tonnage': list[6].text(), 'vessel_length': list[7].text(),
                                       'total_number_of_equipment_with_track': list[8].text(),
                                       'vessel_type': list[9].text()}
            #

            #
            tmp_dict['Marine Electronics Info'] = {'device_management_id': list[10].text(),
                                                   'device_type': list[11].text(),
                                                   'device_manufacturer': list[12].text(),
                                                   'device_model_name': list[13].text(),
                                                   'device_model_serial_number': list[14].text(),
                                                   'device_os_firmware': list[15].text(),
                                                   'device_description': list[16].text()}
            #

            ##
            tmp_dict['Gather Info'] = {'gather_no': list[17].text(), 'gather_location': list[18].text(),
                                       'gather_person_name': list[19].text(),
                                       'gather_datetime': list[20].text(), 'gather_person_agency': list[21].text(),
                                       'gather_person_rank': list[22].text(),
                                       'gather_organization_code': list[23].text(),
                                       'submitter_name': list[24].text(),
                                       'gather_source_name': list[25].text(),
                                       'gather_relation_person_type_code': list[26].text()}
            tmp_list = []
            for list in self.DE_AddAll_List:
                tmp_list.append({'gather_media_type': list[28].text(), 'gather_hash_type': list[29].text(),
                                 'gather_hash': list[30].text(), 'gather_path': list[31].text(),
                                       'gather_metadata': list[32].text()})
            tmp_dict['Gather Info']['Gather Info Media File'] = tmp_list
            ##

            ###
            tmp_list = []
            for other_files_list in self.DE_AddAll_List:
                tmp_list.append(
                    {'other_files_id': other_files_list[34].text(), 'other_files_type': other_files_list[35].text(),
                     'other_files_size': other_files_list[36].text(), 'other_files_path': other_files_list[37].text(),
                     'other_files_hash_type': other_files_list[38].text(),
                     'other_files_hash_value': other_files_list[39].text(),
                     'other_files_file_description': other_files_list[40].text(),
                     'other_files_file_metadata': other_files_list[41].text()})
            tmp_dict['Other Files'] = tmp_list
            ###

            # ### Acquisition #1
            tmp_list = []
            for list in self.DE_AddAll_List:
                tmp_list.append({'authentication_id': list[42].text(),
                  'authentication_person_name': list[43].text(),
                'authentication_date_time': list[44].text(),
                 'authentication_location': list[45].text(),
               'authentication_tool': list[46].text(),
                                 'authentication_tool_version': list[47].text(),
                                 'authentication_person_party_name': list[48].text()
                                 })

            tmp_dict['Authentication Info'] = tmp_list


            #Acquisition #2
            tmp_list = []
            for acquisition_list in self.DE_AddAll_List:
                tmp_list.append({'serial_no': acquisition_list[49].text(),
                         'management_id': acquisition_list[50].text(),
                     'digital_evidence_type': acquisition_list[51].text(),
                     'evidences_gathering_type': acquisition_list[52].text(),
                     'gather_no': acquisition_list[53].text(),

                     'file_name': acquisition_list[55].text(),

                     'file_path': acquisition_list[56].text() ,
                     'hash_type': acquisition_list[57].text(),
                     'hash_value': acquisition_list[58].text(),
                     'sector_size': acquisition_list[59].text(),
                    'file_size': acquisition_list[60].text(),
                    'metadata': acquisition_list[61].text()
                        })

            for q in q_number:
                tmp_dict['Authentication Info'][q]['Digital Evidence Files'] = tmp_list


            list_DE.append(tmp_dict)

        dict_json['Digital Evidence Package']["Digital Evidences"] = list_DE

        ### Analysis Information other files### #!
        dict_AI = dict()
        dict_json['Digital Evidence Package']["Analysis Info"] = dict()

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

        list_AIOtherFiles = []
        for list in self.AI_List:
            list_AIOtherFiles.append(
                {"id": list[1].text(), "type": list[2].text(), "file_size": list[3].text(),
                 "file_path": list[4].text(),
                 "file_hash_type": list[5].text(), "file_hash_value": list[6].text(),
                 "file_description": list[7].text(), "file_metadata": list[8].text()})
        dict_json['Digital Evidence Package']['Analysis Info']['Other Files'] = list_AIOtherFiles

        # Log
        list_Log = []
        for list in self.Log_List:
            list_Log.append(
                {'digital_evidence_package_management_id': list[0].text(),
                 'log_history_start_date_time': list[1].text(),
                 'log_history_end_date_time': str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))),
                 'log_type': list[3].text(), 'log_description': list[4].text(),
                 'devision_name_of_logger': list[5].text(),
                 'team_name_of_logger': list[6].text(), 'rank_of_logger': list[7].text(),
                 'name_of_logger': list[8].text()
                 }
            )
        dict_json['Log'] = list_Log

        with open(self.file_path, "w", encoding='utf-8') as json_file:
            json_file.write(json.dumps(dict_json, ensure_ascii=False))

        self.MessageBox("증거팩 파일 생성이 완료되었습니다.")

    def MessageBox(self, str):
        msg = QMessageBox()
        msg.setText(str)
        msg.setWindowTitle("완료")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

        # DE Gather Info Browse버튼 클릭하면 파일 입력

        # <Browse>


    def DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog(self, a, b):
        file_name = QFileDialog.getOpenFileName(filter="JPG File (*.jpg);; JPEG File (*.jpeg);; MP3 File (*.mp3);; MP4 File (*.mp4)") #JPG File (*.jpg);; JPEG File (*.jpeg);;

        self.DE_Gather_Info_List[a][b][0].setText(file_name[0])

        # DE Other Files Browse누르면 파일 업로드

    def DE_other_files_file_browse__browseButton_1_QFileDialog(self, a, b):
        file_name = QFileDialog.getOpenFileName()

        self.DE_Other_Files_Info_List[a][b][0].setText(file_name[0])

    def DE_Acquisition_Info_DEF_browse__browseButton_1_QFileDialog(self, a, b):
        file_name = QFileDialog.getOpenFileName()
        self.DE_Acquisition_Info_DEF_List[a][b][0].setText(file_name[0])

        # <Gather에는 jpg, mp4>


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

            input_file = file_path
            exe = "hachoir-metadata.exe"
            process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            out_list = []
            for output in process.stdout:
                if 'Metadata' in output:
                    continue
                output = output.replace('\n', ', ')
                output = output.replace('-', '')
                out_list.append(output)

            result = ""
            for i in out_list:
                result = result + i

        self.DE_Gather_Info_List[a][b][1].setText(file_name[file_name.rfind(".") + 1:])
        self.DE_Gather_Info_List[a][b][2].setText("SHA-256")
        self.DE_Gather_Info_List[a][b][3].setText(sha256.hexdigest())
        self.DE_Gather_Info_List[a][b][4].setText(copy_file_path)
        self.DE_Gather_Info_List[a][b][5].setText(str(result))

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
            ###################
            file2 = open(file_path, 'rb')
            magic = file2.read(8)
            magic.hex()

            self.DE_Other_Files_Info_List[a][b][2].setText(file_name[file_name.rfind(".") + 1:])
            self.DE_Other_Files_Info_List[a][b][3].setText(str(file_size))
            self.DE_Other_Files_Info_List[a][b][4].setText(copy_file_path)
            self.DE_Other_Files_Info_List[a][b][5].setText("SHA-256")
            self.DE_Other_Files_Info_List[a][b][6].setText(sha256.hexdigest())

            if magic.hex() == 'ffd8ffe000104a46' or magic.hex() == '0000001466747970':

                input_file = file_path
                exe = "hachoir-metadata"
                process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                out_list = []
                for output in process.stdout:
                    if 'Metadata' in output:
                        continue
                    output = output.replace('\n', ', ')
                    output = output.replace('-', '')
                    out_list.append(output)

                result = ""
                for i in out_list:
                    result = result + i

                self.DE_Other_Files_Info_List[a][b][8].setText(str(result))


            else:
                file_path = file_path
                with open(file_path, 'rb') as file:
                    content = file.read()

                    # 이름
                    file_name = file_path[file_path.rfind("/") + 1:]

                    # 유형
                    file_signature = file_path[file_path.rfind(".") + 1:]

                    # 크기
                    file_size = os.path.getsize(file_path)

                    # 수정한 날짜
                    modified_time = time.ctime(os.path.getmtime(file_path))

                    chiwon = str("파일 이름: ") + str(file_name) + str(", ") \
                             + str("파일 유형: ") + str(file_signature) + str(", ") \
                             + str("파일 크기: ") + str(file_size) + str(", ") \
                             + str("수정한 날짜: ") + str(modified_time)

                self.DE_Other_Files_Info_List[a][b][8].setText(chiwon)

    def DE_Acquisition_Info_DEF_browse__enterButton_1_Calculate(self, a, b):
        file_path = self.DE_Acquisition_Info_DEF_List[a][b][0].text()
        file_name = file_path[file_path.rfind("/") + 1:]
        copy_file_path = ".\\디지털 증거\\수집 정보\\" + file_name
        if os.path.isdir(".\\디지털 증거\\수집 정보") == False:
            os.makedirs(".\\디지털 증거\\수집 정보")
        copyfile(file_path, copy_file_path)

        with open(copy_file_path, 'rb') as file:
            content = file.read()
            sha256 = hashlib.sha256()
            sha256.update(content)

            file2 = open(file_path, 'rb')
            magic = file2.read(8)
            magic.hex()

            self.DE_Acquisition_Info_DEF_List[a][b][1].setText(file_name)  # 디지털 증거 파일 이름
            self.DE_Acquisition_Info_DEF_List[a][b][2].setText(copy_file_path)  # 디지털 증거 파일 경로
            self.DE_Acquisition_Info_DEF_List[a][b][3].setText("SHA-256")  # 해시 종류
            self.DE_Acquisition_Info_DEF_List[a][b][4].setText(sha256.hexdigest())  # 해시 값

            if magic.hex() == 'ffd8ffe000104a46' or magic.hex() == '0000001466747970':

                input_file = file_path
                exe = "hachoir-metadata"
                process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                out_list = []
                for output in process.stdout:
                    if 'Metadata' in output:
                        continue
                    output = output.replace('\n', ', ')
                    output = output.replace('-', '')
                    out_list.append(output)

                result = ""
                for i in out_list:
                    result = result + i

                self.DE_Acquisition_Info_DEF_List[a][b][6].setText(str(result))


            else:
                file_path = file_path
                with open(file_path, 'rb') as file:
                    content = file.read()

                    # 이름
                    file_name = file_path[file_path.rfind("/") + 1:]

                    # 유형
                    file_signature = file_path[file_path.rfind(".") + 1:]

                    # 크기
                    file_size = os.path.getsize(file_path)

                    # 수정한 날짜
                    modified_time = time.ctime(os.path.getmtime(file_path))

                    chiwon = str("파일 이름: ") + str(file_name) + str(", ") \
                             + str("파일 유형: ") + str(file_signature) + str(", ") \
                             + str("파일 크기: ") + str(file_size) + str(", ") \
                             + str("수정한 날짜: ") + str(modified_time)

                self.DE_Acquisition_Info_DEF_List[a][b][6].setText(chiwon)

        ## AI Report Browse 버튼 클릭하면 파일 업로드


    def DE_Gather_Info_AddTab(self, a):



        tmp_tab_8 = QtWidgets.QWidget()
        tmp_tab_8.setObjectName("tab_8")
        tmp_gridLayout_27 = QtWidgets.QGridLayout(tmp_tab_8)
        tmp_gridLayout_27.setObjectName("gridLayout_27")
        tmp_DE_Gather_Info_file__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file__horizontalLayout_1.setObjectName("DE_Gather_Info_file__horizontalLayout_1")
        tmp_DE_Gather_Info_file__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_8)
        tmp_DE_Gather_Info_file__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Gather_Info_file__scrollArea_1.setObjectName("DE_Gather_Info_file__scrollArea_1")
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -139, 381, 219))
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
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_metadata__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_metadata__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_metadata__label_1.setObjectName("DE_Gather_Info_gather_metadata__label_1")
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_metadata__label_1)
        tmp_DE_Gather_Info_gather_metadata__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_metadata__lineEdit_1.setObjectName("DE_Gather_Info_gather_metadata__lineEdit_1")
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_metadata__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1)
        tmp_gridLayout_18.addLayout(tmp_DE_Gather_Info_file__verticalLayout_1, 1, 0, 1, 1)
        tmp_DE_Gather_Info_file__scrollArea_1.setWidget(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__scrollArea_1)
        tmp_gridLayout_27.addLayout(tmp_DE_Gather_Info_file__horizontalLayout_1, 0, 0, 1, 1)
        self.DE_Gather_Info_Tab_Widget_List[a].addTab(tmp_tab_8, "Tab" + str(len(self.DE_Gather_Info_List[a]) + 1))




        tmp_list = list()
        tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_metadata__lineEdit_1)
        self.DE_Gather_Info_List[a].append(tmp_list)

        gather_info_button_list = list()
        gather_info_button_list.append(tmp_DE_Gather_Info_file__filebrowse__browseButton_1)
        gather_info_button_list.append(tmp_DE_Gather_Info_file__filebrowse__enterButton_1)
        self.DE_Gather_Info_Button_List[a].append(gather_info_button_list)

        tmp_len = len(self.DE_Gather_Info_Button_List[a])-1
        self.DE_Gather_Info_Button_List[a][tmp_len][0].clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog(a, tmp_len)
        )
        self.DE_Gather_Info_Button_List[a][tmp_len][1].clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__enterButton_1_Calculate(a, tmp_len)
        )



        tmp_DE_Gather_Info_file__filebrowse__label_1.setText("파일 입력")
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.setText("Browse...")
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.setText("Enter")

        tmp_DE_Gather_Info_gather_media_type__label_1.setText("채증 미디어 유형:")
        tmp_DE_Gather_Info__gather_hash_type__label_1.setText("채증 미디어 해시 종류:")
        tmp_DE_Gather_Info_gather_hash__label_1.setText("채증 미디어 해시값")
        tmp_DE_Gather_Info_gather_path__label_1.setText("채증 미디어 경로:")
        tmp_DE_Gather_Info_gather_metadata__label_1.setText("파일 메타데이터:")

    def DE_Other_Files_AddTab(self): # tab_4

        tmp_tab_4 = QtWidgets.QWidget()
        tmp_tab_4.setObjectName("tab_4")
        tmp_gridLayout_9 = QtWidgets.QGridLayout(tmp_tab_4)
        tmp_gridLayout_9.setObjectName("gridLayout_9")
        tmp_DE_other_files__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_4)
        tmp_DE_other_files__scrollArea_1.setWidgetResizable(True)
        tmp_DE_other_files__scrollArea_1.setObjectName("DE_other_files__scrollArea_1")
        tmp_DE_other_files__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_other_files__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 385, 312))
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
        tmp_gridLayout_9.addWidget(tmp_DE_other_files__scrollArea_1, 0, 0, 1, 1)
        self.tabWidget_7.addTab(tmp_tab_4, "Tab" + str(len(self.DE_Other_Files_Info_List) + 1))

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
        self.DE_Other_Files_Info_List.append(tmp_list)

        tmp_DE_other_files_file_browse__label_1.setText("파일 입력:")
        tmp_DE_other_files_file_browse__browseButton_1.setText("Browse...")
        tmp_DE_other_files_file_browse__EnterButton_1.setText("Enter")

        tmp_DE_other_files_id__label_1.setText("고유번호:")
        tmp_DE_other_files_type__label_1.setText("파일유형:")
        tmp_DE_other_files_file_size__label_1.setText("파일크기:")
        tmp_DE_other_files_file_path__label_1.setText("파일 경로:")
        tmp_DE_other_files_file_hash_type__label_1.setText("해시 종류:")
        tmp_DE_other_files_file_hash_value__label_1.setText("해시값:")
        tmp_DE_other_files_file_description__label_1.setText("파일 설명:")
        tmp_DE_other_files_file_metadata__label_1.setText("파일 메타데이터:")

    def DE_Acquisition_Info_AddTab(self):
        tmp_tab_6 = QtWidgets.QWidget()
        tmp_tab_6.setObjectName("tab_6")
        tmp_gridLayout_29 = QtWidgets.QGridLayout(tmp_tab_6)
        tmp_gridLayout_29.setObjectName("gridLayout_29")
        tmp_DE_Acquisition_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_6)
        tmp_DE_Acquisition_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Acquisition_Info__scrollArea_1.setObjectName("DE_Acquisition_Info__scrollArea_1")
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -2, 372, 449))
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1.setObjectName("DE_Acquisition_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_4 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_4.setObjectName("gridLayout_4")
        tmp_DE_Acquisition_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__verticalLayout_1.setObjectName("DE_Acquisition_Info__verticalLayout_1")
        tmp_DE_Authentication_ID__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Authentication_ID__horizontalLayout_1.setObjectName("DE_Authentication_ID__horizontalLayout_1")
        tmp_DE_Authentication_ID__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_ID__label_1.setObjectName("DE_Authentication_ID__label_1")
        tmp_DE_Authentication_ID__horizontalLayout_1.addWidget(tmp_DE_Authentication_ID__label_1)
        tmp_DE_Authentication_ID__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_ID__lineEdit_1.setObjectName("DE_Authentication_ID__lineEdit_1")
        tmp_DE_Authentication_ID__horizontalLayout_1.addWidget(tmp_DE_Authentication_ID__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Authentication_ID__horizontalLayout_1)
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
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.setObjectName("DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1.setObjectName("DE_Acquisition_Info_acquisition_tool_version__label_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_tool_version__label_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_tool_version__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1)
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.setObjectName("DE_Authentication_Person_Party_Name__horizontalLayout_1")
        tmp_DE_Authentication_Person_Party_Name__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_Person_Party_Name__label_1.setObjectName("DE_Authentication_Person_Party_Name__label_1")
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(tmp_DE_Authentication_Person_Party_Name__label_1)
        tmp_DE_Authentication_Person_Party_Name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_Person_Party_Name__lineEdit_1.setObjectName("DE_Authentication_Person_Party_Name__lineEdit_1")
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(tmp_DE_Authentication_Person_Party_Name__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1)
        tmp_gridLayout_4.addLayout(tmp_DE_Acquisition_Info__verticalLayout_1, 0, 0, 1, 1)
        tmp_tabWidget_10 = QtWidgets.QTabWidget(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_tabWidget_10.setObjectName("tabWidget_10")
        tmp_tab_9 = QtWidgets.QWidget()
        tmp_tab_9.setObjectName("tab_9")
        tmp_gridLayout_17 = QtWidgets.QGridLayout(tmp_tab_9)
        tmp_gridLayout_17.setObjectName("gridLayout_17")
        tmp_DE_Acquisition_Info_file__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_9)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setObjectName("DE_Acquisition_Info_file__scrollArea_1")
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -356, 381, 436))
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setObjectName("DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1")
        tmp_gridLayout_15 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_15.setObjectName("gridLayout_15")
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.setObjectName("DE_Acquisition_Info__DEF_file__verticalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__label_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_serial_no__label_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_management_id__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_management_id__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__label_1.setObjectName("DE_Acquisition_Info_DEF_management_id__label_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_management_id__label_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_management_id__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__label_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__label_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_gather_no__label_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_browse__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setObjectName("DE_Acquisition_Info_DEF_browse__label_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__label_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_browse__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1 = QtWidgets.QPushButton(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1.setObjectName("DE_Acquisition_Info_DEF_browse__browseButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__browseButton_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1 = QtWidgets.QPushButton(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1.setObjectName("DE_Acquisition_Info_DEF_browse__enterButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__enterButton_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_type__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_value__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__label_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_sector_size__label_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_file_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_file_size__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__label_1.setObjectName("DE_Acquisition_Info_DEF_file_size__label_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_file_size__label_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_file_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF__metadata__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__metadata__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__label_1.setObjectName("DE_Acquisition_Info_DEF__metadata__label_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__metadata__label_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF__metadata__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1)
        tmp_gridLayout_15.addLayout(tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidget(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_17.addWidget(tmp_DE_Acquisition_Info_file__scrollArea_1, 0, 0, 1, 1)
        tmp_tabWidget_10.addTab(tmp_tab_9, "")
        tmp_gridLayout_4.addWidget(tmp_tabWidget_10, 2, 0, 1, 1)
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF__addButton__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__label_1.setObjectName("DE_Acquisition_Info_DEF__label_1")
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__label_1)
        tmp_DE_Acquisition_Info_DEF__addButton_1 = QtWidgets.QPushButton(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__addButton_1.setObjectName("DE_Acquisition_Info_DEF__addButton_1")
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__addButton_1)
        tmp_gridLayout_4.addLayout(tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1, 1, 0, 1, 1)
        tmp_DE_Acquisition_Info__scrollArea_1.setWidget(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_29.addWidget(tmp_DE_Acquisition_Info__scrollArea_1, 0, 0, 1, 1)
        self.tabWidget_8.addTab(tmp_tab_6, "Tab" + str(len(self.DE_Acquisition_Info_List) +1))

        tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setPlaceholderText("ex) 2021-11-30-19:58:13.829475+09:00")

        tmp_list = list()
        tmp_list.append(tmp_DE_Authentication_ID__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)
        tmp_list.append(tmp_DE_Authentication_Person_Party_Name__lineEdit_1)

        tmp_list.append(tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)

        self.DE_Acquisition_Info_List.append(tmp_list)

        _translate = QtCore.QCoreApplication.translate

        tmp_DE_Authentication_ID__label_1.setText("수집 id:")
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1.setText("수집자명:")
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1.setText("수집 시간:")

        tmp_DE_Gather_Info_gather_datetime__lineEdit_1.setPlaceholderText(
            _translate("SecondWindow", "ex) 2021-11-30 19:58:13.829475+09:00"))
        tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setPlaceholderText(
            _translate("SecondWindow", "ex) 2021-11-30 19:58:13.829475+09:00"))



        tmp_DE_Acquisition_Info_acquisition_location__label_1.setText("수집 장소:")
        tmp_DE_Acquisition_Info_acquisition_tool__label_1.setText("수집 도구:")
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1.setText("수집 도구 버젼:")
        tmp_DE_Authentication_Person_Party_Name__label_1.setText("수집 부서:")

        tmp_DE_Acquisition_Info_DEF__label_1.setText("디지털 증거 파일")
        tmp_DE_Acquisition_Info_DEF__addButton_1.setText("+추가")

        tmp_tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_9), _translate("SecondWindow", "Tab 1"))


        tmp_DE_Acquisition_Info_DEF_serial_no__label_1.setText("일련번호:")
        tmp_DE_Acquisition_Info_DEF_management_id__label_1.setText("관리 번호:")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setText("디지털 증거 유형:")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setText("증거 채증 유형:")
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1.setText("채증 번호:")

        tmp_DE_Acquisition_Info_DEF_browse__label_1.setText("파일 입력:")
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1.setText("Browse...")
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1.setText("Enter")


        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setText("디지털 증거 파일 이름:")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setText("디지털 증거 파일:")
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1.setText("해시 종류:")
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1.setText("해시값:")
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1.setText("섹터 크기:")
        tmp_DE_Acquisition_Info_DEF_file_size__label_1.setText("파일 크기:")
        tmp_DE_Acquisition_Info_DEF__metadata__label_1.setText("파일 메타데이터:")

    def DE_Acquisition_Info_DEF_AddTab(self):

        tmp_tab_9 = QtWidgets.QWidget()
        tmp_tab_9.setObjectName("tab_9")
        tmp_gridLayout_17 = QtWidgets.QGridLayout(tmp_tab_9)
        tmp_gridLayout_17.setObjectName("gridLayout_17")
        tmp_DE_Acquisition_Info_file__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_9)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setObjectName("DE_Acquisition_Info_file__scrollArea_1")
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -356, 381, 436))
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setObjectName("DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1")
        tmp_gridLayout_15 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_15.setObjectName("gridLayout_15")
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.setObjectName("DE_Acquisition_Info__DEF_file__verticalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__label_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_serial_no__label_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_management_id__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_management_id__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__label_1.setObjectName("DE_Acquisition_Info_DEF_management_id__label_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_management_id__label_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_management_id__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__label_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__label_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_gather_no__label_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_browse__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setObjectName("DE_Acquisition_Info_DEF_browse__label_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__label_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_browse__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1 = QtWidgets.QPushButton(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1.setObjectName("DE_Acquisition_Info_DEF_browse__browseButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__browseButton_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1 = QtWidgets.QPushButton(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1.setObjectName("DE_Acquisition_Info_DEF_browse__enterButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__enterButton_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_type__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_value__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__label_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_sector_size__label_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_file_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_file_size__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__label_1.setObjectName("DE_Acquisition_Info_DEF_file_size__label_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_file_size__label_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_file_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF__metadata__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__metadata__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__label_1.setObjectName("DE_Acquisition_Info_DEF__metadata__label_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__metadata__label_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF__metadata__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1)
        tmp_gridLayout_15.addLayout(tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidget(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_17.addWidget(tmp_DE_Acquisition_Info_file__scrollArea_1, 0, 0, 1, 1)
        self.tabWidget_10.addTab(tmp_tab_9, "Tab" + str(len(self.DE_Acquisition_Info_DEF_List) +1))

        tmp_list = list()
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        self.DE_Acquisition_Info_DEF_List.append(tmp_list)

        tmp_DE_Acquisition_Info_DEF_serial_no__label_1.setText("일련번호:")
        tmp_DE_Acquisition_Info_DEF_management_id__label_1.setText("관리 번호:")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setText("디지털 증거 유형:")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setText("증거 채증 유형:")
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1.setText("채증 번호:")

        tmp_DE_Acquisition_Info_DEF_browse__label_1.setText("파일 입력:")
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1.setText("Browse...")
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1.setText("Enter")

        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setText("디지털 증거 파일 이름:")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setText("디지털 증거 파일:")
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1.setText("해시 종류:")
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1.setText("해시값:")
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1.setText("섹터 크기:")
        tmp_DE_Acquisition_Info_DEF_file_size__label_1.setText("파일 크기:")
        tmp_DE_Acquisition_Info_DEF__metadata__label_1.setText("파일 메타데이터:")

    def DE_AddTab(self):

        self.DE_Gather_Info_List.append(list())
        self.DE_Gather_Info_Button_List.append(list())

        tmp_tab_2 = QtWidgets.QWidget()
        tmp_tab_2.setObjectName("tab_2")
        tmp_gridLayout_26 = QtWidgets.QGridLayout(tmp_tab_2)
        tmp_gridLayout_26.setObjectName("gridLayout_26")
        tmp_DE_Digitlal_Evidence__label = QtWidgets.QLabel(tmp_tab_2)
        tmp_DE_Digitlal_Evidence__label.setObjectName("DE_Digitlal_Evidence__label")
        tmp_gridLayout_26.addWidget(tmp_DE_Digitlal_Evidence__label, 0, 0, 1, 1)
        tmp_DE__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_2)
        tmp_DE__scrollArea_1.setWidgetResizable(True)
        tmp_DE__scrollArea_1.setObjectName("DE__scrollArea_1")
        tmp_DE__scrollAreaWidgetContents = QtWidgets.QWidget()
        tmp_DE__scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1308, 571))
        tmp_DE__scrollAreaWidgetContents.setObjectName("DE__scrollAreaWidgetContents")
        tmp_gridLayout_7 = QtWidgets.QGridLayout(tmp_DE__scrollAreaWidgetContents)
        tmp_gridLayout_7.setObjectName("gridLayout_7")
        tmp_DE_Gather_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_Gather_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Gather_Info__scrollArea_1.setObjectName("DE_Gather_Info__scrollArea_1")
        tmp_DE_Gather_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Gather_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -176, 372, 544))
        tmp_DE_Gather_Info__scrollAreaWidgetContents_1.setObjectName("DE_Gather_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_3 = QtWidgets.QGridLayout(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_3.setObjectName("gridLayout_3")
        tmp_DE_Gather_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Gather_Info__verticalLayout_1.setObjectName("DE_Gather_Info__verticalLayout_1")
        tmp_DE_Gather_Info_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_no__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_no__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_no__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_no__label_1.setObjectName("DE_Gather_Info_gather_no__label_1")
        tmp_DE_Gather_Info_gather_no__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_no__label_1)
        tmp_DE_Gather_Info_gather_no__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_no__lineEdit_1.setObjectName("DE_Gather_Info_gather_no__lineEdit_1")
        tmp_DE_Gather_Info_gather_no__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_no__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_no__horizontalLayout_1)
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
        tmp_DE_Gather_Info_organization_code__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_organization_code__horizontalLayout_1.setObjectName("DE_Gather_Info_organization_code__horizontalLayout_1")
        tmp_DE_Gather_Info_organization_code__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_organization_code__label_1.setObjectName("DE_Gather_Info_organization_code__label_1")
        tmp_DE_Gather_Info_organization_code__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_organization_code__label_1)
        tmp_DE_Gather_Info_organization_code__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_organization_code__lineEdit_1.setObjectName("DE_Gather_Info_organization_code__lineEdit_1")
        tmp_DE_Gather_Info_organization_code__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_organization_code__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_organization_code__horizontalLayout_1)
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1.setObjectName("DE_Gather_Info_submitter_name__horizontalLayout_1")
        tmp_DE_Gather_Info_submitter_name__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_submitter_name__label_1.setObjectName("DE_Gather_Info_submitter_name__label_1")
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_submitter_name__label_1)
        tmp_DE_Gather_Info_submitter_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_submitter_name__lineEdit_1.setObjectName("DE_Gather_Info_submitter_name__lineEdit_1")
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_submitter_name__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_submitter_name__horizontalLayout_1)
        tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1.setObjectName("DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1")
        tmp_DE_Gather_Inf_Gather_Source_Name__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Inf_Gather_Source_Name__label_1.setObjectName("DE_Gather_Inf_Gather_Source_Name__label_1")
        tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1.addWidget(tmp_DE_Gather_Inf_Gather_Source_Name__label_1)
        tmp_DE_Gather_Inf_Gather_Source_Name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Inf_Gather_Source_Name__lineEdit_1.setObjectName("DE_Gather_Inf_Gather_Source_Name__lineEdit_1")
        tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1.addWidget(tmp_DE_Gather_Inf_Gather_Source_Name__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1)
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1.setObjectName("DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1")
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1.setObjectName("DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1")
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1.addWidget(tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1)
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1.setObjectName("DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1")
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1.addWidget(tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1)
        tmp_gridLayout_3.addLayout(tmp_DE_Gather_Info__verticalLayout_1, 0, 0, 1, 1)
        tmp_tabWidget_9 = QtWidgets.QTabWidget(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_tabWidget_9.setObjectName("tabWidget_9")
        tmp_tab_8 = QtWidgets.QWidget()
        tmp_tab_8.setObjectName("tab_8")
        tmp_gridLayout_27 = QtWidgets.QGridLayout(tmp_tab_8)
        tmp_gridLayout_27.setObjectName("gridLayout_27")
        tmp_DE_Gather_Info_file__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file__horizontalLayout_1.setObjectName("DE_Gather_Info_file__horizontalLayout_1")
        tmp_DE_Gather_Info_file__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_8)
        tmp_DE_Gather_Info_file__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Gather_Info_file__scrollArea_1.setObjectName("DE_Gather_Info_file__scrollArea_1")
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -139, 381, 219))
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
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.setObjectName("DE_Gather_Info_gather_metadata__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_metadata__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_metadata__label_1.setObjectName("DE_Gather_Info_gather_metadata__label_1")
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_metadata__label_1)
        tmp_DE_Gather_Info_gather_metadata__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_metadata__lineEdit_1.setObjectName("DE_Gather_Info_gather_metadata__lineEdit_1")
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_metadata__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1)
        tmp_gridLayout_18.addLayout(tmp_DE_Gather_Info_file__verticalLayout_1, 1, 0, 1, 1)
        tmp_DE_Gather_Info_file__scrollArea_1.setWidget(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__scrollArea_1)
        tmp_gridLayout_27.addLayout(tmp_DE_Gather_Info_file__horizontalLayout_1, 0, 0, 1, 1)
        tmp_tabWidget_9.addTab(tmp_tab_8, "")
        tmp_gridLayout_3.addWidget(tmp_tabWidget_9, 2, 0, 1, 1)
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1.setObjectName("DE_Gather_Info_file_addButton__horizontalLayout_1")
        tmp_DE_Gather_Info_file__blanklabel_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__blanklabel_1.setObjectName("DE_Gather_Info_file__blanklabel_1")
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__blanklabel_1)
        tmp_DE_Gather_Info__addButton_1 = QtWidgets.QPushButton(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__addButton_1.setObjectName("DE_Gather_Info__addButton_1")
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1.addWidget(tmp_DE_Gather_Info__addButton_1)
        tmp_gridLayout_3.addLayout(tmp_DE_Gather_Info_file_addButton__horizontalLayout_1, 1, 0, 1, 1)
        tmp_DE_Gather_Info__scrollArea_1.setWidget(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_7.addWidget(tmp_DE_Gather_Info__scrollArea_1, 3, 1, 1, 1)
        tmp_DE_Vessel_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info__horizontalLayout_1.setObjectName("DE_Vessel_Info__horizontalLayout_1")
        tmp_DE_Vessel_Info__label_1 = QtWidgets.QLabel(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_Vessel_Info__label_1.setObjectName("DE_Vessel_Info__label_1")
        tmp_DE_Vessel_Info__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info__label_1)
        tmp_gridLayout_7.addLayout(tmp_DE_Vessel_Info__horizontalLayout_1, 0, 1, 1, 1)
        tmp_DE_Vessel_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_Vessel_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Vessel_Info__scrollArea_1.setObjectName("DE_Vessel_Info__scrollArea_1")
        tmp_DE_Vessel_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Vessel_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 372, 329))
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
        tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1.setPlaceholderText("")
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
        tmp_DE_Vessel_Type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Type__horizontalLayout_1.setObjectName("DE_Vessel_Type__horizontalLayout_1")
        tmp_DE_Vessel_Type__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Type__label_1.setObjectName("DE_Vessel_Type__label_1")
        tmp_DE_Vessel_Type__horizontalLayout_1.addWidget(tmp_DE_Vessel_Type__label_1)
        tmp_DE_Vessel_Type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Type__lineEdit_1.setObjectName("DE_Vessel_Type__lineEdit_1")
        tmp_DE_Vessel_Type__horizontalLayout_1.addWidget(tmp_DE_Vessel_Type__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Type__horizontalLayout_1)
        tmp_gridLayout_20.addLayout(tmp_DE_Vessel_Info__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Vessel_Info__scrollArea_1.setWidget(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_7.addWidget(tmp_DE_Vessel_Info__scrollArea_1, 1, 1, 1, 1)
        tmp_DE_Marines_Electronics_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_Marines_Electronics_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Marines_Electronics_Info__scrollArea_1.setObjectName("DE_Marines_Electronics_Info__scrollArea_1")
        tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 404, 236))
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
        tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.setObjectName("DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1")
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
        tmp_gridLayout_7.addWidget(tmp_DE_Marines_Electronics_Info__scrollArea_1, 1, 2, 1, 1)
        tmp_DE_Marine_Electronics_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marine_Electronics_Info__horizontalLayout_1.setObjectName("DE_Marine_Electronics_Info__horizontalLayout_1")
        tmp_DE_Marine_Electronics_Info__label_1 = QtWidgets.QLabel(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_Marine_Electronics_Info__label_1.setObjectName("DE_Marine_Electronics_Info__label_1")
        tmp_DE_Marine_Electronics_Info__horizontalLayout_1.addWidget(tmp_DE_Marine_Electronics_Info__label_1)
        tmp_gridLayout_7.addLayout(tmp_DE_Marine_Electronics_Info__horizontalLayout_1, 0, 2, 1, 1)
        tmp_DE_Gather_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info__horizontalLayout_1.setObjectName("DE_Gather_Info__horizontalLayout_1")
        tmp_DE_Gather_Info__label_1 = QtWidgets.QLabel(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_Gather_Info__label_1.setObjectName("DE_Gather_Info__label_1")
        tmp_DE_Gather_Info__horizontalLayout_1.addWidget(tmp_DE_Gather_Info__label_1)
        tmp_gridLayout_7.addLayout(tmp_DE_Gather_Info__horizontalLayout_1, 2, 1, 1, 1)
        tmp_DE_other_files__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files__horizontalLayout_1.setObjectName("DE_other_files__horizontalLayout_1")
        tmp_DE_other_files__label_1 = QtWidgets.QLabel(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_other_files__label_1.setObjectName("DE_other_files__label_1")
        tmp_DE_other_files__horizontalLayout_1.addWidget(tmp_DE_other_files__label_1)
        tmp_DE_other_files__addButton_1 = QtWidgets.QPushButton(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_other_files__addButton_1.setObjectName("DE_other_files__addButton_1")
        tmp_DE_other_files__horizontalLayout_1.addWidget(tmp_DE_other_files__addButton_1)
        tmp_gridLayout_7.addLayout(tmp_DE_other_files__horizontalLayout_1, 2, 2, 1, 1)
        tmp_tabWidget_7 = QtWidgets.QTabWidget(tmp_DE__scrollAreaWidgetContents)
        tmp_tabWidget_7.setObjectName("tabWidget_7")
        tmp_tab_4 = QtWidgets.QWidget()
        tmp_tab_4.setObjectName("tab_4")
        tmp_gridLayout_9 = QtWidgets.QGridLayout(tmp_tab_4)
        tmp_gridLayout_9.setObjectName("gridLayout_9")
        tmp_DE_other_files__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_4)
        tmp_DE_other_files__scrollArea_1.setWidgetResizable(True)
        tmp_DE_other_files__scrollArea_1.setObjectName("DE_other_files__scrollArea_1")
        tmp_DE_other_files__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_other_files__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 385, 312))
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
        tmp_gridLayout_9.addWidget(tmp_DE_other_files__scrollArea_1, 0, 0, 1, 1)
        tmp_tabWidget_7.addTab(tmp_tab_4, "")
        tmp_gridLayout_7.addWidget(tmp_tabWidget_7, 3, 2, 1, 1)
        tmp_DE_Acquisition_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info__horizontalLayout_1.setObjectName("DE_Acquisition_Info__horizontalLayout_1")
        tmp_DE_Acquisition_Info__label_1 = QtWidgets.QLabel(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_Acquisition_Info__label_1.setObjectName("DE_Acquisition_Info__label_1")
        tmp_DE_Acquisition_Info__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info__label_1)
        tmp_DE_Acquisition_Info__addButton_1 = QtWidgets.QPushButton(tmp_DE__scrollAreaWidgetContents)
        tmp_DE_Acquisition_Info__addButton_1.setObjectName("DE_Acquisition_Info__addButton_1")
        tmp_DE_Acquisition_Info__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info__addButton_1)
        tmp_gridLayout_7.addLayout(tmp_DE_Acquisition_Info__horizontalLayout_1, 0, 3, 1, 1)
        tmp_tabWidget_8 = QtWidgets.QTabWidget(tmp_DE__scrollAreaWidgetContents)
        tmp_tabWidget_8.setObjectName("tabWidget_8")
        tmp_tab_6 = QtWidgets.QWidget()
        tmp_tab_6.setObjectName("tab_6")
        tmp_gridLayout_29 = QtWidgets.QGridLayout(tmp_tab_6)
        tmp_gridLayout_29.setObjectName("gridLayout_29")
        tmp_DE_Acquisition_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_6)
        tmp_DE_Acquisition_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Acquisition_Info__scrollArea_1.setObjectName("DE_Acquisition_Info__scrollArea_1")
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -2, 372, 449))
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1.setObjectName("DE_Acquisition_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_4 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_4.setObjectName("gridLayout_4")
        tmp_DE_Acquisition_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__verticalLayout_1.setObjectName("DE_Acquisition_Info__verticalLayout_1")
        tmp_DE_Authentication_ID__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Authentication_ID__horizontalLayout_1.setObjectName("DE_Authentication_ID__horizontalLayout_1")
        tmp_DE_Authentication_ID__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_ID__label_1.setObjectName("DE_Authentication_ID__label_1")
        tmp_DE_Authentication_ID__horizontalLayout_1.addWidget(tmp_DE_Authentication_ID__label_1)
        tmp_DE_Authentication_ID__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_ID__lineEdit_1.setObjectName("DE_Authentication_ID__lineEdit_1")
        tmp_DE_Authentication_ID__horizontalLayout_1.addWidget(tmp_DE_Authentication_ID__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Authentication_ID__horizontalLayout_1)
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
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.setObjectName("DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1.setObjectName("DE_Acquisition_Info_acquisition_tool_version__label_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_tool_version__label_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1.setObjectName("DE_Acquisition_Info_acquisition_tool_version__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1)
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.setObjectName("DE_Authentication_Person_Party_Name__horizontalLayout_1")
        tmp_DE_Authentication_Person_Party_Name__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_Person_Party_Name__label_1.setObjectName("DE_Authentication_Person_Party_Name__label_1")
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(tmp_DE_Authentication_Person_Party_Name__label_1)
        tmp_DE_Authentication_Person_Party_Name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_Person_Party_Name__lineEdit_1.setObjectName("DE_Authentication_Person_Party_Name__lineEdit_1")
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(tmp_DE_Authentication_Person_Party_Name__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1)
        tmp_gridLayout_4.addLayout(tmp_DE_Acquisition_Info__verticalLayout_1, 0, 0, 1, 1)
        tmp_tabWidget_10 = QtWidgets.QTabWidget(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_tabWidget_10.setObjectName("tabWidget_10")
        tmp_tab_9 = QtWidgets.QWidget()
        tmp_tab_9.setObjectName("tab_9")
        tmp_gridLayout_17 = QtWidgets.QGridLayout(tmp_tab_9)
        tmp_gridLayout_17.setObjectName("gridLayout_17")
        tmp_DE_Acquisition_Info_file__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_9)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setObjectName("DE_Acquisition_Info_file__scrollArea_1")
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, -356, 381, 436))
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setObjectName("DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1")
        tmp_gridLayout_15 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_15.setObjectName("gridLayout_15")
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.setObjectName("DE_Acquisition_Info__DEF_file__verticalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__label_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_serial_no__label_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_management_id__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_management_id__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__label_1.setObjectName("DE_Acquisition_Info_DEF_management_id__label_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_management_id__label_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_management_id__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__label_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__label_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_gather_no__label_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_browse__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setObjectName("DE_Acquisition_Info_DEF_browse__label_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__label_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_browse__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1 = QtWidgets.QPushButton(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1.setObjectName("DE_Acquisition_Info_DEF_browse__browseButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__browseButton_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1 = QtWidgets.QPushButton(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1.setObjectName("DE_Acquisition_Info_DEF_browse__enterButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_browse__enterButton_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_type__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_value__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__label_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_sector_size__label_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF_file_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_file_size__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__label_1.setObjectName("DE_Acquisition_Info_DEF_file_size__label_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_file_size__label_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_file_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF__metadata__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__metadata__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__label_1.setObjectName("DE_Acquisition_Info_DEF__metadata__label_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__metadata__label_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1 = QtWidgets.QLineEdit(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF__metadata__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1)
        tmp_gridLayout_15.addLayout(tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidget(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_17.addWidget(tmp_DE_Acquisition_Info_file__scrollArea_1, 0, 0, 1, 1)
        tmp_tabWidget_10.addTab(tmp_tab_9, "")
        tmp_gridLayout_4.addWidget(tmp_tabWidget_10, 2, 0, 1, 1)
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.setObjectName("DE_Acquisition_Info_DEF__addButton__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__label_1.setObjectName("DE_Acquisition_Info_DEF__label_1")
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__label_1)
        tmp_DE_Acquisition_Info_DEF__addButton_1 = QtWidgets.QPushButton(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__addButton_1.setObjectName("DE_Acquisition_Info_DEF__addButton_1")
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__addButton_1)
        tmp_gridLayout_4.addLayout(tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1, 1, 0, 1, 1)
        tmp_DE_Acquisition_Info__scrollArea_1.setWidget(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_29.addWidget(tmp_DE_Acquisition_Info__scrollArea_1, 0, 0, 1, 1)
        tmp_tabWidget_8.addTab(tmp_tab_6, "")
        tmp_gridLayout_7.addWidget(tmp_tabWidget_8, 1, 3, 3, 1)
        tmp_DE__scrollArea_1.setWidget(tmp_DE__scrollAreaWidgetContents)
        tmp_gridLayout_26.addWidget(tmp_DE__scrollArea_1, 1, 0, 1, 1)
        self.tabWidget_3.addTab(tmp_tab_2, "Tab" + str(len(self.DE_AddAll_List) +1))

        self.DE_Gather_Info_Tab_Widget_List.append(tmp_tabWidget_9)


        tmp_list = list()
        tmp_list.append(tmp_DE_Vessel_Info_vessel_name__lineEdit_1)  # 0
        tmp_list.append(tmp_DE_Vessel_Info_vessel_management_id__lineEdit_1)  # 1
        tmp_list.append(tmp_DE_Vessel_Info_vessel_MMSI__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_callsign__lineEdit_1)  #
        tmp_list.append(tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_MRN__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_tonnage__lineEdit_1)
        tmp_list.append(tmp_DE_Vessel_Info_vessel_length__lineEdit_1)  # 7
        tmp_list.append(tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1)  # 8
        tmp_list.append(tmp_DE_Vessel_Type__lineEdit_1)  # 9

        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_management_id__lineEdit_1)  # 10
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_type__lineEdit_1)  # 11
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1)  # 12
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_model_name__lineEdit_1)
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1)
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1)  # 15
        tmp_list.append(tmp_DE_Marines_Electronics_Info_device_description__lineEdit_1)  # 16

        tmp_list.append(tmp_DE_Gather_Info_gather_no__lineEdit_1)  # 17
        tmp_list.append(tmp_DE_Gather_Info_gather_location__lineEdit_1)  # 18
        tmp_list.append(tmp_DE_Gather_Info_gather_person_name__lineEdit_1)  # 19
        tmp_list.append(tmp_DE_Gather_Info_gather_datetime__lineEdit_1)  # 20
        tmp_list.append(tmp_DE_Gather_Info_gather_person_agency__lineEdit_1)  # 21
        tmp_list.append(tmp_DE_Gather_Info_gather_person_rank__lineEdit_1)  # 22
        tmp_list.append(tmp_DE_Gather_Info_organization_code__lineEdit_1)  # 23
        tmp_list.append(tmp_DE_Gather_Info_submitter_name__lineEdit_1)  # 24
        tmp_list.append(tmp_DE_Gather_Inf_Gather_Source_Name__lineEdit_1)  # 25
        tmp_list.append(tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1)  # 26

        # Gather추가
        gather_info_list = list()
        gather_info_list.append(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        gather_info_list.append(tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        gather_info_list.append(tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        gather_info_list.append(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        gather_info_list.append(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        gather_info_list.append(tmp_DE_Gather_Info_gather_metadata__lineEdit_1)
        self.DE_Gather_Info_List[len(self.DE_Gather_Info_List)-1].append(gather_info_list)

        gather_info_button_list = list()
        gather_info_button_list.append(tmp_DE_Gather_Info_file__filebrowse__browseButton_1)
        gather_info_button_list.append(tmp_DE_Gather_Info_file__filebrowse__enterButton_1)
        self.DE_Gather_Info_Button_List[len(self.DE_Gather_Info_List)-1].append(gather_info_button_list)

        tmp_len = len(self.DE_Gather_Info_List)-1
        #[큰탭][소탭][버튼]
        self.DE_Gather_Info_Button_List[tmp_len][0][0].clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__browseButton_1_QFileDialog(tmp_len, 0)
        )
        self.DE_Gather_Info_Button_List[tmp_len][0][1].clicked.connect(
            lambda: self.DE_Gather_Info_file__filebrowse__enterButton_1_Calculate(tmp_len, 0)
        )

        tmp_DE_Gather_Info__addButton_1.clicked.connect(
            lambda: self.DE_Gather_Info_AddTab(tmp_len)
        )


        # tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)  # 27
        # tmp_list.append(tmp_DE_Gather_Info_gather_media_type__lineEdit_1)  # 28
        # tmp_list.append(tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)  # 29
        # tmp_list.append(tmp_DE_Gather_Info_gather_hash__lineEdit_1)  # 30
        # tmp_list.append(tmp_DE_Gather_Info_gather_path__lineEdit_1)  # 31
        # tmp_list.append(tmp_DE_Gather_Info_gather_metadata__lineEdit_1)  # 32

        # 기타파일 추가
        tmp_list.append(tmp_DE_other_files_file_browse__lineEdit_1)  # 33
        tmp_list.append(tmp_DE_other_files_id__lineEdit_1)  # 34
        tmp_list.append(tmp_DE_other_files_type__lineEdit_1)  # 35
        tmp_list.append(tmp_DE_other_files_file_size__lineEdit_1)  # 36
        tmp_list.append(tmp_DE_other_files_file_path__lineEdit_1)  # 37
        tmp_list.append(tmp_DE_other_files_file_hash_type__lineEdit_1)  # 38
        tmp_list.append(tmp_DE_other_files_file_hash_value__lineEdit_1)  # 39
        tmp_list.append(tmp_DE_other_files_file_description__lineEdit_1)
        tmp_list.append(tmp_DE_other_files_file_metadata__lineEdit_1)  # 41

        tmp_list.append(tmp_DE_Authentication_ID__lineEdit_1)  # 42
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1)  # 43
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1)  # 44
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1)  # 45
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1)  # 46
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)  # 47
        tmp_list.append(tmp_DE_Authentication_Person_Party_Name__lineEdit_1)  # 48

        # Acquisition 추가
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)  # 49
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)  # 50
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)  # 51
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)  # 52
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)  # 53
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)  # 54
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)  # 55
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)  # 56
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)  # 57
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)  # 58
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)  # 59
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)  # 60
        tmp_list.append(tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)  # 61

        self.DE_AddAll_List.append(tmp_list)






        tmp_DE_Digitlal_Evidence__label.setText("디지털 증거")

        tmp_DE_Vessel_Info__label_1.setText("선박 정보")
        tmp_DE_Marine_Electronics_Info__label_1.setText("해양 장비 정보")

        tmp_DE_Gather_Info__label_1.setText("채증 정보")
        tmp_DE_Gather_Info_file__blanklabel_1.setText("채증 정보 파일")
        tmp_DE_other_files__label_1.setText("기타 파일(jpg, mp4, txt, bin 등)")
        tmp_DE_Acquisition_Info__label_1.setText("수집 정보")
        tmp_DE_Acquisition_Info_DEF__label_1.setText("디지털 증거 파일")

        _translate = QtCore.QCoreApplication.translate
        tmp_tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_8), _translate("SecondWindow", "Tab 1"))

        _translate = QtCore.QCoreApplication.translate
        tmp_tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_4), _translate("SecondWindow", "Tab 1"))

        _translate = QtCore.QCoreApplication.translate
        tmp_tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_6), _translate("SecondWindow", "Tab 1"))

        _translate = QtCore.QCoreApplication.translate
        tmp_tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_9), _translate("SecondWindow", "Tab 1"))

        tmp_DE_Gather_Info__addButton_1.setText("+추가")
        tmp_DE_other_files__addButton_1.setText("+추가")
        tmp_DE_Acquisition_Info__addButton_1.setText("+추가")
        tmp_DE_Acquisition_Info_DEF__addButton_1.setText("+추가")

        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.setText("Browse...")
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.setText("Enter")
        tmp_DE_other_files_file_browse__browseButton_1.setText("Browse...")
        tmp_DE_other_files_file_browse__EnterButton_1.setText("Enter")
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1.setText("Browse...")
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1.setText("Enter")


        tmp_DE_Vessel_Info_vessel_name__label_1.setText("선박 이름:")  # 0
        tmp_DE_Vessel_Info_vessel_management_id__label_1.setText("선박 관리 고유 번호:")  # 1
        tmp_DE_Vessel_Info_vessel_MMSI__label_1.setText("선박 MMSI:")
        tmp_DE_Vessel_Info_vessel_callsign__label_1.setText("선박 callsign:")  #
        tmp_DE_Vessel_Info_vessel_IMO__label_1.setText("선박 IMO:")
        tmp_DE_Vessel_Info_vessel_MRN__label_1.setText("선박 MRN:")
        tmp_DE_Vessel_Info_vessel_tonnage__label_1.setText("선박 톤수:")
        tmp_DE_Vessel_Info_vessel_length__label_1.setText("선박 길이:")  # 7
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1.setText("항적 분석 장비수:")  # 8
        tmp_DE_Vessel_Type__label_1.setText("선박 유형:")  # 9

        tmp_DE_Marines_Electronics_Info_device_management_id__label_1.setText("장비 관리 고유 번호:")  # 10
        tmp_DE_Marines_Electronics_Info_device_type__label_1.setText("장비 유형:")  # 11
        tmp_DE_Marines_Electronics_Info_device_manufacturer__label_1.setText("장비 제조사:")  # 12
        tmp_DE_Marines_Electronics_Info_device_model_name__label_1.setText("장비 모델명:")
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__label_1.setText("장비 모델 시리얼 넘버:")
        tmp_DE_Marines_Electronics_Info_device_os_firmware__label_1.setText("장비 os firmware:")  # 15
        tmp_DE_Marines_Electronics_Info_device_description__label_1.setText("장비 설명:")  # 16

        tmp_DE_Gather_Info_gather_no__label_1.setText("채증 번호:")  # 17
        tmp_DE_Gather_Info_gather_location__label_1.setText("채증 장소:")  # 18
        tmp_DE_Gather_Info_gather_person_name__label_1.setText("채증 담당자:")  # 19
        tmp_DE_Gather_Info_gather_datetime__label_1.setText("채증 시간:")  # 20
        tmp_DE_Gather_Info_gather_person_agency__label_1.setText("채증 기관:")  # 21
        tmp_DE_Gather_Info_gather_person_rank__label_1.setText("채증 담당자 계급:")  # 22
        tmp_DE_Gather_Info_organization_code__label_1.setText("소속 조직 코드:")  # 23
        tmp_DE_Gather_Info_submitter_name__label_1.setText("피압수자:")  # 24
        tmp_DE_Gather_Inf_Gather_Source_Name__label_1.setText("정보 저장 매체명:")  # 25
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1.setText("수집 대상자 유형:")  # 26


        tmp_DE_Gather_Info_file__filebrowse__label_1.setText("파일 입력")  # 27
        tmp_DE_Gather_Info_gather_media_type__label_1.setText("채증 미디어 유형:")  # 28
        tmp_DE_Gather_Info__gather_hash_type__label_1.setText("채증 미디어 해시 종류:")  # 29
        tmp_DE_Gather_Info_gather_hash__label_1.setText("채증 미디어 해시값")  # 30
        tmp_DE_Gather_Info_gather_path__label_1.setText("채증 미디어 경로:")  # 31
        tmp_DE_Gather_Info_gather_metadata__label_1.setText("파일 메타데이터:")  # 32


        tmp_DE_other_files_file_browse__label_1.setText("파일 입력:")  # 33
        tmp_DE_other_files_id__label_1.setText("고유번호:")  # 34
        tmp_DE_other_files_type__label_1.setText("파일유형:")  # 35
        tmp_DE_other_files_file_size__label_1.setText("파일크기:")  # 36
        tmp_DE_other_files_file_path__label_1.setText("파일 경로:")  # 37
        tmp_DE_other_files_file_hash_type__label_1.setText("해시 종류:")  # 38
        tmp_DE_other_files_file_hash_value__label_1.setText("해시값:")  # 39
        tmp_DE_other_files_file_description__label_1.setText("파일 설명:")
        tmp_DE_other_files_file_metadata__label_1.setText("파일 메타데이터:")  # 41

        tmp_DE_Authentication_ID__label_1.setText("수집 id")  # 42
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1.setText("수집자명:")  # 43
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1.setText("수집 시간:")  # 44
        tmp_DE_Acquisition_Info_acquisition_location__label_1.setText("수집 장소:")  # 45
        tmp_DE_Acquisition_Info_acquisition_tool__label_1.setText("수집 도구:")  # 46
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1.setText("수집 도구 버젼:")  # 47
        tmp_DE_Authentication_Person_Party_Name__label_1.setText("수집 부서:")  # 48


        tmp_DE_Acquisition_Info_DEF_serial_no__label_1.setText("일련 번호:")  # 49
        tmp_DE_Acquisition_Info_DEF_management_id__label_1.setText("관리 번호:")  # 50
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setText("디지털 증거 유형:")  # 51
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setText("증거 채증 유형:")  # 52
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1.setText("채증 번호:")  # 53
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setText("파일입력:")  # 54
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setText("디지털 증거 파일 이름:")  # 55
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setText("디지털 증거 파일 경로:")  # 56
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1.setText("해시 종류:")  # 57
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1.setText("해시값:")  # 58
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1.setText("섹터 크기:")  # 59
        tmp_DE_Acquisition_Info_DEF_file_size__label_1.setText("파일 크기:")  # 60
        tmp_DE_Acquisition_Info_DEF__metadata__label_1.setText("파일 메타데이터:")  # 61

        # a = len(self.DE_AddAll_List)
        # tmp_DE_Gather_Info__addButton_1.clicked.connect(
        #     lambda: self.DE_Gather_Info__addButton_1_AddGatherInfoFile2(a))



    def AI_Reports_file_info__browseButton_1_QFileDialog(self, a):
        file_name = QFileDialog.getOpenFileName()
        self.AIReports_List[a][8].setText(file_name[0])

        ## AI other file Browse...버튼 클릭하면 파일 업로드

    def AI_other_files_file_browse__browseButton_1_QFileDialog(self, a):
        file_name = QFileDialog.getOpenFileName()
        self.AI_List[a][0].setText(file_name[0])

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

            ##################

            file2 = open(file_path, 'rb')
            magic = file2.read(8)
            magic.hex()

            self.AI_List[a][2].setText(file_name[file_name.rfind(".") + 1:])  # 파일 유형
            self.AI_List[a][3].setText(str(file_size))  # 파일 크기
            self.AI_List[a][4].setText(copy_file_path)  # 파일 경로
            self.AI_List[a][5].setText("SHA-256")  # 해시 종류
            self.AI_List[a][6].setText(sha256.hexdigest())  # 해시값

            if magic.hex() == 'ffd8ffe000104a46' or magic.hex() == '0000001466747970':

                input_file = file_path
                exe = "hachoir-metadata"
                process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                out_list = []
                for output in process.stdout:
                    if 'Metadata' in output:
                        continue
                    output = output.replace('\n', ', ')
                    output = output.replace('-', '')
                    out_list.append(output)

                result = ""
                for i in out_list:
                    result = result + i

                self.AI_List[a][8].setText(str(result))  # 메타데이터

            else:
                file_path = file_path
                with open(file_path, 'rb') as file:
                    content = file.read()

                    # 이름
                    file_name = file_path[file_path.rfind("/") + 1:]

                    # 유형
                    file_signature = file_path[file_path.rfind(".") + 1:]

                    # 크기
                    file_size = os.path.getsize(file_path)

                    # 수정한 날짜
                    modified_time = time.ctime(os.path.getmtime(file_path))

                    chiwon = str("파일 이름: ") + str(file_name) + str(", ") \
                             + str("파일 유형: ") + str(file_signature) + str(", ") \
                             + str("파일 크기: ") + str(file_size) + str(", ") \
                             + str("수정한 날짜: ") + str(modified_time)

                self.AI_List[a][8].setText(str(chiwon))  # 메타데이터


    def AI_Reports__AddTab(self):

        tmp_tab_7 = QtWidgets.QWidget()
        tmp_tab_7.setObjectName("tab_7")
        tmp_gridLayout_23 = QtWidgets.QGridLayout(tmp_tab_7)
        tmp_gridLayout_23.setObjectName("gridLayout_23")
        tmp_AI_Report__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Report__horizontalLayout_1.setObjectName("AI_Report__horizontalLayout_1")
        tmp_AI_Report__label_1 = QtWidgets.QLabel(tmp_tab_7)
        tmp_AI_Report__label_1.setObjectName("AI_Report__label_1")
        tmp_AI_Report__horizontalLayout_1.addWidget(tmp_AI_Report__label_1)
        tmp_gridLayout_23.addLayout(tmp_AI_Report__horizontalLayout_1, 0, 0, 1, 1)
        tmp_AI_Reports_scrollArea = QtWidgets.QScrollArea(tmp_tab_7)
        tmp_AI_Reports_scrollArea.setWidgetResizable(True)
        tmp_AI_Reports_scrollArea.setObjectName("AI_Reports_scrollArea")
        tmp_AI_Reports__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_AI_Reports__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 593, 529))
        tmp_AI_Reports__scrollAreaWidgetContents_1.setObjectName("AI_Reports__scrollAreaWidgetContents_1")
        tmp_gridLayout_12 = QtWidgets.QGridLayout(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_gridLayout_12.setObjectName("gridLayout_12")
        tmp_AI_Reports__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_AI_Reports__verticalLayout_1.setObjectName("AI_Reports__verticalLayout_1")
        tmp_AI_Reports_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_id__horizontalLayout_1.setObjectName("AI_Reports_id__horizontalLayout_1")
        tmp_AI_Reports_id__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_id__label_1.setObjectName("AI_Reports_id__label_1")
        tmp_AI_Reports_id__horizontalLayout_1.addWidget(tmp_AI_Reports_id__label_1)
        tmp_AI_Reports_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_id__lineEdit_1.setObjectName("AI_Reports_id__lineEdit_1")
        tmp_AI_Reports_id__horizontalLayout_1.addWidget(tmp_AI_Reports_id__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_id__horizontalLayout_1)
        tmp_AI_Reports_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_type__horizontalLayout_1.setObjectName("AI_Reports_type__horizontalLayout_1")
        tmp_AI_Reports_type__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_type__label_1.setObjectName("AI_Reports_type__label_1")
        tmp_AI_Reports_type__horizontalLayout_1.addWidget(tmp_AI_Reports_type__label_1)
        tmp_AI_Reports_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_type__lineEdit_1.setObjectName("AI_Reports_type__lineEdit_1")
        tmp_AI_Reports_type__horizontalLayout_1.addWidget(tmp_AI_Reports_type__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_type__horizontalLayout_1)
        tmp_AI_Reports_subtype__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_subtype__horizontalLayout_1.setObjectName("AI_Reports_subtype__horizontalLayout_1")
        tmp_AI_Reports_subtype__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_subtype__label_1.setObjectName("AI_Reports_subtype__label_1")
        tmp_AI_Reports_subtype__horizontalLayout_1.addWidget(tmp_AI_Reports_subtype__label_1)
        tmp_AI_Reports_subtype__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_subtype__lineEdit_1.setObjectName("AI_Reports_subtype__lineEdit_1")
        tmp_AI_Reports_subtype__horizontalLayout_1.addWidget(tmp_AI_Reports_subtype__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_subtype__horizontalLayout_1)
        tmp_AI_Reports_mgmt_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_mgmt_id__horizontalLayout_1.setObjectName("AI_Reports_mgmt_id__horizontalLayout_1")
        tmp_AI_Reports_mgmt_id__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_mgmt_id__label_1.setObjectName("AI_Reports_mgmt_id__label_1")
        tmp_AI_Reports_mgmt_id__horizontalLayout_1.addWidget(tmp_AI_Reports_mgmt_id__label_1)
        tmp_AI_Reports_mgmt_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_mgmt_id__lineEdit_1.setObjectName("AI_Reports_mgmt_id__lineEdit_1")
        tmp_AI_Reports_mgmt_id__horizontalLayout_1.addWidget(tmp_AI_Reports_mgmt_id__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_mgmt_id__horizontalLayout_1)
        tmp_AI_Reports_submission_agency__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_submission_agency__horizontalLayout_1.setObjectName("AI_Reports_submission_agency__horizontalLayout_1")
        tmp_AI_Reports_submission_agency__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_submission_agency__label_1.setObjectName("AI_Reports_submission_agency__label_1")
        tmp_AI_Reports_submission_agency__horizontalLayout_1.addWidget(tmp_AI_Reports_submission_agency__label_1)
        tmp_AI_Reports_submission_agency__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_submission_agency__lineEdit_1.setObjectName("AI_Reports_submission_agency__lineEdit_1")
        tmp_AI_Reports_submission_agency__horizontalLayout_1.addWidget(tmp_AI_Reports_submission_agency__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_submission_agency__horizontalLayout_1)
        tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1.setObjectName("AI_Reports_reports_creation_datetime__horizontalLayout_1")
        tmp_AI_Reports_reprot_creation_datetime__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_reprot_creation_datetime__label_1.setObjectName("AI_Reports_reprot_creation_datetime__label_1")
        tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1.addWidget(tmp_AI_Reports_reprot_creation_datetime__label_1)
        tmp_AI_Reports_reprot_creation_datetime__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_reprot_creation_datetime__lineEdit_1.setObjectName("AI_Reports_reprot_creation_datetime__lineEdit_1")
        tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1.addWidget(tmp_AI_Reports_reprot_creation_datetime__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_reports_creation_datetime__horizontalLayout_1)
        tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1.setObjectName("AI_Reports_division_name_of_report_maker__horizontalLayout_1")
        tmp_AI_Reports_division_name_of_report_maker__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_division_name_of_report_maker__label_1.setObjectName("AI_Reports_division_name_of_report_maker__label_1")
        tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1.addWidget(tmp_AI_Reports_division_name_of_report_maker__label_1)
        tmp_AI_Reports_division_name_of_report_maker__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_division_name_of_report_maker__lineEdit_1.setObjectName("AI_Reports_division_name_of_report_maker__lineEdit_1")
        tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1.addWidget(tmp_AI_Reports_division_name_of_report_maker__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_division_name_of_report_maker__horizontalLayout_1)
        tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1.setObjectName("AI_Reports_team_name_of_report_maker__horizontalLayout_1")
        tmp_AI_Reports_team_name_of_report_maker__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_team_name_of_report_maker__label_1.setObjectName("AI_Reports_team_name_of_report_maker__label_1")
        tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1.addWidget(tmp_AI_Reports_team_name_of_report_maker__label_1)
        tmp_AI_Reports_team_name_of_report_maker__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_team_name_of_report_maker__lineEdit_1.setObjectName("AI_Reports_team_name_of_report_maker__lineEdit_1")
        tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1.addWidget(tmp_AI_Reports_team_name_of_report_maker__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_team_name_of_report_maker__horizontalLayout_1)
        tmp_AI_Reports_file_info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_info__horizontalLayout_1.setObjectName("AI_Reports_file_info__horizontalLayout_1")
        tmp_AI_Reports_file_info__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_info__label_1.setObjectName("AI_Reports_file_info__label_1")
        tmp_AI_Reports_file_info__horizontalLayout_1.addWidget(tmp_AI_Reports_file_info__label_1)
        tmp_AI_Reports_file_info__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_info__lineEdit_1.setObjectName("AI_Reports_file_info__lineEdit_1")
        tmp_AI_Reports_file_info__horizontalLayout_1.addWidget(tmp_AI_Reports_file_info__lineEdit_1)
        tmp_AI_Reports_file_info__browseButton_1 = QtWidgets.QPushButton(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_info__browseButton_1.setObjectName("AI_Reports_file_info__browseButton_1")
        tmp_AI_Reports_file_info__horizontalLayout_1.addWidget(tmp_AI_Reports_file_info__browseButton_1)
        tmp_AI_Reports_file_info__enterButton_1 = QtWidgets.QPushButton(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_info__enterButton_1.setObjectName("AI_Reports_file_info__enterButton_1")
        tmp_AI_Reports_file_info__horizontalLayout_1.addWidget(tmp_AI_Reports_file_info__enterButton_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_info__horizontalLayout_1)
        tmp_AI_Reports_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_name__horizontalLayout_1.setObjectName("AI_Reports_file_name__horizontalLayout_1")
        tmp_AI_Reports_file_name__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_name__label_1.setObjectName("AI_Reports_file_name__label_1")
        tmp_AI_Reports_file_name__horizontalLayout_1.addWidget(tmp_AI_Reports_file_name__label_1)
        tmp_AI_Reports_file_name__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_name__lineEdit_1.setObjectName("AI_Reports_file_name__lineEdit_1")
        tmp_AI_Reports_file_name__horizontalLayout_1.addWidget(tmp_AI_Reports_file_name__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_name__horizontalLayout_1)
        tmp_AI_Reports_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_size__horizontalLayout_1.setObjectName("AI_Reports_file_size__horizontalLayout_1")
        tmp_AI_Reports_file_size__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_size__label_1.setObjectName("AI_Reports_file_size__label_1")
        tmp_AI_Reports_file_size__horizontalLayout_1.addWidget(tmp_AI_Reports_file_size__label_1)
        tmp_AI_Reports_file_size__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_size__lineEdit_1.setObjectName("AI_Reports_file_size__lineEdit_1")
        tmp_AI_Reports_file_size__horizontalLayout_1.addWidget(tmp_AI_Reports_file_size__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_size__horizontalLayout_1)
        tmp_AI_Reports_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_path__horizontalLayout_1.setObjectName("AI_Reports_file_path__horizontalLayout_1")
        tmp_AI_Reports_file_path__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_path__label_1.setObjectName("AI_Reports_file_path__label_1")
        tmp_AI_Reports_file_path__horizontalLayout_1.addWidget(tmp_AI_Reports_file_path__label_1)
        tmp_AI_Reports_file_path__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_path__lineEdit_1.setObjectName("AI_Reports_file_path__lineEdit_1")
        tmp_AI_Reports_file_path__horizontalLayout_1.addWidget(tmp_AI_Reports_file_path__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_path__horizontalLayout_1)
        tmp_AI_Reports_file_creation_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_creation_datetime__horizontalLayout_1.setObjectName("AI_Reports_file_creation_datetime__horizontalLayout_1")
        tmp_AI_Reports_file_creation_datetime__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_creation_datetime__label_1.setObjectName("AI_Reports_file_creation_datetime__label_1")
        tmp_AI_Reports_file_creation_datetime__horizontalLayout_1.addWidget(tmp_AI_Reports_file_creation_datetime__label_1)
        tmp_AI_Reports_file_creation_datetime__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_creation_datetime__lineEdit_1.setPlaceholderText("")
        tmp_AI_Reports_file_creation_datetime__lineEdit_1.setObjectName("AI_Reports_file_creation_datetime__lineEdit_1")
        tmp_AI_Reports_file_creation_datetime__horizontalLayout_1.addWidget(tmp_AI_Reports_file_creation_datetime__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_creation_datetime__horizontalLayout_1)
        tmp_AI_Reports_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_description__horizontalLayout_1.setObjectName("AI_Reports_file_description__horizontalLayout_1")
        tmp_AI_Reports_file_description__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_description__label_1.setObjectName("AI_Reports_file_description__label_1")
        tmp_AI_Reports_file_description__horizontalLayout_1.addWidget(tmp_AI_Reports_file_description__label_1)
        tmp_AI_Reports_file_description__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_description__lineEdit_1.setObjectName("AI_Reports_file_description__lineEdit_1")
        tmp_AI_Reports_file_description__horizontalLayout_1.addWidget(tmp_AI_Reports_file_description__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_description__horizontalLayout_1)
        tmp_AI_Reports_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_hash_type__horizontalLayout_1.setObjectName("AI_Reports_file_hash_type__horizontalLayout_1")
        tmp_AI_Reports_file_hash_type__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_hash_type__label_1.setObjectName("AI_Reports_file_hash_type__label_1")
        tmp_AI_Reports_file_hash_type__horizontalLayout_1.addWidget(tmp_AI_Reports_file_hash_type__label_1)
        tmp_AI_Reports_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_hash_type__lineEdit_1.setObjectName("AI_Reports_file_hash_type__lineEdit_1")
        tmp_AI_Reports_file_hash_type__horizontalLayout_1.addWidget(tmp_AI_Reports_file_hash_type__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_hash_type__horizontalLayout_1)
        tmp_AI_Reports_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_Reports_file_hash_value__horizontalLayout_1.setObjectName("AI_Reports_file_hash_value__horizontalLayout_1")
        tmp_AI_Reports_file_hash_value__label_1 = QtWidgets.QLabel(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_hash_value__label_1.setObjectName("AI_Reports_file_hash_value__label_1")
        tmp_AI_Reports_file_hash_value__horizontalLayout_1.addWidget(tmp_AI_Reports_file_hash_value__label_1)
        tmp_AI_Reports_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_AI_Reports_file_hash_value__lineEdit_1.setObjectName("AI_Reports_file_hash_value__lineEdit_1")
        tmp_AI_Reports_file_hash_value__horizontalLayout_1.addWidget(tmp_AI_Reports_file_hash_value__lineEdit_1)
        tmp_AI_Reports__verticalLayout_1.addLayout(tmp_AI_Reports_file_hash_value__horizontalLayout_1)
        tmp_gridLayout_12.addLayout(tmp_AI_Reports__verticalLayout_1, 0, 0, 1, 1)
        tmp_AI_Reports_scrollArea.setWidget(tmp_AI_Reports__scrollAreaWidgetContents_1)
        tmp_gridLayout_23.addWidget(tmp_AI_Reports_scrollArea, 1, 0, 1, 1)
        self.tabWidget_6.addTab(tmp_tab_7, "Tab" + str(len(self.AIReports_List) +1))

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

        tmp_AI_Report__label_1.setText("보고서: ")

        tmp_AI_Reports_id__label_1.setText("고유번호: ")
        tmp_AI_Reports_type__label_1.setText("유형: ")
        tmp_AI_Reports_subtype__label_1.setText("하위유형: ")
        tmp_AI_Reports_mgmt_id__label_1.setText("장비 고유번호: ")
        tmp_AI_Reports_submission_agency__label_1.setText("제출 기관: ")
        tmp_AI_Reports_reprot_creation_datetime__label_1.setText("보고서 작성 시간: ")
        tmp_AI_Reports_division_name_of_report_maker__label_1.setText("보고서 작성 부서명: ")
        tmp_AI_Reports_team_name_of_report_maker__label_1.setText("보고서 작성 팀명: ")

        tmp_AI_Reports_file_info__label_1.setText("파일 입력: ")
        tmp_AI_Reports_file_info__browseButton_1.setText("Browse...")
        tmp_AI_Reports_file_info__enterButton_1.setText("Enter")

        tmp_AI_Reports_file_name__label_1.setText("파일 이름: ")
        tmp_AI_Reports_file_size__label_1.setText("파일 크기: ")
        tmp_AI_Reports_file_path__label_1.setText("파일 경로: ")
        tmp_AI_Reports_file_creation_datetime__label_1.setText("파일 생성 날짜/시간: ")
        tmp_AI_Reports_file_description__label_1.setText("파일 설명: ")
        tmp_AI_Reports_file_hash_type__label_1.setText("파일 해시 종류: ")
        tmp_AI_Reports_file_hash_value__label_1.setText("파일 해시 값: ")





                # self.tabWidget_2.addTab(QWidget(), "New Tab")

    def AI_Equipment_Traces_AddTab(self):

        tmp_tab_5 = QtWidgets.QWidget()
        tmp_tab_5.setObjectName("tab_5")
        tmp_gridLayout_22 = QtWidgets.QGridLayout(tmp_tab_5)
        tmp_gridLayout_22.setObjectName("gridLayout_22")
        tmp_AI_EquipmentTraces__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces__horizontalLayout_1.setObjectName("AI_EquipmentTraces__horizontalLayout_1")
        tmp_AI_EquipmentTraces__label_1 = QtWidgets.QLabel(tmp_tab_5)
        tmp_AI_EquipmentTraces__label_1.setObjectName("AI_EquipmentTraces__label_1")
        tmp_AI_EquipmentTraces__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces__label_1)
        tmp_gridLayout_22.addLayout(tmp_AI_EquipmentTraces__horizontalLayout_1, 0, 0, 1, 1)
        tmp_AI_EquipmentTraces__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_5)
        tmp_AI_EquipmentTraces__scrollArea_1.setWidgetResizable(True)
        tmp_AI_EquipmentTraces__scrollArea_1.setObjectName("AI_EquipmentTraces__scrollArea_1")
        tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 593, 346))
        tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1.setObjectName("AI_EquipmentTraces__scrollAreaWidgetContents_1")
        tmp_gridLayout_19 = QtWidgets.QGridLayout(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_gridLayout_19.setObjectName("gridLayout_19")
        tmp_AI_EquipmentTraces__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_AI_EquipmentTraces__verticalLayout_1.setObjectName("AI_EquipmentTraces__verticalLayout_1")
        tmp_AI_EquipmentTraces_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_id__horizontalLayout_1.setObjectName("AI_EquipmentTraces_id__horizontalLayout_1")
        tmp_AI_EquipmentTraces_id__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_id__label_1.setObjectName("AI_EquipmentTraces_id__label_1")
        tmp_AI_EquipmentTraces_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_id__label_1)
        tmp_AI_EquipmentTraces_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_id__lineEdit_1.setReadOnly(False)
        tmp_AI_EquipmentTraces_id__lineEdit_1.setObjectName("AI_EquipmentTraces_id__lineEdit_1")
        tmp_AI_EquipmentTraces_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_id__lineEdit_1)
        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_id__horizontalLayout_1)
        tmp_AI_EquipmentTraces_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_type__horizontalLayout_1.setObjectName("AI_EquipmentTraces_type__horizontalLayout_1")
        tmp_AI_EquipmentTraces_type__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_type__label_1.setObjectName("AI_EquipmentTraces_type__label_1")
        tmp_AI_EquipmentTraces_type__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_type__label_1)
        tmp_AI_EquipmentTraces_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_type__lineEdit_1.setObjectName("AI_EquipmentTraces_type__lineEdit_1")
        tmp_AI_EquipmentTraces_type__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_type__lineEdit_1)
        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_type__horizontalLayout_1)
        tmp_AI_EquipmentTraces_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_description__horizontalLayout_1.setObjectName("AI_EquipmentTraces_description__horizontalLayout_1")
        tmp_AI_EquipmentTraces_description__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_description__label_1.setObjectName("AI_EquipmentTraces_description__label_1")
        tmp_AI_EquipmentTraces_description__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_description__label_1)
        tmp_AI_EquipmentTraces_description__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_description__lineEdit_1.setObjectName("AI_EquipmentTraces_description__lineEdit_1")
        tmp_AI_EquipmentTraces_description__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_description__lineEdit_1)
        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_description__horizontalLayout_1)
        tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1.setObjectName("AI_EquipmentTraces_mgmt_id__horizontalLayout_1")
        tmp_AI_EquipmentTraces_mgmt_id__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_mgmt_id__label_1.setObjectName("AI_EquipmentTraces_mgmt_id__label_1")
        tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_mgmt_id__label_1)
        tmp_AI_EquipmentTraces_mgmt_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_mgmt_id__lineEdit_1.setObjectName("AI_EquipmentTraces_mgmt_id__lineEdit_1")
        tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_mgmt_id__lineEdit_1)
        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_mgmt_id__horizontalLayout_1)
        tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1.setObjectName("AI_EquipmentTraces_vessel_id__horizontalLayout_1")
        tmp_AI_EquipmentTraces_vessel_id__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_vessel_id__label_1.setObjectName("AI_EquipmentTraces_vessel_id__label_1")
        tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_vessel_id__label_1)
        tmp_AI_EquipmentTraces_vessel_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_vessel_id__lineEdit_1.setObjectName("AI_EquipmentTraces_vessel_id__lineEdit_1")
        tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_vessel_id__lineEdit_1)
        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_vessel_id__horizontalLayout_1)
        tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1.setObjectName("AI_EquipmentTraces_evidence_id__horizontalLayout_1")
        tmp_AI_EquipmentTraces_evidence_id__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_evidence_id__label_1.setObjectName("AI_EquipmentTraces_evidence_id__label_1")
        tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_evidence_id__label_1)
        tmp_AI_EquipmentTraces_evidence_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_evidence_id__lineEdit_1.setObjectName("AI_EquipmentTraces_evidence_id__lineEdit_1")
        tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_evidence_id__lineEdit_1)
        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_evidence_id__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info__horizontalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info__label_1.setObjectName("AI_EquipmentTraces_user_trace_info__label_1")
        tmp_AI_EquipmentTraces_user_trace_info__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info__label_1)
        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_trace_info__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1")
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1 = QtWidgets.QScrollArea(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1.setWidgetResizable(True)
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1.setObjectName("AI_EquipmentTraces_user_traces_info_sub__scrollArea_1")
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 535, 267))
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1.setObjectName("AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1")
        tmp_gridLayout_14 = QtWidgets.QGridLayout(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_gridLayout_14.setObjectName("gridLayout_14")
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.setObjectName("AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1")
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1")
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__lineEdit_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_description__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_description__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_description__label_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_system_description__label_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_system_description__lineEdit_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_trace_info_system_description__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_operation_status__label_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__label_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lineEdit_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__lhorizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_recording_period__label_1")
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__label_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1")
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__lineEdit_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1")
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1")
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__lineEdit_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__horizontalLayout_1)
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1.setObjectName("AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1")
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1 = QtWidgets.QLabel(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1.setObjectName("AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1")
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1)
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1.setObjectName("AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1")
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__lineEdit_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__horizontalLayout_1)
        tmp_gridLayout_14.addLayout(tmp_AI_EquipmentTraces_user_traces_info_sub__verticalLayout_1, 0, 0, 1, 1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1.setWidget(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollAreaWidgetContents_1)
        tmp_AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1.addWidget(tmp_AI_EquipmentTraces_user_traces_info_sub__scrollArea_1)
        tmp_AI_EquipmentTraces__verticalLayout_1.addLayout(tmp_AI_EquipmentTraces_user_traces_info_sub__horizontalLayout_1)
        tmp_gridLayout_19.addLayout(tmp_AI_EquipmentTraces__verticalLayout_1, 0, 0, 2, 2)
        tmp_AI_EquipmentTraces__scrollArea_1.setWidget(tmp_AI_EquipmentTraces__scrollAreaWidgetContents_1)
        tmp_gridLayout_22.addWidget(tmp_AI_EquipmentTraces__scrollArea_1, 1, 0, 1, 1)
        self.tabWidget_5.addTab(tmp_tab_5, "Tab" + str(len(self.AI_EquipmentTraces_List) + 1))

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


        tmp_AI_EquipmentTraces__label_1.setText("Equipment Traces (장비별로)")

        tmp_AI_EquipmentTraces_id__label_1.setText("고유번호: ")
        tmp_AI_EquipmentTraces_type__label_1.setText("유형: ")
        tmp_AI_EquipmentTraces_description__label_1.setText("유형 설명: ")
        tmp_AI_EquipmentTraces_mgmt_id__label_1.setText("장비 아이디: ")
        tmp_AI_EquipmentTraces_vessel_id__label_1.setText("선박 고유번호: ")
        tmp_AI_EquipmentTraces_evidence_id__label_1.setText("증거 고유번호: ")

        tmp_AI_EquipmentTraces_user_trace_info__label_1.setText("사용자 추적 정보: ")

        tmp_AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1.setText("시스템 시작 시간: ")
        tmp_AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1.setText("항적 추출 방법: ")
        tmp_AI_EquipmentTraces_user_trace_info_system_description__label_1.setText("시스템 설명: ")
        tmp_AI_EquipmentTraces_user_trace_info_system_operation_status__label_1.setText("시스템 운영 상태: ")
        tmp_AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1.setText("시스템 종료 시간: ")
        tmp_AI_EquipmentTraces_user_trace_info_track_recording_period__label_1.setText("항적 기록 시간: ")
        tmp_AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1.setText("항적 삭제 개수: ")
        tmp_AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1.setText("비고: ")

    def AI_Other_Files_AddTab(self):

        tmp_tab_3 = QtWidgets.QWidget()
        tmp_tab_3.setObjectName("tab_3")
        tmp_gridLayout_10 = QtWidgets.QGridLayout(tmp_tab_3)
        tmp_gridLayout_10.setObjectName("gridLayout_10")
        tmp_AI_other_files__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files__horizontalLayout_1.setObjectName("AI_other_files__horizontalLayout_1")
        tmp_AI_other_files__label_1 = QtWidgets.QLabel(tmp_tab_3)
        tmp_AI_other_files__label_1.setObjectName("AI_other_files__label_1")
        tmp_AI_other_files__horizontalLayout_1.addWidget(tmp_AI_other_files__label_1)
        tmp_gridLayout_10.addLayout(tmp_AI_other_files__horizontalLayout_1, 0, 0, 1, 1)
        tmp_AI_other_files__scrollArea = QtWidgets.QScrollArea(tmp_tab_3)
        tmp_AI_other_files__scrollArea.setWidgetResizable(True)
        tmp_AI_other_files__scrollArea.setObjectName("AI_other_files__scrollArea")
        tmp_AI__scrollAreaWidgetContents = QtWidgets.QWidget()
        tmp_AI__scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 618, 520))
        tmp_AI__scrollAreaWidgetContents.setObjectName("AI__scrollAreaWidgetContents")
        tmp_gridLayout_11 = QtWidgets.QGridLayout(tmp_AI__scrollAreaWidgetContents)
        tmp_gridLayout_11.setObjectName("gridLayout_11")
        tmp_AI_other_files__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_AI_other_files__verticalLayout_1.setObjectName("AI_other_files__verticalLayout_1")
        tmp_AI_other_files_file_browse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_browse__horizontalLayout_1.setObjectName("AI_other_files_file_browse__horizontalLayout_1")
        tmp_AI_other_files_file_browse__label_1 = QtWidgets.QLabel(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_browse__label_1.setObjectName("AI_other_files_file_browse__label_1")
        tmp_AI_other_files_file_browse__horizontalLayout_1.addWidget(tmp_AI_other_files_file_browse__label_1)
        tmp_AI_other_files_file_browse__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_browse__lineEdit_1.setObjectName("AI_other_files_file_browse__lineEdit_1")
        tmp_AI_other_files_file_browse__horizontalLayout_1.addWidget(tmp_AI_other_files_file_browse__lineEdit_1)
        tmp_AI_other_files_file_browse__browseButton_1 = QtWidgets.QPushButton(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_browse__browseButton_1.setObjectName("AI_other_files_file_browse__browseButton_1")
        tmp_AI_other_files_file_browse__horizontalLayout_1.addWidget(tmp_AI_other_files_file_browse__browseButton_1)
        tmp_AI_other_files_file_browse__enterButton_1 = QtWidgets.QPushButton(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_browse__enterButton_1.setObjectName("AI_other_files_file_browse__enterButton_1")
        tmp_AI_other_files_file_browse__horizontalLayout_1.addWidget(tmp_AI_other_files_file_browse__enterButton_1)
        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_browse__horizontalLayout_1)
        tmp_AI_other_files_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_id__horizontalLayout_1.setObjectName("AI_other_files_id__horizontalLayout_1")
        tmp_AI_other_files_id__label_1 = QtWidgets.QLabel(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_id__label_1.setObjectName("AI_other_files_id__label_1")
        tmp_AI_other_files_id__horizontalLayout_1.addWidget(tmp_AI_other_files_id__label_1)
        tmp_AI_other_files_id__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_id__lineEdit_1.setObjectName("AI_other_files_id__lineEdit_1")
        tmp_AI_other_files_id__horizontalLayout_1.addWidget(tmp_AI_other_files_id__lineEdit_1)
        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_id__horizontalLayout_1)
        tmp_AI_other_files_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_type__horizontalLayout_1.setObjectName("AI_other_files_type__horizontalLayout_1")
        tmp_AI_other_files_type__label_1 = QtWidgets.QLabel(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_type__label_1.setObjectName("AI_other_files_type__label_1")
        tmp_AI_other_files_type__horizontalLayout_1.addWidget(tmp_AI_other_files_type__label_1)
        tmp_AI_other_files_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_type__lineEdit_1.setObjectName("AI_other_files_type__lineEdit_1")
        tmp_AI_other_files_type__horizontalLayout_1.addWidget(tmp_AI_other_files_type__lineEdit_1)
        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_type__horizontalLayout_1)
        tmp_AI_other_files_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_size__horizontalLayout_1.setObjectName("AI_other_files_file_size__horizontalLayout_1")
        tmp_AI_other_files_file_size__label_1 = QtWidgets.QLabel(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_size__label_1.setObjectName("AI_other_files_file_size__label_1")
        tmp_AI_other_files_file_size__horizontalLayout_1.addWidget(tmp_AI_other_files_file_size__label_1)
        tmp_AI_other_files_file_size__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_size__lineEdit_1.setObjectName("AI_other_files_file_size__lineEdit_1")
        tmp_AI_other_files_file_size__horizontalLayout_1.addWidget(tmp_AI_other_files_file_size__lineEdit_1)
        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_size__horizontalLayout_1)
        tmp_AI_other_files_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_path__horizontalLayout_1.setObjectName("AI_other_files_file_path__horizontalLayout_1")
        tmp_AI_other_files_file_path__label_1 = QtWidgets.QLabel(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_path__label_1.setObjectName("AI_other_files_file_path__label_1")
        tmp_AI_other_files_file_path__horizontalLayout_1.addWidget(tmp_AI_other_files_file_path__label_1)
        tmp_AI_other_files_file_path__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_path__lineEdit_1.setObjectName("AI_other_files_file_path__lineEdit_1")
        tmp_AI_other_files_file_path__horizontalLayout_1.addWidget(tmp_AI_other_files_file_path__lineEdit_1)
        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_path__horizontalLayout_1)
        tmp_AI_other_files_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_hash_type__horizontalLayout_1.setObjectName("AI_other_files_file_hash_type__horizontalLayout_1")
        tmp_AI_other_files_file_hash_type__label_1 = QtWidgets.QLabel(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_hash_type__label_1.setObjectName("AI_other_files_file_hash_type__label_1")
        tmp_AI_other_files_file_hash_type__horizontalLayout_1.addWidget(tmp_AI_other_files_file_hash_type__label_1)
        tmp_AI_other_files_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_hash_type__lineEdit_1.setObjectName("AI_other_files_file_hash_type__lineEdit_1")
        tmp_AI_other_files_file_hash_type__horizontalLayout_1.addWidget(tmp_AI_other_files_file_hash_type__lineEdit_1)
        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_hash_type__horizontalLayout_1)
        tmp_AI_other_files_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_hash_value__horizontalLayout_1.setObjectName("AI_other_files_file_hash_value__horizontalLayout_1")
        tmp_AI_other_files_file_hash_value__label_1 = QtWidgets.QLabel(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_hash_value__label_1.setObjectName("AI_other_files_file_hash_value__label_1")
        tmp_AI_other_files_file_hash_value__horizontalLayout_1.addWidget(tmp_AI_other_files_file_hash_value__label_1)
        tmp_AI_other_files_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_hash_value__lineEdit_1.setObjectName("AI_other_files_file_hash_value__lineEdit_1")
        tmp_AI_other_files_file_hash_value__horizontalLayout_1.addWidget(tmp_AI_other_files_file_hash_value__lineEdit_1)
        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_hash_value__horizontalLayout_1)
        tmp_AI_other_files_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_description__horizontalLayout_1.setObjectName("AI_other_files_file_description__horizontalLayout_1")
        tmp_AI_other_files_file_description__label_1 = QtWidgets.QLabel(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_description__label_1.setObjectName("AI_other_files_file_description__label_1")
        tmp_AI_other_files_file_description__horizontalLayout_1.addWidget(tmp_AI_other_files_file_description__label_1)
        tmp_AI_other_files_file_description__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_description__lineEdit_1.setObjectName("AI_other_files_file_description__lineEdit_1")
        tmp_AI_other_files_file_description__horizontalLayout_1.addWidget(tmp_AI_other_files_file_description__lineEdit_1)
        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_description__horizontalLayout_1)
        tmp_AI_other_files_file_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_AI_other_files_file_metadata__horizontalLayout_1.setObjectName("AI_other_files_file_metadata__horizontalLayout_1")
        tmp_AI_other_files_file_metadata__label_1 = QtWidgets.QLabel(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_metadata__label_1.setObjectName("AI_other_files_file_metadata__label_1")
        tmp_AI_other_files_file_metadata__horizontalLayout_1.addWidget(tmp_AI_other_files_file_metadata__label_1)
        tmp_AI_other_files_file_metadata__lineEdit_1 = QtWidgets.QLineEdit(tmp_AI__scrollAreaWidgetContents)
        tmp_AI_other_files_file_metadata__lineEdit_1.setObjectName("AI_other_files_file_metadata__lineEdit_1")
        tmp_AI_other_files_file_metadata__horizontalLayout_1.addWidget(tmp_AI_other_files_file_metadata__lineEdit_1)
        tmp_AI_other_files__verticalLayout_1.addLayout(tmp_AI_other_files_file_metadata__horizontalLayout_1)
        tmp_gridLayout_11.addLayout(tmp_AI_other_files__verticalLayout_1, 0, 0, 1, 1)
        tmp_AI_other_files__scrollArea.setWidget(tmp_AI__scrollAreaWidgetContents)
        tmp_gridLayout_10.addWidget(tmp_AI_other_files__scrollArea, 1, 0, 1, 1)
        self.tabWidget_4.addTab(tmp_tab_3, "Tab" + str(len(self.AI_List)+1))

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

        tmp_AI_other_files__label_1.setText("기타 파일(jpg, mp4, txt, bin 등)")

        tmp_AI_other_files_file_browse__label_1.setText("파일 입력")
        tmp_AI_other_files_file_browse__browseButton_1.setText("Browse...")
        tmp_AI_other_files_file_browse__enterButton_1.setText("Enter")

        tmp_AI_other_files_id__label_1.setText("고유번호: ")
        tmp_AI_other_files_type__label_1.setText("파일유형:")
        tmp_AI_other_files_file_size__label_1.setText("파일크기: ")
        tmp_AI_other_files_file_path__label_1.setText("파일 경로: ")
        tmp_AI_other_files_file_hash_type__label_1.setText("해시종류: ")
        tmp_AI_other_files_file_hash_value__label_1.setText("해시값: ")
        tmp_AI_other_files_file_description__label_1.setText("파일 설명: ")
        tmp_AI_other_files_file_metadata__label_1.setText("파일 메타데이터: ")


    def Log__addButton_AddTab(self):

        tmp_tab = QtWidgets.QWidget()
        tmp_tab.setObjectName("tab")
        tmp_gridLayout_5 = QtWidgets.QGridLayout(tmp_tab)
        tmp_gridLayout_5.setObjectName("gridLayout_5")
        tmp_Log__scrollArea = QtWidgets.QScrollArea(tmp_tab)
        tmp_Log__scrollArea.setWidgetResizable(True)
        tmp_Log__scrollArea.setObjectName("Log__scrollArea")
        tmp_scrollAreaWidgetContents_12 = QtWidgets.QWidget()
        tmp_scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 1308, 592))
        tmp_scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
        tmp_gridLayout_16 = QtWidgets.QGridLayout(tmp_scrollAreaWidgetContents_12)
        tmp_gridLayout_16.setObjectName("gridLayout_16")
        tmp_Log__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_Log__verticalLayout_1.setObjectName("Log__verticalLayout_1")
        tmp_Log_digital_evidence_package_management_id___horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_Log_digital_evidence_package_management_id___horizontalLayout_1.setObjectName(
            "Log_digital_evidence_package_management_id___horizontalLayout_1")
        tmp_Log_digital_evidence_package_management_id__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
        tmp_Log_digital_evidence_package_management_id__label_1.setObjectName(
            "Log_digital_evidence_package_management_id__label_1")
        tmp_Log_digital_evidence_package_management_id___horizontalLayout_1.addWidget(
            tmp_Log_digital_evidence_package_management_id__label_1)
        tmp_Log_digital_evidence_package_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_scrollAreaWidgetContents_12)
        tmp_Log_digital_evidence_package_management_id__lineEdit_1.setObjectName(
            "Log_digital_evidence_package_management_id__lineEdit_1")
        tmp_Log_digital_evidence_package_management_id___horizontalLayout_1.addWidget(
            tmp_Log_digital_evidence_package_management_id__lineEdit_1)
        tmp_Log__verticalLayout_1.addLayout(tmp_Log_digital_evidence_package_management_id___horizontalLayout_1)
        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1.setObjectName(
            "Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1")
        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1 = QtWidgets.QLabel(
            tmp_scrollAreaWidgetContents_12)
        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1.setObjectName(
            "Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1")
        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1.addWidget(
            tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1)
        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_scrollAreaWidgetContents_12)
        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1.setObjectName(
            "Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1")
        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1.addWidget(
            tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1)
        tmp_Log__verticalLayout_1.addLayout(tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__horizontalLayout_1)
        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1.setObjectName(
            "Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1")
        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__label_1 = QtWidgets.QLabel(
            tmp_scrollAreaWidgetContents_12)
        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__label_1.setObjectName(
            "Log_Digital_Evidence_Pack_History_End_Date_Time__label_1")
        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1.addWidget(
            tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__label_1)
        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_scrollAreaWidgetContents_12)
        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1.setObjectName(
            "Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1")
        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1.addWidget(
            tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__lineEdit_1)
        tmp_Log__verticalLayout_1.addLayout(tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__horizontalLayout_1)
        tmp_Log_log_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_Log_log_type__horizontalLayout_1.setObjectName("Log_log_type__horizontalLayout_1")
        tmp_Log_log_type__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
        tmp_Log_log_type__label_1.setObjectName("Log_log_type__label_1")
        tmp_Log_log_type__horizontalLayout_1.addWidget(tmp_Log_log_type__label_1)
        tmp_Log_log_type__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
        tmp_Log_log_type__lineEdit_1.setObjectName("Log_log_type__lineEdit_1")
        tmp_Log_log_type__horizontalLayout_1.addWidget(tmp_Log_log_type__lineEdit_1)
        tmp_Log__verticalLayout_1.addLayout(tmp_Log_log_type__horizontalLayout_1)
        tmp_Log_log_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_Log_log_description__horizontalLayout_1.setObjectName("Log_log_description__horizontalLayout_1")
        tmp_Log_log_description__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
        tmp_Log_log_description__label_1.setObjectName("Log_log_description__label_1")
        tmp_Log_log_description__horizontalLayout_1.addWidget(tmp_Log_log_description__label_1)
        tmp_Log_log_description__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
        tmp_Log_log_description__lineEdit_1.setObjectName("Log_log_description__lineEdit_1")
        tmp_Log_log_description__horizontalLayout_1.addWidget(tmp_Log_log_description__lineEdit_1)
        tmp_Log__verticalLayout_1.addLayout(tmp_Log_log_description__horizontalLayout_1)
        tmp_Log_devision_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_Log_devision_name_of_logger__horizontalLayout_1.setObjectName(
            "Log_devision_name_of_logger__horizontalLayout_1")
        tmp_Log_devision_name_of_logger__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
        tmp_Log_devision_name_of_logger__label_1.setObjectName("Log_devision_name_of_logger__label_1")
        tmp_Log_devision_name_of_logger__horizontalLayout_1.addWidget(tmp_Log_devision_name_of_logger__label_1)
        tmp_Log_devision_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
        tmp_Log_devision_name_of_logger__lineEdit_1.setObjectName("Log_devision_name_of_logger__lineEdit_1")
        tmp_Log_devision_name_of_logger__horizontalLayout_1.addWidget(tmp_Log_devision_name_of_logger__lineEdit_1)
        tmp_Log__verticalLayout_1.addLayout(tmp_Log_devision_name_of_logger__horizontalLayout_1)
        tmp_Log_team_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_Log_team_name_of_logger__horizontalLayout_1.setObjectName("Log_team_name_of_logger__horizontalLayout_1")
        tmp_Log_team_name_of_logger__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
        tmp_Log_team_name_of_logger__label_1.setObjectName("Log_team_name_of_logger__label_1")
        tmp_Log_team_name_of_logger__horizontalLayout_1.addWidget(tmp_Log_team_name_of_logger__label_1)
        tmp_Log_team_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
        tmp_Log_team_name_of_logger__lineEdit_1.setObjectName("Log_team_name_of_logger__lineEdit_1")
        tmp_Log_team_name_of_logger__horizontalLayout_1.addWidget(tmp_Log_team_name_of_logger__lineEdit_1)
        tmp_Log__verticalLayout_1.addLayout(tmp_Log_team_name_of_logger__horizontalLayout_1)
        tmp_Log_rank_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_Log_rank_of_logger__horizontalLayout_1.setObjectName("Log_rank_of_logger__horizontalLayout_1")
        tmp_Log_rank_of_logger__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
        tmp_Log_rank_of_logger__label_1.setObjectName("Log_rank_of_logger__label_1")
        tmp_Log_rank_of_logger__horizontalLayout_1.addWidget(tmp_Log_rank_of_logger__label_1)
        tmp_Log_rank_of_logger__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
        tmp_Log_rank_of_logger__lineEdit_1.setObjectName("Log_rank_of_logger__lineEdit_1")
        tmp_Log_rank_of_logger__horizontalLayout_1.addWidget(tmp_Log_rank_of_logger__lineEdit_1)
        tmp_Log__verticalLayout_1.addLayout(tmp_Log_rank_of_logger__horizontalLayout_1)
        tmp_Log_name_of_logger__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_Log_name_of_logger__horizontalLayout_1.setObjectName("Log_name_of_logger__horizontalLayout_1")
        tmp_Log_name_of_logger__label_1 = QtWidgets.QLabel(tmp_scrollAreaWidgetContents_12)
        tmp_Log_name_of_logger__label_1.setObjectName("Log_name_of_logger__label_1")
        tmp_Log_name_of_logger__horizontalLayout_1.addWidget(tmp_Log_name_of_logger__label_1)
        tmp_Log_name_of_logger__lineEdit_1 = QtWidgets.QLineEdit(tmp_scrollAreaWidgetContents_12)
        tmp_Log_name_of_logger__lineEdit_1.setObjectName("Log_name_of_logger__lineEdit_1")
        tmp_Log_name_of_logger__horizontalLayout_1.addWidget(tmp_Log_name_of_logger__lineEdit_1)
        tmp_Log__verticalLayout_1.addLayout(tmp_Log_name_of_logger__horizontalLayout_1)
        tmp_gridLayout_16.addLayout(tmp_Log__verticalLayout_1, 0, 0, 1, 1)
        tmp_Log__scrollArea.setWidget(tmp_scrollAreaWidgetContents_12)
        tmp_gridLayout_5.addWidget(tmp_Log__scrollArea, 0, 0, 1, 1)
        self.tabWidget_2.addTab(tmp_tab, "Tab " + str(len(self.Log_List) + 1))

        # 추가
        now = datetime.datetime.now()

        tmp_list = list()
        tmp_list.append(tmp_Log_digital_evidence_package_management_id__lineEdit_1)
        tmp_list.append(tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__lineEdit_1)
        tmp_list.append(now)
        tmp_list.append(tmp_Log_log_type__lineEdit_1)
        tmp_list.append(tmp_Log_log_description__lineEdit_1)
        tmp_list.append(tmp_Log_devision_name_of_logger__lineEdit_1)
        tmp_list.append(tmp_Log_team_name_of_logger__lineEdit_1)
        tmp_list.append(tmp_Log_rank_of_logger__lineEdit_1)
        tmp_list.append(tmp_Log_name_of_logger__lineEdit_1)
        self.Log_List.append(tmp_list)

        tmp_Log_digital_evidence_package_management_id__label_1.setText("디지털 증거 패키지 고유번호: ")
        tmp_Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1.setText("시작 시간: ")
        tmp_Log_Digital_Evidence_Pack_History_End_Date_Time__label_1.setText("종료 시간: ")
        tmp_Log_log_type__label_1.setText("이력 유형: ")
        tmp_Log_log_description__label_1.setText("이력 설명: ")
        tmp_Log_devision_name_of_logger__label_1.setText("이력 분석 조직명: ")
        tmp_Log_team_name_of_logger__label_1.setText("이력 분석 팀명: ")
        tmp_Log_rank_of_logger__label_1.setText("이력 분석자 계급: ")
        tmp_Log_name_of_logger__label_1.setText("이력 분석자명")


    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.Digital_Evidence_Package.setText(_translate("SecondWindow", "Digital Evidence Package"))
        self.Case_Info.setText(_translate("SecondWindow", "사건 정보"))
        self.case_management_id__label.setText(_translate("SecondWindow", "사건 관리 번호:"))
        self.agency_case_no__label.setText(_translate("SecondWindow", "기관 사건 번호:"))
        self.agency_organization_code__label.setText(_translate("SecondWindow", "기관 코드:"))
        self.agency_organization_name__label.setText(_translate("SecondWindow", "기관명:"))
        self.agency_organization_party_name__label.setText(_translate("SecondWindow", "부서명:"))
        self.contents_of_request__label.setText(_translate("SecondWindow", "요청사항:"))
        self.case_summary__label.setText(_translate("SecondWindow", "사건 요약:"))
        self.case_description__label.setText(_translate("SecondWindow", "사건 설명:"))
        self.case_datetime__label.setText(_translate("SecondWindow", "사건 발생 시각:"))
        self.ordering_datetime__label.setText(_translate("SecondWindow", "사건 의뢰 시각:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Case_Info_tab), _translate("SecondWindow", "Case Info"))
        self.DE__addButton.setText(_translate("SecondWindow", "+추가"))
        self.DE_Digitlal_Evidence__label.setText(_translate("SecondWindow", "디지털 증거"))
        self.DE_Gather_Info_gather_no__label_1.setText(_translate("SecondWindow", "채증 번호:"))
        self.DE_Gather_Info_gather_location__label_1.setText(_translate("SecondWindow", "채증 장소:"))
        self.DE_Gather_Info_gather_person_name__label_1.setText(_translate("SecondWindow", "채증 담당자:"))
        self.DE_Gather_Info_gather_datetime__label_1.setText(_translate("SecondWindow", "채증 시간:"))
        self.DE_Gather_Info_gather_datetime__lineEdit_1.setPlaceholderText(_translate("SecondWindow", "ex) 2021-11-30 19:58:13.829475+09:00"))
        self.DE_Gather_Info_gather_person_agency__label_1.setText(_translate("SecondWindow", "채증 기관:"))
        self.DE_Gather_Info_gather_person_rank__label_1.setText(_translate("SecondWindow", "채증 담당자 계급:"))
        self.DE_Gather_Info_organization_code__label_1.setText(_translate("SecondWindow", "소속 조직 코드:"))
        self.DE_Gather_Info_submitter_name__label_1.setText(_translate("SecondWindow", "피압수자:"))
        self.DE_Gather_Inf_Gather_Source_Name__label_1.setText(_translate("SecondWindow", "정보 저장 매체명:"))
        self.DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1.setText(_translate("SecondWindow", "수집 대상자 유형:"))
        self.DE_Gather_Info_file__filebrowse__label_1.setText(_translate("SecondWindow", "파일 입력"))
        self.DE_Gather_Info_file__filebrowse__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.DE_Gather_Info_file__filebrowse__enterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.DE_Gather_Info_gather_media_type__label_1.setText(_translate("SecondWindow", "채증 미디어 유형:"))
        self.DE_Gather_Info__gather_hash_type__label_1.setText(_translate("SecondWindow", "채증 미디어 해시 종류:"))
        self.DE_Gather_Info_gather_hash__label_1.setText(_translate("SecondWindow", "채증 미디어 해시값:"))
        self.DE_Gather_Info_gather_path__label_1.setText(_translate("SecondWindow", "채증 미디어 경로:"))
        self.DE_Gather_Info_gather_metadata__label_1.setText(_translate("SecondWindow", "파일 메타데이터: "))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_8), _translate("SecondWindow", "Tab 1"))
        self.DE_Gather_Info_file__blanklabel_1.setText(_translate("SecondWindow", "채증 정보 파일"))
        self.DE_Gather_Info__addButton_1.setText(_translate("SecondWindow", "+추가"))
        self.DE_Vessel_Info__label_1.setText(_translate("SecondWindow", "선박 정보"))
        self.DE_Vessel_Info_vessel_name__label_1.setText(_translate("SecondWindow", "선박 이름:"))
        self.DE_Vessel_Info_vessel_management_id__label_1.setText(_translate("SecondWindow", "선박 관리 고유 번호:"))
        self.DE_Vessel_Info_vessel_MMSI__label_1.setText(_translate("SecondWindow", "선박 MMSI:"))
        self.DE_Vessel_Info_vessel_callsign__label_1.setText(_translate("SecondWindow", "선박 callsign:"))
        self.DE_Vessel_Info_vessel_IMO__label_1.setText(_translate("SecondWindow", "선박 IMO:"))
        self.DE_Vessel_Info_vessel_MRN__label_1.setText(_translate("SecondWindow", "선박 MRN:"))
        self.DE_Vessel_Info_vessel_tonnage__label_1.setText(_translate("SecondWindow", "선박 톤수:"))
        self.DE_Vessel_Info_vessel_length__label_1.setText(_translate("SecondWindow", "선박 길이:"))
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1.setText(_translate("SecondWindow", "항적 분석 장비수:"))
        self.DE_Vessel_Type__label_1.setText(_translate("SecondWindow", "선박 유형:"))
        self.DE_Marines_Electronics_Info_device_management_id__label_1.setText(_translate("SecondWindow", "장비 관리 고유 번호:"))
        self.DE_Marines_Electronics_Info_device_type__label_1.setText(_translate("SecondWindow", "장비 유형:"))
        self.DE_Marines_Electronics_Info_device_manufacturer__label_1.setText(_translate("SecondWindow", "장비 제조사:"))
        self.DE_Marines_Electronics_Info_device_model_name__label_1.setText(_translate("SecondWindow", "장비 모델명:"))
        self.DE_Marines_Electronics_Info_device_model_serial_number__label_1.setText(_translate("SecondWindow", "장비 모델 시리얼 넘버:"))
        self.DE_Marines_Electronics_Info_device_os_firmware__label_1.setText(_translate("SecondWindow", "장비 os firmware:"))
        self.DE_Marines_Electronics_Info_device_description__label_1.setText(_translate("SecondWindow", "장비 설명:"))
        self.DE_Marine_Electronics_Info__label_1.setText(_translate("SecondWindow", "해양 장비 정보"))
        self.DE_Gather_Info__label_1.setText(_translate("SecondWindow", "채증 정보"))
        self.DE_other_files__label_1.setText(_translate("SecondWindow", "기타 파일(jpg, mp4, txt, bin 등)"))
        self.DE_other_files__addButton_1.setText(_translate("SecondWindow", "+추가"))
        self.DE_other_files_file_browse__label_1.setText(_translate("SecondWindow", "파일 입력:"))
        self.DE_other_files_file_browse__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.DE_other_files_file_browse__EnterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.DE_other_files_id__label_1.setText(_translate("SecondWindow", "고유번호:"))
        self.DE_other_files_type__label_1.setText(_translate("SecondWindow", "파일유형:"))
        self.DE_other_files_file_size__label_1.setText(_translate("SecondWindow", "파일크기:"))
        self.DE_other_files_file_path__label_1.setText(_translate("SecondWindow", "파일 경로:"))
        self.DE_other_files_file_hash_type__label_1.setText(_translate("SecondWindow", "해시 종류:"))
        self.DE_other_files_file_hash_value__label_1.setText(_translate("SecondWindow", "해시값:"))
        self.DE_other_files_file_description__label_1.setText(_translate("SecondWindow", "파일 설명: "))
        self.DE_other_files_file_metadata__label_1.setText(_translate("SecondWindow", "파일 메타데이터:"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_4), _translate("SecondWindow", "Tab 1"))
        self.DE_Acquisition_Info__label_1.setText(_translate("SecondWindow", "수집 정보"))
        self.DE_Acquisition_Info__addButton_1.setText(_translate("SecondWindow", "+추가"))
        self.DE_Authentication_ID__label_1.setText(_translate("SecondWindow", "수집 id"))
        self.DE_Acquisition_Info_acquisition_person_name__label_1.setText(_translate("SecondWindow", "수집자명:"))
        self.DE_Acquisition_Info_acquisition_date_time__label_1.setText(_translate("SecondWindow", "수집 시간:"))
        self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setPlaceholderText(_translate("SecondWindow", "ex) 2021-11-30 19:58:13.829475+09:00"))
        self.DE_Acquisition_Info_acquisition_location__label_1.setText(_translate("SecondWindow", "수집 장소:"))
        self.DE_Acquisition_Info_acquisition_tool__label_1.setText(_translate("SecondWindow", "수집 도구:"))
        self.DE_Acquisition_Info_acquisition_tool_version__label_1.setText(_translate("SecondWindow", "수집 도구 버젼:"))
        self.DE_Authentication_Person_Party_Name__label_1.setText(_translate("SecondWindow", "수집 부서:"))
        self.DE_Acquisition_Info_DEF_serial_no__label_1.setText(_translate("SecondWindow", "일련 번호:"))
        self.DE_Acquisition_Info_DEF_management_id__label_1.setText(_translate("SecondWindow", "관리 번호:"))
        self.DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setText(_translate("SecondWindow", "디지털 증거 유형:"))
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setText(_translate("SecondWindow", "증거 채증 유형:"))
        self.DE_Acquisition_Info_DEF_gather_no__label_1.setText(_translate("SecondWindow", "채증 번호:"))
        self.DE_Acquisition_Info_DEF_browse__label_1.setText(_translate("SecondWindow", "파일입력:"))
        self.DE_Acquisition_Info_DEF_browse__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.DE_Acquisition_Info_DEF_browse__enterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setText(_translate("SecondWindow", "디지털 증거 파일 이름:"))
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setText(_translate("SecondWindow", "디지털 증거 파일 경로:"))
        self.DE_Acquisition_Info_DEF_hash_type__label_1.setText(_translate("SecondWindow", "해시 종류:"))
        self.DE_Acquisition_Info_DEF_hash_value__label_1.setText(_translate("SecondWindow", "해시값:"))
        self.DE_Acquisition_Info_DEF_sector_size__label_1.setText(_translate("SecondWindow", "섹터 크기: "))
        self.DE_Acquisition_Info_DEF_file_size__label_1.setText(_translate("SecondWindow", "파일 크기: "))
        self.DE_Acquisition_Info_DEF__metadata__label_1.setText(_translate("SecondWindow", "파일 메타데이터: "))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_9), _translate("SecondWindow", "Tab 1"))
        self.DE_Acquisition_Info_DEF__label_1.setText(_translate("SecondWindow", "디지털 증거 파일"))
        self.DE_Acquisition_Info_DEF__addButton_1.setText(_translate("SecondWindow", "+추가"))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_6), _translate("SecondWindow", "Tab 1"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), _translate("SecondWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DE_tab), _translate("SecondWindow", "Digital Evidences"))
        self.AI_title__label.setText(_translate("SecondWindow", "분석 정보"))
        self.AI_EquipmentTraces__addButton.setText(_translate("SecondWindow", "+추가"))
        self.AI_Report__label_1.setText(_translate("SecondWindow", "보고서"))
        self.AI_Reports_id__label_1.setText(_translate("SecondWindow", "고유번호:"))
        self.AI_Reports_type__label_1.setText(_translate("SecondWindow", "유형:"))
        self.AI_Reports_subtype__label_1.setText(_translate("SecondWindow", "하위유형:"))
        self.AI_Reports_mgmt_id__label_1.setText(_translate("SecondWindow", "장비 고유번호:"))
        self.AI_Reports_submission_agency__label_1.setText(_translate("SecondWindow", "제출 기관:"))
        self.AI_Reports_reprot_creation_datetime__label_1.setText(_translate("SecondWindow", "보고서 작성 시간:"))
        self.AI_Reports_reprot_creation_datetime__lineEdit_1.setPlaceholderText(_translate("SecondWindow", "ex) 2021-11-30 19:58:13.829475+09:00"))
        self.AI_Reports_division_name_of_report_maker__label_1.setText(_translate("SecondWindow", "보고서 작성 부서명:"))
        self.AI_Reports_team_name_of_report_maker__label_1.setText(_translate("SecondWindow", "보고서 작성 팀명:"))
        self.AI_Reports_file_info__label_1.setText(_translate("SecondWindow", "파일 입력"))
        self.AI_Reports_file_info__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.AI_Reports_file_info__enterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.AI_Reports_file_name__label_1.setText(_translate("SecondWindow", "파일 이름:"))
        self.AI_Reports_file_size__label_1.setText(_translate("SecondWindow", "파일 크기:"))
        self.AI_Reports_file_path__label_1.setText(_translate("SecondWindow", "파일 경로:"))
        self.AI_Reports_file_creation_datetime__label_1.setText(_translate("SecondWindow", "파일 생성 날짜/시간: "))
        self.AI_Reports_file_description__label_1.setText(_translate("SecondWindow", "파일 설명:"))
        self.AI_Reports_file_hash_type__label_1.setText(_translate("SecondWindow", "파일 해시 종류:"))
        self.AI_Reports_file_hash_value__label_1.setText(_translate("SecondWindow", "파일 해시 값:"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_7), _translate("SecondWindow", "Tab 1"))
        self.AI_other_files__label_1.setText(_translate("SecondWindow", "기타 파일(jpg, mp4, txt, bin 등)"))
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
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_3), _translate("SecondWindow", "Tab 1"))
        self.AI_EquipmentTraces__label_1.setText(_translate("SecondWindow", "Equipment Traces (장비별로)"))
        self.AI_EquipmentTraces_id__label_1.setText(_translate("SecondWindow", "고유번호:"))
        self.AI_EquipmentTraces_type__label_1.setText(_translate("SecondWindow", "유형:"))
        self.AI_EquipmentTraces_description__label_1.setText(_translate("SecondWindow", "유형 설명:"))
        self.AI_EquipmentTraces_mgmt_id__label_1.setText(_translate("SecondWindow", "장비 아이디:"))
        self.AI_EquipmentTraces_vessel_id__label_1.setText(_translate("SecondWindow", "선박 고유번호:"))
        self.AI_EquipmentTraces_evidence_id__label_1.setText(_translate("SecondWindow", "증거 고유번호"))
        self.AI_EquipmentTraces_user_trace_info__label_1.setText(_translate("SecondWindow", "사용자 추적 정보"))
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__label_1.setText(_translate("SecondWindow", "시스템 시작 시간:"))
        self.AI_EquipmentTraces_user_trace_info_system_power_on_time__lineEdit_1.setPlaceholderText(_translate("SecondWindow", "ex) 2021-11-30 19:58:13.829475+09:00"))
        self.AI_EquipmentTraces_user_trace_info_track_extractopm_description__label_1.setText(_translate("SecondWindow", "항적 추출 방법:"))
        self.AI_EquipmentTraces_user_trace_info_system_description__label_1.setText(_translate("SecondWindow", "시스템 설명:"))
        self.AI_EquipmentTraces_user_trace_info_system_operation_status__label_1.setText(_translate("SecondWindow", "시스템 운영 상태:"))
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__label_1.setText(_translate("SecondWindow", "시스템 종료 시간:"))
        self.AI_EquipmentTraces_user_trace_info_system_power_off_time__lineEdit_1.setPlaceholderText(_translate("SecondWindow", "ex) 2021-11-30 19:58:13.829475+09:00"))
        self.AI_EquipmentTraces_user_trace_info_track_recording_period__label_1.setText(_translate("SecondWindow", "항적 기록 시간:"))
        self.AI_EquipmentTraces_user_trace_info_track_deletion_trace__label_1.setText(_translate("SecondWindow", "항적 삭제 개수:"))
        self.AI_EquipmentTraces_user_trace_info_user_trace_notes__label_1.setText(_translate("SecondWindow", "비고:"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_5), _translate("SecondWindow", "Tab 1"))
        self.AI_Reports__addButton.setText(_translate("SecondWindow", "+추가"))
        self.AI_other_files__addButton.setText(_translate("SecondWindow", "+추가"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AI_tab), _translate("SecondWindow", "Analysis info"))
        self.Log__addButton.setText(_translate("SecondWindow", "+추가"))
        self.Log_digital_evidence_package_management_id__label_1.setText(_translate("SecondWindow", "디지털 증거 패키지 고유번호:"))
        self.Log_Digital_Evidence_Pack_History_Start_Date_Time__label_1.setText(_translate("SecondWindow", "시작 시간: "))
        self.Log_Digital_Evidence_Pack_History_End_Date_Time__label_1.setText(_translate("SecondWindow", "종료 시간: "))
        self.Log_log_type__label_1.setText(_translate("SecondWindow", "이력 유형:"))
        self.Log_log_description__label_1.setText(_translate("SecondWindow", "이력 설명:"))
        self.Log_devision_name_of_logger__label_1.setText(_translate("SecondWindow", "이력 분석 조직명:"))
        self.Log_team_name_of_logger__label_1.setText(_translate("SecondWindow", "이력 분석 팀명:"))
        self.Log_rank_of_logger__label_1.setText(_translate("SecondWindow", "이력 분석자 계급:"))
        self.Log_name_of_logger__label_1.setText(_translate("SecondWindow", "이력 분석자명:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("SecondWindow", "Tab 1"))
        self.Log__label.setText(_translate("SecondWindow", "디지털 증거 패키지 로그"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Log_tab), _translate("SecondWindow", "Log"))
        self.KSButton.setText(_translate("SecondWindow", "KS 표준으로 내보내기"))
        self.ExportButton.setText(_translate("SecondWindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())

# ++되는 상황
