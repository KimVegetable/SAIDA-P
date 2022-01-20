from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):

    def __init__(self):
        self.DE_Gather_Info_List = list()
        self.DE_Gather_Info_List.append(list())
        self.DE_Gather_Info_Tab_Widget_List = list()

        self.DE_Acquisition_Info_DEF_List = list()
        self.DE_Acquisition_Info_DEF_List.append(list())
        self.DE_Acquisition_Info_DEF_Tab_Widget_List = list()

        self.DE_Acquisition_Info_List = list()
        self.DE_Acquisition_Info_List.append(list())
        self.DE_Acquisition_Info_Tab_Widget_List = list()

        self.DE_AddAll_List = list()

    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(1223, 970)
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
        self.DE__scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1155, 751))
        self.DE__scrollAreaWidgetContents.setObjectName("DE__scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.DE__scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.DE_Gather_Info__scrollArea_1 = QtWidgets.QScrollArea(self.DE__scrollAreaWidgetContents)
        self.DE_Gather_Info__scrollArea_1.setWidgetResizable(True)
        self.DE_Gather_Info__scrollArea_1.setObjectName("DE_Gather_Info__scrollArea_1")
        self.DE_Gather_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.DE_Gather_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 351, 448))
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
        self.DE_Gather_Info_gather_location__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_location__horizontalLayout_1")
        self.DE_Gather_Info_gather_location__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_location__label_1.setObjectName("DE_Gather_Info_gather_location__label_1")
        self.DE_Gather_Info_gather_location__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_location__label_1)
        self.DE_Gather_Info_gather_location__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_location__lineEdit_1.setObjectName("DE_Gather_Info_gather_location__lineEdit_1")
        self.DE_Gather_Info_gather_location__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_location__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_location__horizontalLayout_1)
        self.DE_Gather_Info_gather_person_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_person_name__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_person_name__horizontalLayout_1")
        self.DE_Gather_Info_gather_person_name__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_name__label_1.setObjectName("DE_Gather_Info_gather_person_name__label_1")
        self.DE_Gather_Info_gather_person_name__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_person_name__label_1)
        self.DE_Gather_Info_gather_person_name__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_name__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_person_name__lineEdit_1")
        self.DE_Gather_Info_gather_person_name__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_person_name__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_person_name__horizontalLayout_1)
        self.DE_Gather_Info_gather_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_datetime__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_datetime__horizontalLayout_1")
        self.DE_Gather_Info_gather_datetime__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_datetime__label_1.setObjectName("DE_Gather_Info_gather_datetime__label_1")
        self.DE_Gather_Info_gather_datetime__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_datetime__label_1)
        self.DE_Gather_Info_gather_datetime__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_datetime__lineEdit_1.setObjectName("DE_Gather_Info_gather_datetime__lineEdit_1")
        self.DE_Gather_Info_gather_datetime__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_datetime__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_datetime__horizontalLayout_1)
        self.DE_Gather_Info_gather_person_agency__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_person_agency__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_person_agency__horizontalLayout_1")
        self.DE_Gather_Info_gather_person_agency__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_agency__label_1.setObjectName("DE_Gather_Info_gather_person_agency__label_1")
        self.DE_Gather_Info_gather_person_agency__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_person_agency__label_1)
        self.DE_Gather_Info_gather_person_agency__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_agency__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_person_agency__lineEdit_1")
        self.DE_Gather_Info_gather_person_agency__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_person_agency__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_person_agency__horizontalLayout_1)
        self.DE_Gather_Info_gather_person_rank__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_person_rank__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_person_rank__horizontalLayout_1")
        self.DE_Gather_Info_gather_person_rank__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_rank__label_1.setObjectName("DE_Gather_Info_gather_person_rank__label_1")
        self.DE_Gather_Info_gather_person_rank__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_person_rank__label_1)
        self.DE_Gather_Info_gather_person_rank__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_person_rank__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_person_rank__lineEdit_1")
        self.DE_Gather_Info_gather_person_rank__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_person_rank__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_person_rank__horizontalLayout_1)
        self.DE_Gather_Info_organization_code__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_organization_code__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_organization_code__horizontalLayout_1")
        self.DE_Gather_Info_organization_code__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_organization_code__label_1.setObjectName("DE_Gather_Info_organization_code__label_1")
        self.DE_Gather_Info_organization_code__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_organization_code__label_1)
        self.DE_Gather_Info_organization_code__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_organization_code__lineEdit_1.setObjectName("DE_Gather_Info_organization_code__lineEdit_1")
        self.DE_Gather_Info_organization_code__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_organization_code__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_organization_code__horizontalLayout_1)
        self.DE_Gather_Info_submitter_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_submitter_name__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_submitter_name__horizontalLayout_1")
        self.DE_Gather_Info_submitter_name__label_1 = QtWidgets.QLabel(self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_submitter_name__label_1.setObjectName("DE_Gather_Info_submitter_name__label_1")
        self.DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(self.DE_Gather_Info_submitter_name__label_1)
        self.DE_Gather_Info_submitter_name__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_submitter_name__lineEdit_1.setObjectName("DE_Gather_Info_submitter_name__lineEdit_1")
        self.DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(self.DE_Gather_Info_submitter_name__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_submitter_name__horizontalLayout_1)
        self.DE_Gather_Info_Gather_Source_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_Gather_Source_Name__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_Gather_Source_Name__horizontalLayout_1")
        self.DE_Gather_Info_Gather_Source_Name__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_Gather_Source_Name__label_1.setObjectName("DE_Gather_Info_Gather_Source_Name__label_1")
        self.DE_Gather_Info_Gather_Source_Name__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_Gather_Source_Name__label_1)
        self.DE_Gather_Inf_Gather_Source_Name__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Inf_Gather_Source_Name__lineEdit_1.setObjectName("DE_Gather_Inf_Gather_Source_Name__lineEdit_1")
        self.DE_Gather_Info_Gather_Source_Name__horizontalLayout_1.addWidget(
            self.DE_Gather_Inf_Gather_Source_Name__lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(self.DE_Gather_Info_Gather_Source_Name__horizontalLayout_1)
        self.DE_Gather_Info_Gather_Relation_Person_Type_Code___horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_Gather_Relation_Person_Type_Code___horizontalLayout_1.setObjectName(
            "DE_Gather_Info_Gather_Relation_Person_Type_Code___horizontalLayout_1")
        self.DE_Gather_Info_Gather_Relation_Person_Type_Code___label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_Gather_Relation_Person_Type_Code___label_1.setObjectName(
            "DE_Gather_Info_Gather_Relation_Person_Type_Code___label_1")
        self.DE_Gather_Info_Gather_Relation_Person_Type_Code___horizontalLayout_1.addWidget(
            self.DE_Gather_Info_Gather_Relation_Person_Type_Code___label_1)
        self.DE_Gather_Info_Gather_Relation_Person_Type_Code___lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_Gather_Relation_Person_Type_Code___lineEdit_1.setObjectName(
            "DE_Gather_Info_Gather_Relation_Person_Type_Code___lineEdit_1")
        self.DE_Gather_Info_Gather_Relation_Person_Type_Code___horizontalLayout_1.addWidget(
            self.DE_Gather_Info_Gather_Relation_Person_Type_Code___lineEdit_1)
        self.DE_Gather_Info__verticalLayout_1.addLayout(
            self.DE_Gather_Info_Gather_Relation_Person_Type_Code___horizontalLayout_1)
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
        self.DE_Gather_Info_file__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 288, 185))
        self.DE_Gather_Info_file__scrollAreaWidgetContents_1.setObjectName(
            "DE_Gather_Info_file__scrollAreaWidgetContents_1")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.DE_Gather_Info_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Gather_Info_file__verticalLayout_1.setObjectName("DE_Gather_Info_file__verticalLayout_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__horizontalLayout_1")
        self.DE_Gather_Info_file__filebrowse__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__filebrowse__label_1.setObjectName("DE_Gather_Info_file__filebrowse__label_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_file__filebrowse__label_1)
        self.DE_Gather_Info_file__filebrowse__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__filebrowse__lineEdit_1.setObjectName("DE_Gather_Info_file__filebrowse__lineEdit_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_file__filebrowse__lineEdit_1)
        self.DE_Gather_Info_file__filebrowse__browseButton_1 = QtWidgets.QPushButton(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__filebrowse__browseButton_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__browseButton_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_file__filebrowse__browseButton_1)
        self.DE_Gather_Info_file__filebrowse__enterButton_1 = QtWidgets.QPushButton(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__filebrowse__enterButton_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__enterButton_1")
        self.DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_file__filebrowse__enterButton_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_file__filebrowse__horizontalLayout_1)
        self.DE_Gather_Info_gather_media_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_media_type__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_media_type__horizontalLayout_1")
        self.DE_Gather_Info_gather_media_type__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_media_type__label_1.setObjectName("DE_Gather_Info_gather_media_type__label_1")
        self.DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_media_type__label_1)
        self.DE_Gather_Info_gather_media_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_media_type__lineEdit_1.setObjectName("DE_Gather_Info_gather_media_type__lineEdit_1")
        self.DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_media_type__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_media_type__horizontalLayout_1)
        self.DE_Gather_Info_gather_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_hash_type__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_hash_type__horizontalLayout_1")
        self.DE_Gather_Info__gather_hash_type__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info__gather_hash_type__label_1.setObjectName("DE_Gather_Info__gather_hash_type__label_1")
        self.DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(
            self.DE_Gather_Info__gather_hash_type__label_1)
        self.DE_Gather_Info__gather_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info__gather_hash_type__lineEdit_1.setObjectName("DE_Gather_Info__gather_hash_type__lineEdit_1")
        self.DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(
            self.DE_Gather_Info__gather_hash_type__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_hash_type__horizontalLayout_1)
        self.DE_Gather_Info_gather_hash__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_hash__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_hash__horizontalLayout_1")
        self.DE_Gather_Info_gather_hash__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_hash__label_1.setObjectName("DE_Gather_Info_gather_hash__label_1")
        self.DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_hash__label_1)
        self.DE_Gather_Info_gather_hash__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_hash__lineEdit_1.setObjectName("DE_Gather_Info_gather_hash__lineEdit_1")
        self.DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_hash__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_hash__horizontalLayout_1)
        self.DE_Gather_Info_gather_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_path__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_path__horizontalLayout_1")
        self.DE_Gather_Info_gather_path__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_path__label_1.setObjectName("DE_Gather_Info_gather_path__label_1")
        self.DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_path__label_1)
        self.DE_Gather_Info_gather_path__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_path__lineEdit_1.setObjectName("DE_Gather_Info_gather_path__lineEdit_1")
        self.DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_path__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_path__horizontalLayout_1)
        self.DE_Gather_Info_gather_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_gather_metadata__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_metadata__horizontalLayout_1")
        self.DE_Gather_Info_gather_metadata__label_1 = QtWidgets.QLabel(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_metadata__label_1.setObjectName("DE_Gather_Info_gather_metadata__label_1")
        self.DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(self.DE_Gather_Info_gather_metadata__label_1)
        self.DE_Gather_Info_gather_metadata__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_gather_metadata__lineEdit_1.setObjectName("DE_Gather_Info_gather_metadata__lineEdit_1")
        self.DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(
            self.DE_Gather_Info_gather_metadata__lineEdit_1)
        self.DE_Gather_Info_file__verticalLayout_1.addLayout(self.DE_Gather_Info_gather_metadata__horizontalLayout_1)
        self.gridLayout_18.addLayout(self.DE_Gather_Info_file__verticalLayout_1, 1, 0, 1, 1)
        self.DE_Gather_Info_file__scrollArea_1.setWidget(self.DE_Gather_Info_file__scrollAreaWidgetContents_1)
        self.DE_Gather_Info_file__horizontalLayout_1.addWidget(self.DE_Gather_Info_file__scrollArea_1)
        self.gridLayout_27.addLayout(self.DE_Gather_Info_file__horizontalLayout_1, 0, 0, 1, 1)
        self.tabWidget_9.addTab(self.tab_8, "")
        self.gridLayout_3.addWidget(self.tabWidget_9, 2, 0, 1, 1)
        self.DE_Gather_Info_file_addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Gather_Info_file_addButton__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_file_addButton__horizontalLayout_1")
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
        self.DE_Vessel_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 368, 331))
        self.DE_Vessel_Info__scrollAreaWidgetContents_1.setObjectName("DE_Vessel_Info__scrollAreaWidgetContents_1")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.DE_Vessel_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Vessel_Info__verticalLayout_1.setObjectName("DE_Vessel_Info__verticalLayout_1")
        self.DE_Veseel_Info_vessel_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Veseel_Info_vessel_name__horizontalLayout_1.setObjectName(
            "DE_Veseel_Info_vessel_name__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_name__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_name__label_1.setObjectName("DE_Vessel_Info_vessel_name__label_1")
        self.DE_Veseel_Info_vessel_name__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_name__label_1)
        self.DE_Vessel_Info_vessel_name__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_name__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_name__lineEdit_1")
        self.DE_Veseel_Info_vessel_name__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_name__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Veseel_Info_vessel_name__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_management_id__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_management_id__label_1 = QtWidgets.QLabel(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_management_id__label_1.setObjectName("DE_Vessel_Info_vessel_management_id__label_1")
        self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1.addWidget(
            self.DE_Vessel_Info_vessel_management_id__label_1)
        self.DE_Vessel_Info_vessel_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_management_id__lineEdit_1.setObjectName(
            "DE_Vessel_Info_vessel_management_id__lineEdit_1")
        self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1.addWidget(
            self.DE_Vessel_Info_vessel_management_id__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_management_id__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_MMSI__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_MMSI__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_MMSI__label_1.setObjectName("DE_Vessel_Info_vessel_MMSI__label_1")
        self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_MMSI__label_1)
        self.DE_Vessel_Info_vessel_MMSI__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_MMSI__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_MMSI__lineEdit_1")
        self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_MMSI__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_MMSI__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_callsign__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_callsign__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_callsign__label_1.setObjectName("DE_Vessel_Info_vessel_callsign__label_1")
        self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_callsign__label_1)
        self.DE_Vessel_Info_vessel_callsign__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_callsign__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_callsign__lineEdit_1")
        self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1.addWidget(
            self.DE_Vessel_Info_vessel_callsign__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_callsign__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_IMO__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_IMO__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_IMO__label_1.setObjectName("DE_Vessel_Info_vessel_IMO__label_1")
        self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_IMO__label_1)
        self.DE_Vessel_Info_vessel_IMO__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_IMO__lineEdit_1.setPlaceholderText("")
        self.DE_Vessel_Info_vessel_IMO__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_IMO__lineEdit_1")
        self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_IMO__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_IMO__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_MRN__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_MRN__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_MRN__label_1.setObjectName("DE_Vessel_Info_vessel_MRN__label_1")
        self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_MRN__label_1)
        self.DE_Vessel_Info_vessel_MRN__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_MRN__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_MRN__lineEdit_1")
        self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_MRN__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_MRN__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_tonnage__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_tonnage__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_tonnage__label_1.setObjectName("DE_Vessel_Info_vessel_tonnage__label_1")
        self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_tonnage__label_1)
        self.DE_Vessel_Info_vessel_tonnage__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_tonnage__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_tonnage__lineEdit_1")
        self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_tonnage__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_tonnage__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_length__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_length__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_length__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_length__label_1 = QtWidgets.QLabel(self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_length__label_1.setObjectName("DE_Vessel_Info_vessel_length__label_1")
        self.DE_Vessel_Info_vessel_length__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_length__label_1)
        self.DE_Vessel_Info_vessel_length__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_length__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_length__lineEdit_1")
        self.DE_Vessel_Info_vessel_length__horizontalLayout_1.addWidget(self.DE_Vessel_Info_vessel_length__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(self.DE_Vessel_Info_vessel_length__horizontalLayout_1)
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1")
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1 = QtWidgets.QLabel(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1.setObjectName(
            "DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1")
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.addWidget(
            self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1)
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Vessel_Info__scrollAreaWidgetContents_1)
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1.setObjectName(
            "DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1")
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.addWidget(
            self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1)
        self.DE_Vessel_Info__verticalLayout_1.addLayout(
            self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1)
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
        self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 359, 331))
        self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1.setObjectName(
            "DE_Marines_Electronics_Info__scrollAreaWidgetContents_1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.DE_Marines_Electronics_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Marines_Electronics_Info__verticalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info__verticalLayout_1")
        self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_management_id__label_1 = QtWidgets.QLabel(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_management_id__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_management_id__label_1")
        self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_management_id__label_1)
        self.DE_Marines_Electronics_Info_device_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_management_id__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_management_id__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_management_id__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            self.DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_type__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_type__label_1 = QtWidgets.QLabel(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_type__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_type__label_1")
        self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_type__label_1)
        self.DE_Marines_Electronics_Info_device_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_type__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_type__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_type__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            self.DE_Marines_Electronics_Info_device_type__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_manufacturer__label_1 = QtWidgets.QLabel(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_manufacturer__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_manufacturer__label_1")
        self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_manufacturer__label_1)
        self.DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            self.DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_model_name__label_1 = QtWidgets.QLabel(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_model_name__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_name__label_1")
        self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_model_name__label_1)
        self.DE_Marines_Electronics_Info_device_model_name__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_model_name__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_name__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_model_name__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            self.DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_model_serial_number__label_1 = QtWidgets.QLabel(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_model_serial_number__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_serial_number__label_1")
        self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_model_serial_number__label_1)
        self.DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            self.DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_os_firmware__label_1 = QtWidgets.QLabel(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_os_firmware__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_os_firmware__label_1")
        self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_os_firmware__label_1)
        self.DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            self.DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1)
        self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_description__horizontalLayout_1")
        self.DE_Marines_Electronics_Info_device_description__label_1 = QtWidgets.QLabel(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_description__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_description__label_1")
        self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_description__label_1)
        self.DE_Marines_Electronics_Info_device_description__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.DE_Marines_Electronics_Info_device_description__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_description__lineEdit_1")
        self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1.addWidget(
            self.DE_Marines_Electronics_Info_device_description__lineEdit_1)
        self.DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            self.DE_Marines_Electronics_Info_device_description__horizontalLayout_1)
        self.gridLayout_6.addLayout(self.DE_Marines_Electronics_Info__verticalLayout_1, 0, 0, 1, 1)
        self.DE_Marines_Electronics_Info__scrollArea_1.setWidget(
            self.DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        self.gridLayout_7.addWidget(self.DE_Marines_Electronics_Info__scrollArea_1, 1, 2, 1, 1)
        self.DE_Marine_Electronics_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Marine_Electronics_Info__horizontalLayout_1.setObjectName(
            "DE_Marine_Electronics_Info__horizontalLayout_1")
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
        self.DE_other_files__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 335, 287))
        self.DE_other_files__scrollAreaWidgetContents_1.setObjectName("DE_other_files__scrollAreaWidgetContents_1")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.DE_other_files__scrollAreaWidgetContents_1)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.DE_other_files__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_other_files__verticalLayout_1.setObjectName("DE_other_files__verticalLayout_1")
        self.DE_other_files_file_browse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_browse__horizontalLayout_1.setObjectName(
            "DE_other_files_file_browse__horizontalLayout_1")
        self.DE_other_files_file_browse__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_browse__label_1.setObjectName("DE_other_files_file_browse__label_1")
        self.DE_other_files_file_browse__horizontalLayout_1.addWidget(self.DE_other_files_file_browse__label_1)
        self.DE_other_files_file_browse__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_browse__lineEdit_1.setObjectName("DE_other_files_file_browse__lineEdit_1")
        self.DE_other_files_file_browse__horizontalLayout_1.addWidget(self.DE_other_files_file_browse__lineEdit_1)
        self.DE_other_files_file_browse__browseButton_1 = QtWidgets.QPushButton(
            self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_browse__browseButton_1.setObjectName("DE_other_files_file_browse__browseButton_1")
        self.DE_other_files_file_browse__horizontalLayout_1.addWidget(self.DE_other_files_file_browse__browseButton_1)
        self.DE_other_files_file_browse__EnterButton_1 = QtWidgets.QPushButton(
            self.DE_other_files__scrollAreaWidgetContents_1)
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
        self.DE_other_files_file_hash_type__horizontalLayout_1.setObjectName(
            "DE_other_files_file_hash_type__horizontalLayout_1")
        self.DE_other_files_file_hash_type__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_hash_type__label_1.setObjectName("DE_other_files_file_hash_type__label_1")
        self.DE_other_files_file_hash_type__horizontalLayout_1.addWidget(self.DE_other_files_file_hash_type__label_1)
        self.DE_other_files_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_hash_type__lineEdit_1.setObjectName("DE_other_files_file_hash_type__lineEdit_1")
        self.DE_other_files_file_hash_type__horizontalLayout_1.addWidget(self.DE_other_files_file_hash_type__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_hash_type__horizontalLayout_1)
        self.DE_other_files_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_hash_value__horizontalLayout_1.setObjectName(
            "DE_other_files_file_hash_value__horizontalLayout_1")
        self.DE_other_files_file_hash_value__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_hash_value__label_1.setObjectName("DE_other_files_file_hash_value__label_1")
        self.DE_other_files_file_hash_value__horizontalLayout_1.addWidget(self.DE_other_files_file_hash_value__label_1)
        self.DE_other_files_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_hash_value__lineEdit_1.setObjectName("DE_other_files_file_hash_value__lineEdit_1")
        self.DE_other_files_file_hash_value__horizontalLayout_1.addWidget(
            self.DE_other_files_file_hash_value__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_hash_value__horizontalLayout_1)
        self.DE_other_files_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_description__horizontalLayout_1.setObjectName(
            "DE_other_files_file_description__horizontalLayout_1")
        self.DE_other_files_file_description__label_1 = QtWidgets.QLabel(
            self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_description__label_1.setObjectName("DE_other_files_file_description__label_1")
        self.DE_other_files_file_description__horizontalLayout_1.addWidget(
            self.DE_other_files_file_description__label_1)
        self.DE_other_files_file_description__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_description__lineEdit_1.setObjectName("DE_other_files_file_description__lineEdit_1")
        self.DE_other_files_file_description__horizontalLayout_1.addWidget(
            self.DE_other_files_file_description__lineEdit_1)
        self.DE_other_files__verticalLayout_1.addLayout(self.DE_other_files_file_description__horizontalLayout_1)
        self.DE_other_files_file_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_other_files_file_metadata__horizontalLayout_1.setObjectName(
            "DE_other_files_file_metadata__horizontalLayout_1")
        self.DE_other_files_file_metadata__label_1 = QtWidgets.QLabel(self.DE_other_files__scrollAreaWidgetContents_1)
        self.DE_other_files_file_metadata__label_1.setObjectName("DE_other_files_file_metadata__label_1")
        self.DE_other_files_file_metadata__horizontalLayout_1.addWidget(self.DE_other_files_file_metadata__label_1)
        self.DE_other_files_file_metadata__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_other_files__scrollAreaWidgetContents_1)
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
        self.DE_Acquisition_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 368, 657))
        self.DE_Acquisition_Info__scrollAreaWidgetContents_1.setObjectName(
            "DE_Acquisition_Info__scrollAreaWidgetContents_1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.DE_Acquisition_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Acquisition_Info__verticalLayout_1.setObjectName("DE_Acquisition_Info__verticalLayout_1")
        self.DE_Authentication_ID__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Authentication_ID__horizontalLayout_1.setObjectName("DE_Authentication_ID__horizontalLayout_1")
        self.DE_Authentication_ID__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Authentication_ID__label_1.setObjectName("DE_Authentication_ID__label_1")
        self.DE_Authentication_ID__horizontalLayout_1.addWidget(self.DE_Authentication_ID__label_1)
        self.DE_Authentication_ID__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Authentication_ID__lineEdit_1.setObjectName("DE_Authentication_ID__lineEdit_1")
        self.DE_Authentication_ID__horizontalLayout_1.addWidget(self.DE_Authentication_ID__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(self.DE_Authentication_ID__horizontalLayout_1)
        self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_person_name__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_person_name__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_person_name__label_1")
        self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_person_name__label_1)
        self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_person_name__lineEdit_1")
        self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1)
        self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_date_time__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_date_time__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_date_time__label_1")
        self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_date_time__label_1)
        self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_date_time__lineEdit_1")
        self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1)
        self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.setObjectName(
            "DE_Acquisiton_Info_acquisition_location__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_location__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_location__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_location__label_1")
        self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_location__label_1)
        self.DE_Acquisition_Info_acquisition_location__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_location__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_location__lineEdit_1")
        self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_location__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(
            self.DE_Acquisiton_Info_acquisition_location__horizontalLayout_1)
        self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_tool__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_tool__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool__label_1")
        self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_tool__label_1)
        self.DE_Acquisition_Info_acquisition_tool__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_tool__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool__lineEdit_1")
        self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_tool__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_acquisition_tool__horizontalLayout_1)
        self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1")
        self.DE_Acquisition_Info_acquisition_tool_version__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_tool_version__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool_version__label_1")
        self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_tool_version__label_1)
        self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool_version__lineEdit_1")
        self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1)
        self.DE_Authentication_Person_Party_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Authentication_Person_Party_Name__horizontalLayout_1.setObjectName(
            "DE_Authentication_Person_Party_Name__horizontalLayout_1")
        self.DE_Authentication_Person_Party_Name__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Authentication_Person_Party_Name__label_1.setObjectName("DE_Authentication_Person_Party_Name__label_1")
        self.DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(
            self.DE_Authentication_Person_Party_Name__label_1)
        self.DE_Authentication_Person_Party_Name__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Authentication_Person_Party_Name__lineEdit_1.setObjectName(
            "DE_Authentication_Person_Party_Name__lineEdit_1")
        self.DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(
            self.DE_Authentication_Person_Party_Name__lineEdit_1)
        self.DE_Acquisition_Info__verticalLayout_1.addLayout(
            self.DE_Authentication_Person_Party_Name__horizontalLayout_1)
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
        self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 307, 381))
        self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setObjectName(
            "DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.setObjectName(
            "DE_Acquisition_Info__DEF_file__verticalLayout_1")
        self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_serial_no__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_serial_no__label_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__label_1")
        self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_serial_no__label_1)
        self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_serial_no__lineEdit_1")
        self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_management_id__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_management_id__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__label_1")
        self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_management_id__label_1)
        self.DE_Acquisition_Info_DEF_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_management_id__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__lineEdit_1")
        self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_management_id__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_type__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__label_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_digital_evidence_type__label_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__label_1")
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_evidences_gathering_type__label_1)
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1")
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_gather_no__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_gather_no__label_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__label_1")
        self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_gather_no__label_1)
        self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_gather_no__lineEdit_1")
        self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_browse__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        self.DE_Acquisition_Info_DEF_browse__label_1.setObjectName("DE_Acquisition_Info_DEF_browse__label_1")
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_browse__label_1)
        self.DE_Acquisition_Info_DEF_browse__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_browse__lineEdit_1")
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_browse__lineEdit_1)
        self.DE_Acquisition_Info_DEF_browse__browseButton_1 = QtWidgets.QPushButton(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_browse__browseButton_1.setObjectName(
            "DE_Acquisition_Info_DEF_browse__browseButton_1")
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_browse__browseButton_1)
        self.DE_Acquisition_Info_DEF_browse__enterButton_1 = QtWidgets.QPushButton(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_browse__enterButton_1.setObjectName(
            "DE_Acquisition_Info_DEF_browse__enterButton_1")
        self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_browse__enterButton_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1")
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_hash_type__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_hash_type__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__label_1")
        self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_hash_type__label_1)
        self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_type__lineEdit_1")
        self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_hash_value__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_hash_value__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__label_1")
        self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_hash_value__label_1)
        self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_value__lineEdit_1")
        self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_sector_size__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_sector_size__label_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__label_1")
        self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_sector_size__label_1)
        self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_sector_size__lineEdit_1")
        self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_size__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF_file_size__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_file_size__label_1.setObjectName("DE_Acquisition_Info_DEF_file_size__label_1")
        self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_file_size__label_1)
        self.DE_Acquisition_Info_DEF_file_size__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF_file_size__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_size__lineEdit_1")
        self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF_file_size__horizontalLayout_1)
        self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF__metadata__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF__metadata__label_1 = QtWidgets.QLabel(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF__metadata__label_1.setObjectName("DE_Acquisition_Info_DEF__metadata__label_1")
        self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF__metadata__label_1)
        self.DE_Acquisition_Info_DEF__metadata__lineEdit_1 = QtWidgets.QLineEdit(
            self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF__metadata__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF__metadata__lineEdit_1")
        self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(
            self.DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        self.DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            self.DE_Acquisition_Info_DEF__metadata__horizontalLayout_1)
        self.gridLayout_15.addLayout(self.DE_Acquisition_Info__DEF_file__verticalLayout_1, 0, 0, 1, 1)
        self.DE_Acquisition_Info_file__scrollArea_1.setWidget(self.DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        self.gridLayout_17.addWidget(self.DE_Acquisition_Info_file__scrollArea_1, 0, 0, 1, 1)
        self.tabWidget_10.addTab(self.tab_9, "")
        self.gridLayout_4.addWidget(self.tabWidget_10, 2, 0, 1, 1)
        self.DE_Acquisition_Info_DEF__addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF__addButton__horizontalLayout_1")
        self.DE_Acquisition_Info_DEF__label_1 = QtWidgets.QLabel(self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
        self.DE_Acquisition_Info_DEF__label_1.setObjectName("DE_Acquisition_Info_DEF__label_1")
        self.DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(self.DE_Acquisition_Info_DEF__label_1)
        self.DE_Acquisition_Info_DEF__addButton_1 = QtWidgets.QPushButton(
            self.DE_Acquisition_Info__scrollAreaWidgetContents_1)
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
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

        tmp_list = list()
        tmp_list.append(self.DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_path__lineEdit_1)
        tmp_list.append(self.DE_Gather_Info_gather_metadata__lineEdit_1)
        self.DE_Gather_Info_List[0].append(tmp_list)

        tmp_list = list()
        tmp_list.append(self.DE_Acquisition_Info_DEF_browse__browseButton_1)  # 0
        tmp_list.append(self.DE_Acquisition_Info_DEF_browse__enterButton_1)  # 1

        tmp_list.append(self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1)  # 2
        tmp_list.append(self.DE_Acquisition_Info_DEF_management_id__lineEdit_1)  # 3
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)  # 4
        tmp_list.append(self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)  # 5
        tmp_list.append(self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1)  # 6

        tmp_list.append(self.DE_Acquisition_Info_DEF_browse__lineEdit_1)  # 7
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        self.DE_Acquisition_Info_DEF_List[0].append(tmp_list)

        tmp_list = list()
        tmp_list.append(self.DE_Acquisition_Info__addButton_1)
        tmp_list.append(self.DE_Authentication_ID__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_location__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_tool__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)  #
        tmp_list.append(self.DE_Authentication_Person_Party_Name__lineEdit_1)

        tmp_list.append(self.DE_Acquisition_Info_DEF_browse__browseButton_1)  # 0
        tmp_list.append(self.DE_Acquisition_Info_DEF_browse__enterButton_1)  # 1

        tmp_list.append(self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1)  # 2
        tmp_list.append(self.DE_Acquisition_Info_DEF_management_id__lineEdit_1)  # 3
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)  # 4
        tmp_list.append(self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)  # 5
        tmp_list.append(self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1)  # 6

        tmp_list.append(self.DE_Acquisition_Info_DEF_browse__lineEdit_1)  # 7
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        self.DE_Acquisition_Info_List[0].append(tmp_list)

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
        tmp_list.append(self.DE_Gather_Info_organization_code__lineEdit_1)  # 23
        tmp_list.append(self.DE_Gather_Info_submitter_name__lineEdit_1)  # 24
        tmp_list.append(self.DE_Gather_Inf_Gather_Source_Name__lineEdit_1)  # 25
        tmp_list.append(self.DE_Gather_Info_Gather_Relation_Person_Type_Code___lineEdit_1)  # 26

        tmp_list.append(self.DE_other_files_file_browse__lineEdit_1)  # 0
        tmp_list.append(self.DE_other_files_id__lineEdit_1)  #
        tmp_list.append(self.DE_other_files_type__lineEdit_1)  #
        tmp_list.append(self.DE_other_files_file_size__lineEdit_1)  #
        tmp_list.append(self.DE_other_files_file_path__lineEdit_1)  #
        tmp_list.append(self.DE_other_files_file_hash_type__lineEdit_1)  #
        tmp_list.append(self.DE_other_files_file_hash_value__lineEdit_1)  #
        tmp_list.append(self.DE_other_files_file_description__lineEdit_1)  #
        tmp_list.append(self.DE_other_files_file_metadata__lineEdit_1)

        # Acquisition_Info
        tmp_list.append(self.DE_Authentication_ID__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_person_name__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_location__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_tool__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)  #
        tmp_list.append(self.DE_Authentication_Person_Party_Name__lineEdit_1)

        # DEF Acquisition 추가
        tmp_list.append(self.DE_Acquisition_Info_DEF_serial_no__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_management_id__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_gather_no__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_browse__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_type__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_hash_value__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_sector_size__lineEdit_1)  #
        tmp_list.append(self.DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_list.append(self.DE_Acquisition_Info_DEF__metadata__lineEdit_1)  #
        self.DE_AddAll_List.append(tmp_list)

        self.DE__addButton.clicked.connect(self.DE_AddTab)

        self.DE_Gather_Info_Tab_Widget_List.append(self.tabWidget_9)

        self.DE_Gather_Info__addButton_1.clicked.connect(lambda: self.DE_Gather_Info_AddTab(0))

        self.DE_Acquisition_Info_DEF_Tab_Widget_List.append(self.tabWidget_10)  # tabWidget_DEF(10) tab_DEF(9)

        self.DE_Acquisition_Info__addButton_1.clicked.connect(self.DE_Acquisition_Info_AddTab)

        self.DE_Acquisition_Info_DEF__addButton_1.clicked.connect(lambda: self.DE_Acquisition_Info_DEF_AddTab(0, 0))

        self.DE_Acquisition_Info_Tab_Widget_List.append(self.tabWidget_8)

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
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 288, 185))
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1.setObjectName(
            "DE_Gather_Info_file__scrollAreaWidgetContents_1")
        tmp_gridLayout_18 = QtWidgets.QGridLayout(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_gridLayout_18.setObjectName("gridLayout_18")
        tmp_DE_Gather_Info_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Gather_Info_file__verticalLayout_1.setObjectName("DE_Gather_Info_file__verticalLayout_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__horizontalLayout_1")
        tmp_DE_Gather_Info_file__filebrowse__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__label_1.setObjectName("DE_Gather_Info_file__filebrowse__label_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__filebrowse__label_1)
        tmp_DE_Gather_Info_file__filebrowse__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__lineEdit_1.setObjectName("DE_Gather_Info_file__filebrowse__lineEdit_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1 = QtWidgets.QPushButton(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__browseButton_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__browseButton_1)
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1 = QtWidgets.QPushButton(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__enterButton_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__enterButton_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_media_type__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_media_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_media_type__label_1.setObjectName("DE_Gather_Info_gather_media_type__label_1")
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_media_type__label_1)
        tmp_DE_Gather_Info_gather_media_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_media_type__lineEdit_1.setObjectName("DE_Gather_Info_gather_media_type__lineEdit_1")
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_hash_type__horizontalLayout_1")
        tmp_DE_Gather_Info__gather_hash_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__gather_hash_type__label_1.setObjectName("DE_Gather_Info__gather_hash_type__label_1")
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(tmp_DE_Gather_Info__gather_hash_type__label_1)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1.setObjectName("DE_Gather_Info__gather_hash_type__lineEdit_1")
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_hash__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_hash__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_hash__label_1.setObjectName("DE_Gather_Info_gather_hash__label_1")
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_hash__label_1)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1.setObjectName("DE_Gather_Info_gather_hash__lineEdit_1")
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_hash__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_path__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_path__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_path__label_1.setObjectName("DE_Gather_Info_gather_path__label_1")
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_path__label_1)
        tmp_DE_Gather_Info_gather_path__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_path__lineEdit_1.setObjectName("DE_Gather_Info_gather_path__lineEdit_1")
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_path__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_metadata__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_metadata__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_metadata__label_1.setObjectName("DE_Gather_Info_gather_metadata__label_1")
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_metadata__label_1)
        tmp_DE_Gather_Info_gather_metadata__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
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

        tmp_DE_Gather_Info_file__filebrowse__label_1.setText("파일 입력")
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.setText("Browse...")
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.setText("Enter")

        tmp_DE_Gather_Info_gather_media_type__label_1.setText("채증 미디어 유형:")
        tmp_DE_Gather_Info__gather_hash_type__label_1.setText("채증 미디어 해시 종류:")
        tmp_DE_Gather_Info_gather_hash__label_1.setText("채증 미디어 해시값")
        tmp_DE_Gather_Info_gather_path__label_1.setText("채증 미디어 경로:")
        tmp_DE_Gather_Info_gather_metadata__label_1.setText("파일 메타데이터:")

    def DE_Acquisition_Info_DEF_AddTab(self, a, b):
        tmp_tab_9 = QtWidgets.QWidget()
        tmp_tab_9.setObjectName("tab_9")
        tmp_gridLayout_17 = QtWidgets.QGridLayout(tmp_tab_9)
        tmp_gridLayout_17.setObjectName("gridLayout_17")
        tmp_DE_Acquisition_Info_file__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_9)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setObjectName("DE_Acquisition_Info_file__scrollArea_1")
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 307, 381))
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setObjectName(
            "DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1")
        tmp_gridLayout_15 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_15.setObjectName("gridLayout_15")
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.setObjectName(
            "DE_Acquisition_Info__DEF_file__verticalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__label_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_serial_no__label_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_management_id__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__label_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_management_id__label_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__label_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__label_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_gather_no__label_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_gather_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_browse__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setObjectName("DE_Acquisition_Info_DEF_browse__label_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__label_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_browse__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1 = QtWidgets.QPushButton(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1.setObjectName(
            "DE_Acquisition_Info_DEF_browse__browseButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__browseButton_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1 = QtWidgets.QPushButton(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1.setObjectName(
            "DE_Acquisition_Info_DEF_browse__enterButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__enterButton_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_type__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_value__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_value__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__label_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_sector_size__label_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_sector_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_file_size__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__label_1.setObjectName("DE_Acquisition_Info_DEF_file_size__label_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_file_size__label_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF__metadata__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__metadata__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__label_1.setObjectName("DE_Acquisition_Info_DEF__metadata__label_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF__metadata__label_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF__metadata__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1)
        tmp_gridLayout_15.addLayout(tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidget(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_17.addWidget(tmp_DE_Acquisition_Info_file__scrollArea_1, 0, 0, 1, 1)
        self.DE_Acquisition_Info_DEF_Tab_Widget_List[b].addTab(tmp_tab_9, "Tab" + str(
            len(self.DE_Acquisition_Info_DEF_List[b]) + 1))

        # a = DEF의 widget 숫자

        # b = Acquisition widget 숫자

        tmp_list = list()
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_browse__browseButton_1)  # 0
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_browse__enterButton_1)  # 1

        tmp_list.append(tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)  # 2
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)  # 3
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)  # 4
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)  # 5
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)  # 6

        tmp_list.append(tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)  # 7
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        self.DE_Acquisition_Info_DEF_List[a].append(tmp_list)

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

    def DE_Acquisition_Info_AddTab(self, a):
        self.DE_Acquisition_Info_DEF_List.append(list())

        tmp_tab_6 = QtWidgets.QWidget()
        tmp_tab_6.setObjectName("tab_6")
        tmp_gridLayout_29 = QtWidgets.QGridLayout(tmp_tab_6)
        tmp_gridLayout_29.setObjectName("gridLayout_29")
        tmp_DE_Acquisition_Info__scrollArea_1 = QtWidgets.QScrollArea(tmp_tab_6)
        tmp_DE_Acquisition_Info__scrollArea_1.setWidgetResizable(True)
        tmp_DE_Acquisition_Info__scrollArea_1.setObjectName("DE_Acquisition_Info__scrollArea_1")
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 368, 657))
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1.setObjectName(
            "DE_Acquisition_Info__scrollAreaWidgetContents_1")
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
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_person_name__label_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_person_name__label_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_person_name__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_date_time__label_1")
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_date_time__label_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_date_time__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1)
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.setObjectName(
            "DE_Acquisiton_Info_acquisition_location__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_location__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_location__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_location__label_1")
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_location__label_1)
        tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_location__lineEdit_1")
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1)
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_tool__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool__label_1.setObjectName("DE_Acquisition_Info_acquisition_tool__label_1")
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_tool__label_1)
        tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool_version__label_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_tool_version__label_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool_version__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1)
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.setObjectName(
            "DE_Authentication_Person_Party_Name__horizontalLayout_1")
        tmp_DE_Authentication_Person_Party_Name__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_Person_Party_Name__label_1.setObjectName("DE_Authentication_Person_Party_Name__label_1")
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(
            tmp_DE_Authentication_Person_Party_Name__label_1)
        tmp_DE_Authentication_Person_Party_Name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_Person_Party_Name__lineEdit_1.setObjectName(
            "DE_Authentication_Person_Party_Name__lineEdit_1")
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(
            tmp_DE_Authentication_Person_Party_Name__lineEdit_1)
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
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 307, 381))
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setObjectName(
            "DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1")
        tmp_gridLayout_15 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_15.setObjectName("gridLayout_15")
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.setObjectName(
            "DE_Acquisition_Info__DEF_file__verticalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__label_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_serial_no__label_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_management_id__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__label_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_management_id__label_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__label_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__label_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_gather_no__label_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_gather_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_browse__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setObjectName("DE_Acquisition_Info_DEF_browse__label_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__label_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_browse__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1 = QtWidgets.QPushButton(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1.setObjectName(
            "DE_Acquisition_Info_DEF_browse__browseButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__browseButton_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1 = QtWidgets.QPushButton(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1.setObjectName(
            "DE_Acquisition_Info_DEF_browse__enterButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__enterButton_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_type__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_value__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_value__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1.setObjectName("DE_Acquisition_Info_DEF_sector_size__label_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_sector_size__label_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_sector_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_file_size__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__label_1.setObjectName("DE_Acquisition_Info_DEF_file_size__label_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_file_size__label_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF__metadata__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__metadata__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__label_1.setObjectName("DE_Acquisition_Info_DEF__metadata__label_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF__metadata__label_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF__metadata__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1)
        tmp_gridLayout_15.addLayout(tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidget(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_17.addWidget(tmp_DE_Acquisition_Info_file__scrollArea_1, 0, 0, 1, 1)
        tmp_tabWidget_10.addTab(tmp_tab_9, "")
        tmp_gridLayout_4.addWidget(tmp_tabWidget_10, 2, 0, 1, 1)
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF__addButton__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__label_1.setObjectName("DE_Acquisition_Info_DEF__label_1")
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__label_1)
        tmp_DE_Acquisition_Info_DEF__addButton_1 = QtWidgets.QPushButton(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__addButton_1.setObjectName("DE_Acquisition_Info_DEF__addButton_1")
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__addButton_1)
        tmp_gridLayout_4.addLayout(tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1, 1, 0, 1, 1)
        tmp_DE_Acquisition_Info__scrollArea_1.setWidget(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_29.addWidget(tmp_DE_Acquisition_Info__scrollArea_1, 0, 0, 1, 1)
        self.DE_Acquisition_Info_Tab_Widget_List[a].addTab(tmp_tab_6,
                                                           "Tab" + str(len(self.DE_Acquisition_Info_List[a]) + 1))

        self.DE_Acquisition_Info_DEF_Tab_Widget_List.append(tmp_tabWidget_10)

        # tabWidget_8: tabWidget_Acquisition
        # tab_6: tab_Acquisition

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
        self.DE_Acquisition_Info_List[a].append(tmp_list)

        tmp_list = list()
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
        self.DE_Acquisition_Info_DEF_List[len(self.DE_Acquisition_Info_DEF_List) - 1].append(tmp_list)

        Big = len(self.DE_AddAll_List) - 1
        Acq = len(self.DE_Acquisition_Info_List[a]) - 1
        #
        tmp_DE_Acquisition_Info_DEF__addButton_1.clicked.connect(
            lambda: self.DE_Acquisition_Info_DEF_AddTab(Big, Acq)
        )

        _translate = QtCore.QCoreApplication.translate

        tmp_DE_Authentication_ID__label_1.setText("수집 id:")
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1.setText("수집자명:")
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1.setText("수집 시간:")

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

    def DE_AddTab(self):
        self.DE_Gather_Info_List.append(list())

        self.DE_Acquisition_Info_List.append(list())

        self.DE_Acquisition_Info_DEF_List.append(list())

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
        tmp_DE_Gather_Info_gather_no__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_no__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_no__label_1 = QtWidgets.QLabel(tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_no__label_1.setObjectName("DE_Gather_Info_gather_no__label_1")
        tmp_DE_Gather_Info_gather_no__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_no__label_1)
        tmp_DE_Gather_Info_gather_no__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_no__lineEdit_1.setObjectName("DE_Gather_Info_gather_no__lineEdit_1")
        tmp_DE_Gather_Info_gather_no__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_no__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_no__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_location__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_location__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_location__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_location__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_location__label_1.setObjectName("DE_Gather_Info_gather_location__label_1")
        tmp_DE_Gather_Info_gather_location__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_location__label_1)
        tmp_DE_Gather_Info_gather_location__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_location__lineEdit_1.setObjectName("DE_Gather_Info_gather_location__lineEdit_1")
        tmp_DE_Gather_Info_gather_location__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_location__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_location__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_person_name__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_person_name__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_name__label_1.setObjectName("DE_Gather_Info_gather_person_name__label_1")
        tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_person_name__label_1)
        tmp_DE_Gather_Info_gather_person_name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_name__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_person_name__lineEdit_1")
        tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_person_name__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_person_name__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_datetime__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_datetime__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_datetime__label_1.setObjectName("DE_Gather_Info_gather_datetime__label_1")
        tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_datetime__label_1)
        tmp_DE_Gather_Info_gather_datetime__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_datetime__lineEdit_1.setObjectName("DE_Gather_Info_gather_datetime__lineEdit_1")
        tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_datetime__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_datetime__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_person_agency__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_person_agency__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_agency__label_1.setObjectName(
            "DE_Gather_Info_gather_person_agency__label_1")
        tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_person_agency__label_1)
        tmp_DE_Gather_Info_gather_person_agency__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_agency__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_person_agency__lineEdit_1")
        tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_person_agency__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_person_agency__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_person_rank__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_person_rank__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_rank__label_1.setObjectName("DE_Gather_Info_gather_person_rank__label_1")
        tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_person_rank__label_1)
        tmp_DE_Gather_Info_gather_person_rank__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_person_rank__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_person_rank__lineEdit_1")
        tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_person_rank__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_person_rank__horizontalLayout_1)
        tmp_DE_Gather_Info_organization_code__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_organization_code__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_organization_code__horizontalLayout_1")
        tmp_DE_Gather_Info_organization_code__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_organization_code__label_1.setObjectName("DE_Gather_Info_organization_code__label_1")
        tmp_DE_Gather_Info_organization_code__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_organization_code__label_1)
        tmp_DE_Gather_Info_organization_code__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_organization_code__lineEdit_1.setObjectName(
            "DE_Gather_Info_organization_code__lineEdit_1")
        tmp_DE_Gather_Info_organization_code__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_organization_code__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_organization_code__horizontalLayout_1)
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_submitter_name__horizontalLayout_1")
        tmp_DE_Gather_Info_submitter_name__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_submitter_name__label_1.setObjectName("DE_Gather_Info_submitter_name__label_1")
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_submitter_name__label_1)
        tmp_DE_Gather_Info_submitter_name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_submitter_name__lineEdit_1.setObjectName("DE_Gather_Info_submitter_name__lineEdit_1")
        tmp_DE_Gather_Info_submitter_name__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_submitter_name__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Info_submitter_name__horizontalLayout_1)
        tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1.setObjectName(
            "DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1")
        tmp_DE_Gather_Inf_Gather_Source_Name__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Inf_Gather_Source_Name__label_1.setObjectName("DE_Gather_Inf_Gather_Source_Name__label_1")
        tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Inf_Gather_Source_Name__label_1)
        tmp_DE_Gather_Inf_Gather_Source_Name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Inf_Gather_Source_Name__lineEdit_1.setObjectName(
            "DE_Gather_Inf_Gather_Source_Name__lineEdit_1")
        tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Inf_Gather_Source_Name__lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(tmp_DE_Gather_Inf_Gather_Source_Name__horizontalLayout_1)
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1.setObjectName(
            "DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1")
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1.setObjectName(
            "DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1")
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1.addWidget(
            tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___label_1)
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1.setObjectName(
            "DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1")
        tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1.addWidget(
            tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___lineEdit_1)
        tmp_DE_Gather_Info__verticalLayout_1.addLayout(
            tmp_DE_Gather_Inf_Gather_Relation_Person_Type_Code___horizontalLayout_1)
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
        tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1.setObjectName(
            "DE_Gather_Info_file__scrollAreaWidgetContents_1")
        tmp_gridLayout_18 = QtWidgets.QGridLayout(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_gridLayout_18.setObjectName("gridLayout_18")
        tmp_DE_Gather_Info_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Gather_Info_file__verticalLayout_1.setObjectName("DE_Gather_Info_file__verticalLayout_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__horizontalLayout_1")
        tmp_DE_Gather_Info_file__filebrowse__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__label_1.setObjectName("DE_Gather_Info_file__filebrowse__label_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__label_1)
        tmp_DE_Gather_Info_file__filebrowse__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__lineEdit_1.setObjectName("DE_Gather_Info_file__filebrowse__lineEdit_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1 = QtWidgets.QPushButton(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__browseButton_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__browseButton_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__browseButton_1)
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1 = QtWidgets.QPushButton(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__filebrowse__enterButton_1.setObjectName(
            "DE_Gather_Info_file__filebrowse__enterButton_1")
        tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_file__filebrowse__enterButton_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_file__filebrowse__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_media_type__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_media_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_media_type__label_1.setObjectName("DE_Gather_Info_gather_media_type__label_1")
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_media_type__label_1)
        tmp_DE_Gather_Info_gather_media_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_media_type__lineEdit_1.setObjectName(
            "DE_Gather_Info_gather_media_type__lineEdit_1")
        tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(
            tmp_DE_Gather_Info_gather_media_type__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_hash_type__horizontalLayout_1")
        tmp_DE_Gather_Info__gather_hash_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__gather_hash_type__label_1.setObjectName("DE_Gather_Info__gather_hash_type__label_1")
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info__gather_hash_type__label_1)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info__gather_hash_type__lineEdit_1.setObjectName(
            "DE_Gather_Info__gather_hash_type__lineEdit_1")
        tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_hash_type__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_hash__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_hash__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_hash__label_1.setObjectName("DE_Gather_Info_gather_hash__label_1")
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_hash__label_1)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_hash__lineEdit_1.setObjectName("DE_Gather_Info_gather_hash__lineEdit_1")
        tmp_DE_Gather_Info_gather_hash__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_hash__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_path__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_path__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_path__label_1.setObjectName("DE_Gather_Info_gather_path__label_1")
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_path__label_1)
        tmp_DE_Gather_Info_gather_path__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_path__lineEdit_1.setObjectName("DE_Gather_Info_gather_path__lineEdit_1")
        tmp_DE_Gather_Info_gather_path__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_path__horizontalLayout_1)
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_gather_metadata__horizontalLayout_1")
        tmp_DE_Gather_Info_gather_metadata__label_1 = QtWidgets.QLabel(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_metadata__label_1.setObjectName("DE_Gather_Info_gather_metadata__label_1")
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_metadata__label_1)
        tmp_DE_Gather_Info_gather_metadata__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_gather_metadata__lineEdit_1.setObjectName("DE_Gather_Info_gather_metadata__lineEdit_1")
        tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1.addWidget(
            tmp_DE_Gather_Info_gather_metadata__lineEdit_1)
        tmp_DE_Gather_Info_file__verticalLayout_1.addLayout(tmp_DE_Gather_Info_gather_metadata__horizontalLayout_1)
        tmp_gridLayout_18.addLayout(tmp_DE_Gather_Info_file__verticalLayout_1, 1, 0, 1, 1)
        tmp_DE_Gather_Info_file__scrollArea_1.setWidget(tmp_DE_Gather_Info_file__scrollAreaWidgetContents_1)
        tmp_DE_Gather_Info_file__horizontalLayout_1.addWidget(tmp_DE_Gather_Info_file__scrollArea_1)
        tmp_gridLayout_27.addLayout(tmp_DE_Gather_Info_file__horizontalLayout_1, 0, 0, 1, 1)
        tmp_tabWidget_9.addTab(tmp_tab_8, "")
        tmp_gridLayout_3.addWidget(tmp_tabWidget_9, 2, 0, 1, 1)
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Gather_Info_file_addButton__horizontalLayout_1.setObjectName(
            "DE_Gather_Info_file_addButton__horizontalLayout_1")
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
        tmp_DE_Veseel_Info_vessel_name__horizontalLayout_1.setObjectName(
            "DE_Veseel_Info_vessel_name__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_name__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_name__label_1.setObjectName("DE_Vessel_Info_vessel_name__label_1")
        tmp_DE_Veseel_Info_vessel_name__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_name__label_1)
        tmp_DE_Vessel_Info_vessel_name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_name__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_name__lineEdit_1")
        tmp_DE_Veseel_Info_vessel_name__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_name__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Veseel_Info_vessel_name__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_management_id__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_management_id__label_1 = QtWidgets.QLabel(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_management_id__label_1.setObjectName(
            "DE_Vessel_Info_vessel_management_id__label_1")
        tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Vessel_Info_vessel_management_id__label_1)
        tmp_DE_Vessel_Info_vessel_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_management_id__lineEdit_1.setObjectName(
            "DE_Vessel_Info_vessel_management_id__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Vessel_Info_vessel_management_id__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_management_id__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_MMSI__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_MMSI__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_MMSI__label_1.setObjectName("DE_Vessel_Info_vessel_MMSI__label_1")
        tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_MMSI__label_1)
        tmp_DE_Vessel_Info_vessel_MMSI__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_MMSI__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_MMSI__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_MMSI__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_MMSI__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_callsign__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_callsign__label_1 = QtWidgets.QLabel(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_callsign__label_1.setObjectName("DE_Vessel_Info_vessel_callsign__label_1")
        tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1.addWidget(
            tmp_DE_Vessel_Info_vessel_callsign__label_1)
        tmp_DE_Vessel_Info_vessel_callsign__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_callsign__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_callsign__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1.addWidget(
            tmp_DE_Vessel_Info_vessel_callsign__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_callsign__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_IMO__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_IMO__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_IMO__label_1.setObjectName("DE_Vessel_Info_vessel_IMO__label_1")
        tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_IMO__label_1)
        tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1.setPlaceholderText("")
        tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_IMO__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_IMO__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_IMO__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_MRN__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_MRN__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_MRN__label_1.setObjectName("DE_Vessel_Info_vessel_MRN__label_1")
        tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_MRN__label_1)
        tmp_DE_Vessel_Info_vessel_MRN__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_MRN__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_MRN__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_MRN__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_MRN__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_tonnage__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_tonnage__label_1 = QtWidgets.QLabel(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_tonnage__label_1.setObjectName("DE_Vessel_Info_vessel_tonnage__label_1")
        tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_tonnage__label_1)
        tmp_DE_Vessel_Info_vessel_tonnage__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_tonnage__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_tonnage__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1.addWidget(
            tmp_DE_Vessel_Info_vessel_tonnage__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_tonnage__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_length__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_length__label_1 = QtWidgets.QLabel(tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_length__label_1.setObjectName("DE_Vessel_Info_vessel_length__label_1")
        tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_length__label_1)
        tmp_DE_Vessel_Info_vessel_length__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_length__lineEdit_1.setObjectName("DE_Vessel_Info_vessel_length__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1.addWidget(tmp_DE_Vessel_Info_vessel_length__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(tmp_DE_Vessel_Info_vessel_length__horizontalLayout_1)
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.setObjectName(
            "DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1")
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1 = QtWidgets.QLabel(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1.setObjectName(
            "DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1")
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.addWidget(
            tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1)
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Vessel_Info__scrollAreaWidgetContents_1)
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1.setObjectName(
            "DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1")
        tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1.addWidget(
            tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__lineEdit_1)
        tmp_DE_Vessel_Info__verticalLayout_1.addLayout(
            tmp_DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__horizontalLayout_1)
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
        tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1.setObjectName(
            "DE_Marines_Electronics_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_6 = QtWidgets.QGridLayout(tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_6.setObjectName("gridLayout_6")
        tmp_DE_Marines_Electronics_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info__verticalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_management_id__label_1 = QtWidgets.QLabel(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_management_id__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_management_id__label_1")
        tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_management_id__label_1)
        tmp_DE_Marines_Electronics_Info_device_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_management_id__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_management_id__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_management_id__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            tmp_DE_Marines_Electronics_Info_device_management_id__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_type__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_type__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_type__label_1")
        tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_type__label_1)
        tmp_DE_Marines_Electronics_Info_device_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_type__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_type__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_type__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            tmp_DE_Marines_Electronics_Info_device_type__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_manufacturer__label_1 = QtWidgets.QLabel(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_manufacturer__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_manufacturer__label_1")
        tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_manufacturer__label_1)
        tmp_DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_manufacturer__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            tmp_DE_Marines_Electronics_Info_device_manufacturer__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_model_name__label_1 = QtWidgets.QLabel(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_model_name__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_name__label_1")
        tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_model_name__label_1)
        tmp_DE_Marines_Electronics_Info_device_model_name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_model_name__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_name__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_model_name__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            tmp_DE_Marines_Electronics_Info_device_model_name__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__label_1 = QtWidgets.QLabel(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_serial_number__label_1")
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_model_serial_number__label_1)
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_model_serial_number__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            tmp_DE_Marines_Electronics_Info_device_model_serial_number__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_os_firmware__label_1 = QtWidgets.QLabel(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_os_firmware__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_os_firmware__label_1")
        tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_os_firmware__label_1)
        tmp_DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_os_firmware__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            tmp_DE_Marines_Electronics_Info_device_os_firmware__horizontalLayout_1)
        tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1.setObjectName(
            "DE_Marines_Electronics_Info_device_description__horizontalLayout_1")
        tmp_DE_Marines_Electronics_Info_device_description__label_1 = QtWidgets.QLabel(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_description__label_1.setObjectName(
            "DE_Marines_Electronics_Info_device_description__label_1")
        tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_description__label_1)
        tmp_DE_Marines_Electronics_Info_device_description__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_DE_Marines_Electronics_Info_device_description__lineEdit_1.setObjectName(
            "DE_Marines_Electronics_Info_device_description__lineEdit_1")
        tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1.addWidget(
            tmp_DE_Marines_Electronics_Info_device_description__lineEdit_1)
        tmp_DE_Marines_Electronics_Info__verticalLayout_1.addLayout(
            tmp_DE_Marines_Electronics_Info_device_description__horizontalLayout_1)
        tmp_gridLayout_6.addLayout(tmp_DE_Marines_Electronics_Info__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Marines_Electronics_Info__scrollArea_1.setWidget(
            tmp_DE_Marines_Electronics_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_7.addWidget(tmp_DE_Marines_Electronics_Info__scrollArea_1, 1, 2, 1, 1)
        tmp_DE_Marine_Electronics_Info__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Marine_Electronics_Info__horizontalLayout_1.setObjectName(
            "DE_Marine_Electronics_Info__horizontalLayout_1")
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
        tmp_DE_other_files_file_browse__horizontalLayout_1.setObjectName(
            "DE_other_files_file_browse__horizontalLayout_1")
        tmp_DE_other_files_file_browse__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__label_1.setObjectName("DE_other_files_file_browse__label_1")
        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__label_1)
        tmp_DE_other_files_file_browse__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__lineEdit_1.setObjectName("DE_other_files_file_browse__lineEdit_1")
        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__lineEdit_1)
        tmp_DE_other_files_file_browse__browseButton_1 = QtWidgets.QPushButton(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_browse__browseButton_1.setObjectName("DE_other_files_file_browse__browseButton_1")
        tmp_DE_other_files_file_browse__horizontalLayout_1.addWidget(tmp_DE_other_files_file_browse__browseButton_1)
        tmp_DE_other_files_file_browse__EnterButton_1 = QtWidgets.QPushButton(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
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
        tmp_DE_other_files_file_size__horizontalLayout_1.setObjectName(
            "DE_other_files_file_size__horizontalLayout_1")
        tmp_DE_other_files_file_size__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_size__label_1.setObjectName("DE_other_files_file_size__label_1")
        tmp_DE_other_files_file_size__horizontalLayout_1.addWidget(tmp_DE_other_files_file_size__label_1)
        tmp_DE_other_files_file_size__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_size__lineEdit_1.setObjectName("DE_other_files_file_size__lineEdit_1")
        tmp_DE_other_files_file_size__horizontalLayout_1.addWidget(tmp_DE_other_files_file_size__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_size__horizontalLayout_1)
        tmp_DE_other_files_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_path__horizontalLayout_1.setObjectName(
            "DE_other_files_file_path__horizontalLayout_1")
        tmp_DE_other_files_file_path__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_path__label_1.setObjectName("DE_other_files_file_path__label_1")
        tmp_DE_other_files_file_path__horizontalLayout_1.addWidget(tmp_DE_other_files_file_path__label_1)
        tmp_DE_other_files_file_path__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_path__lineEdit_1.setObjectName("DE_other_files_file_path__lineEdit_1")
        tmp_DE_other_files_file_path__horizontalLayout_1.addWidget(tmp_DE_other_files_file_path__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_path__horizontalLayout_1)
        tmp_DE_other_files_file_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_hash_type__horizontalLayout_1.setObjectName(
            "DE_other_files_file_hash_type__horizontalLayout_1")
        tmp_DE_other_files_file_hash_type__label_1 = QtWidgets.QLabel(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_type__label_1.setObjectName("DE_other_files_file_hash_type__label_1")
        tmp_DE_other_files_file_hash_type__horizontalLayout_1.addWidget(tmp_DE_other_files_file_hash_type__label_1)
        tmp_DE_other_files_file_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_type__lineEdit_1.setObjectName("DE_other_files_file_hash_type__lineEdit_1")
        tmp_DE_other_files_file_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_other_files_file_hash_type__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_hash_type__horizontalLayout_1)
        tmp_DE_other_files_file_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_hash_value__horizontalLayout_1.setObjectName(
            "DE_other_files_file_hash_value__horizontalLayout_1")
        tmp_DE_other_files_file_hash_value__label_1 = QtWidgets.QLabel(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_value__label_1.setObjectName("DE_other_files_file_hash_value__label_1")
        tmp_DE_other_files_file_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_other_files_file_hash_value__label_1)
        tmp_DE_other_files_file_hash_value__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_hash_value__lineEdit_1.setObjectName("DE_other_files_file_hash_value__lineEdit_1")
        tmp_DE_other_files_file_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_other_files_file_hash_value__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_hash_value__horizontalLayout_1)
        tmp_DE_other_files_file_description__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_description__horizontalLayout_1.setObjectName(
            "DE_other_files_file_description__horizontalLayout_1")
        tmp_DE_other_files_file_description__label_1 = QtWidgets.QLabel(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_description__label_1.setObjectName("DE_other_files_file_description__label_1")
        tmp_DE_other_files_file_description__horizontalLayout_1.addWidget(
            tmp_DE_other_files_file_description__label_1)
        tmp_DE_other_files_file_description__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_description__lineEdit_1.setObjectName("DE_other_files_file_description__lineEdit_1")
        tmp_DE_other_files_file_description__horizontalLayout_1.addWidget(
            tmp_DE_other_files_file_description__lineEdit_1)
        tmp_DE_other_files__verticalLayout_1.addLayout(tmp_DE_other_files_file_description__horizontalLayout_1)
        tmp_DE_other_files_file_metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_other_files_file_metadata__horizontalLayout_1.setObjectName(
            "DE_other_files_file_metadata__horizontalLayout_1")
        tmp_DE_other_files_file_metadata__label_1 = QtWidgets.QLabel(tmp_DE_other_files__scrollAreaWidgetContents_1)
        tmp_DE_other_files_file_metadata__label_1.setObjectName("DE_other_files_file_metadata__label_1")
        tmp_DE_other_files_file_metadata__horizontalLayout_1.addWidget(tmp_DE_other_files_file_metadata__label_1)
        tmp_DE_other_files_file_metadata__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_other_files__scrollAreaWidgetContents_1)
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
        tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1.setObjectName(
            "DE_Acquisition_Info__scrollAreaWidgetContents_1")
        tmp_gridLayout_4 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_4.setObjectName("gridLayout_4")
        tmp_DE_Acquisition_Info__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__verticalLayout_1.setObjectName("DE_Acquisition_Info__verticalLayout_1")
        tmp_DE_Authentication_ID__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Authentication_ID__horizontalLayout_1.setObjectName("DE_Authentication_ID__horizontalLayout_1")
        tmp_DE_Authentication_ID__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_ID__label_1.setObjectName("DE_Authentication_ID__label_1")
        tmp_DE_Authentication_ID__horizontalLayout_1.addWidget(tmp_DE_Authentication_ID__label_1)
        tmp_DE_Authentication_ID__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_ID__lineEdit_1.setObjectName("DE_Authentication_ID__lineEdit_1")
        tmp_DE_Authentication_ID__horizontalLayout_1.addWidget(tmp_DE_Authentication_ID__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(tmp_DE_Authentication_ID__horizontalLayout_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_person_name__label_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_person_name__label_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_person_name__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_acquisition_person_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_date_time__label_1")
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_date_time__label_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_date_time__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_acquisition_date_time__horizontalLayout_1)
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.setObjectName(
            "DE_Acquisiton_Info_acquisition_location__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_location__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_location__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_location__label_1")
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_location__label_1)
        tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_location__lineEdit_1")
        tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisiton_Info_acquisition_location__horizontalLayout_1)
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_tool__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool__label_1")
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_tool__label_1)
        tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_acquisition_tool__horizontalLayout_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__label_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool_version__label_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_tool_version__label_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_acquisition_tool_version__lineEdit_1")
        tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_acquisition_tool_version__horizontalLayout_1)
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.setObjectName(
            "DE_Authentication_Person_Party_Name__horizontalLayout_1")
        tmp_DE_Authentication_Person_Party_Name__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_Person_Party_Name__label_1.setObjectName(
            "DE_Authentication_Person_Party_Name__label_1")
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(
            tmp_DE_Authentication_Person_Party_Name__label_1)
        tmp_DE_Authentication_Person_Party_Name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Authentication_Person_Party_Name__lineEdit_1.setObjectName(
            "DE_Authentication_Person_Party_Name__lineEdit_1")
        tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1.addWidget(
            tmp_DE_Authentication_Person_Party_Name__lineEdit_1)
        tmp_DE_Acquisition_Info__verticalLayout_1.addLayout(
            tmp_DE_Authentication_Person_Party_Name__horizontalLayout_1)
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
        tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1.setObjectName(
            "DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1")
        tmp_gridLayout_15 = QtWidgets.QGridLayout(tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_15.setObjectName("gridLayout_15")
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1 = QtWidgets.QVBoxLayout()
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.setObjectName(
            "DE_Acquisition_Info__DEF_file__verticalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__label_1.setObjectName("DE_Acquisition_Info_DEF_serial_no__label_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_serial_no__label_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_serial_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_serial_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_management_id__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__label_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_management_id__label_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_management_id__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_management_id__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_type__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__label_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__label_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__label_1.setObjectName("DE_Acquisition_Info_DEF_gather_no__label_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_gather_no__label_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_gather_no__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_gather_no__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_browse__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setMaximumSize(QtCore.QSize(16777215, 16500000))
        tmp_DE_Acquisition_Info_DEF_browse__label_1.setObjectName("DE_Acquisition_Info_DEF_browse__label_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__label_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1.setObjectName("DE_Acquisition_Info_DEF_browse__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1 = QtWidgets.QPushButton(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__browseButton_1.setObjectName(
            "DE_Acquisition_Info_DEF_browse__browseButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__browseButton_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1 = QtWidgets.QPushButton(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_browse__enterButton_1.setObjectName(
            "DE_Acquisition_Info_DEF_browse__enterButton_1")
        tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_browse__enterButton_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_file_browse_horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_type__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_type__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_type__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_hash_type__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__label_1.setObjectName("DE_Acquisition_Info_DEF_hash_value__label_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_value__label_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_hash_value__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_hash_value__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__label_1.setObjectName(
            "DE_Acquisition_Info_DEF_sector_size__label_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_sector_size__label_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_sector_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_sector_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_size__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF_file_size__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__label_1.setObjectName("DE_Acquisition_Info_DEF_file_size__label_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_file_size__label_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF_file_size__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF_file_size__horizontalLayout_1)
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF__metadata__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__metadata__label_1 = QtWidgets.QLabel(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__label_1.setObjectName("DE_Acquisition_Info_DEF__metadata__label_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF__metadata__label_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1 = QtWidgets.QLineEdit(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1.setObjectName(
            "DE_Acquisition_Info_DEF__metadata__lineEdit_1")
        tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)
        tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1.addLayout(
            tmp_DE_Acquisition_Info_DEF__metadata__horizontalLayout_1)
        tmp_gridLayout_15.addLayout(tmp_DE_Acquisition_Info__DEF_file__verticalLayout_1, 0, 0, 1, 1)
        tmp_DE_Acquisition_Info_file__scrollArea_1.setWidget(
            tmp_DE_Acquisition_Info_DEF__scrollAreaWidgetContents_1)
        tmp_gridLayout_17.addWidget(tmp_DE_Acquisition_Info_file__scrollArea_1, 0, 0, 1, 1)
        tmp_tabWidget_10.addTab(tmp_tab_9, "")
        tmp_gridLayout_4.addWidget(tmp_tabWidget_10, 2, 0, 1, 1)
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1 = QtWidgets.QHBoxLayout()
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.setObjectName(
            "DE_Acquisition_Info_DEF__addButton__horizontalLayout_1")
        tmp_DE_Acquisition_Info_DEF__label_1 = QtWidgets.QLabel(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__label_1.setObjectName("DE_Acquisition_Info_DEF__label_1")
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(tmp_DE_Acquisition_Info_DEF__label_1)
        tmp_DE_Acquisition_Info_DEF__addButton_1 = QtWidgets.QPushButton(
            tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_DE_Acquisition_Info_DEF__addButton_1.setObjectName("DE_Acquisition_Info_DEF__addButton_1")
        tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1.addWidget(
            tmp_DE_Acquisition_Info_DEF__addButton_1)
        tmp_gridLayout_4.addLayout(tmp_DE_Acquisition_Info_DEF__addButton__horizontalLayout_1, 1, 0, 1, 1)
        tmp_DE_Acquisition_Info__scrollArea_1.setWidget(tmp_DE_Acquisition_Info__scrollAreaWidgetContents_1)
        tmp_gridLayout_29.addWidget(tmp_DE_Acquisition_Info__scrollArea_1, 0, 0, 1, 1)
        tmp_tabWidget_8.addTab(tmp_tab_6, "")
        tmp_gridLayout_7.addWidget(tmp_tabWidget_8, 1, 3, 3, 1)
        tmp_DE__scrollArea_1.setWidget(tmp_DE__scrollAreaWidgetContents)
        tmp_gridLayout_26.addWidget(tmp_DE__scrollArea_1, 1, 0, 1, 1)
        self.tabWidget_3.addTab(tmp_tab_2, "Tab" + str(len(self.DE_AddAll_List) + 1))

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

        tmp_list.append(tmp_DE_other_files_file_browse__lineEdit_1)  # 0
        tmp_list.append(tmp_DE_other_files_id__lineEdit_1)  #
        tmp_list.append(tmp_DE_other_files_type__lineEdit_1)  #
        tmp_list.append(tmp_DE_other_files_file_size__lineEdit_1)  #
        tmp_list.append(tmp_DE_other_files_file_path__lineEdit_1)  #
        tmp_list.append(tmp_DE_other_files_file_hash_type__lineEdit_1)  #
        tmp_list.append(tmp_DE_other_files_file_hash_value__lineEdit_1)  #
        tmp_list.append(tmp_DE_other_files_file_description__lineEdit_1)  #
        tmp_list.append(tmp_DE_other_files_file_metadata__lineEdit_1)

        # Acquisition_Info
        tmp_list.append(tmp_DE_Authentication_ID__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_person_name__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_date_time__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_location__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_tool__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_acquisition_tool_version__lineEdit_1)  #
        tmp_list.append(tmp_DE_Authentication_Person_Party_Name__lineEdit_1)

        # DEF Acquisition 추가
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_serial_no__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_management_id__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_type__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_evidences_gathering_type__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_gather_no__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_browse__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_name__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_digital_evidence_file_path__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_type__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_hash_value__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_sector_size__lineEdit_1)  #
        tmp_list.append(tmp_DE_Acquisition_Info_DEF_file_size__lineEdit_1)
        tmp_list.append(tmp_DE_Acquisition_Info_DEF__metadata__lineEdit_1)  #
        self.DE_AddAll_List.append(tmp_list)

        tmp_list = list()
        tmp_list.append(tmp_DE_Gather_Info_file__filebrowse__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_media_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info__gather_hash_type__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_hash__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_path__lineEdit_1)
        tmp_list.append(tmp_DE_Gather_Info_gather_metadata__lineEdit_1)
        self.DE_Gather_Info_List[len(self.DE_Gather_Info_List) - 1].append(tmp_list)

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
        self.DE_Acquisition_Info_List[len(self.DE_Acquisition_Info_List) - 1].append(tmp_list)

        self.DE_Gather_Info_List[len(self.DE_Gather_Info_List) - 1].append(tmp_list)

        self.DE_Gather_Info_Tab_Widget_List.append(tmp_tabWidget_9)

        self.DE_Acquisition_Info_Tab_Widget_List.append(tmp_tabWidget_8)

        tmp_len = len(self.DE_Gather_Info_List) - 1

        tmp_DE_Gather_Info__addButton_1.clicked.connect(lambda: self.DE_Gather_Info_AddTab(tmp_len))

        #
        tmp_len2 = len(self.DE_Acquisition_Info_List) - 1
        tmp_DE_Acquisition_Info__addButton_1.clicked.connect(lambda: self.DE_Acquisition_Info_AddTab(tmp_len2))

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

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.Digital_Evidence_Package.setText(_translate("SecondWindow", "Digital Evidence Package"))
        self.DE__addButton.setText(_translate("SecondWindow", "+추가"))
        self.DE_Digitlal_Evidence__label.setText(_translate("SecondWindow", "디지털 증거"))
        self.DE_Gather_Info_gather_no__label_1.setText(_translate("SecondWindow", "채증 번호: "))
        self.DE_Gather_Info_gather_location__label_1.setText(_translate("SecondWindow", "채증 장소:"))
        self.DE_Gather_Info_gather_person_name__label_1.setText(_translate("SecondWindow", "채증 담당자:"))
        self.DE_Gather_Info_gather_datetime__label_1.setText(_translate("SecondWindow", "채증 시간:"))
        self.DE_Gather_Info_gather_datetime__lineEdit_1.setPlaceholderText(
            _translate("SecondWindow", "ex) 2021-11-30 19:58:13.829475+09:00"))
        self.DE_Gather_Info_gather_person_agency__label_1.setText(_translate("SecondWindow", "채증 기관:"))
        self.DE_Gather_Info_gather_person_rank__label_1.setText(_translate("SecondWindow", "채증 담당자 계급:"))
        self.DE_Gather_Info_organization_code__label_1.setText(_translate("SecondWindow", "소속 조직 코드: "))
        self.DE_Gather_Info_submitter_name__label_1.setText(_translate("SecondWindow", "피압수자:"))
        self.DE_Gather_Info_Gather_Source_Name__label_1.setText(_translate("SecondWindow", "정보 저장 매체명: "))
        self.DE_Gather_Info_Gather_Relation_Person_Type_Code___label_1.setText(
            _translate("SecondWindow", "수집 대상자 유형: "))
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
        self.DE_Gather_Info__addButton_1.setText(_translate("SecondWindow", "+"))
        self.DE_Vessel_Info__label_1.setText(_translate("SecondWindow", "   선박 정보"))
        self.DE_Vessel_Info_vessel_name__label_1.setText(_translate("SecondWindow", "선박 이름:"))
        self.DE_Vessel_Info_vessel_management_id__label_1.setText(_translate("SecondWindow", "선박 관리 고유 번호:"))
        self.DE_Vessel_Info_vessel_MMSI__label_1.setText(_translate("SecondWindow", "선박 MMSI:"))
        self.DE_Vessel_Info_vessel_callsign__label_1.setText(_translate("SecondWindow", "선박 callsign:"))
        self.DE_Vessel_Info_vessel_IMO__label_1.setText(_translate("SecondWindow", "선박 IMO:"))
        self.DE_Vessel_Info_vessel_MRN__label_1.setText(_translate("SecondWindow", "선박 MRN:"))
        self.DE_Vessel_Info_vessel_tonnage__label_1.setText(_translate("SecondWindow", "선박 톤수:"))
        self.DE_Vessel_Info_vessel_length__label_1.setText(_translate("SecondWindow", "선박 길이:"))
        self.DE_Vessel_Info_vessel_total_number_of_equipmentwith_track__label_1.setText(
            _translate("SecondWindow", "항적 분석 장비 수:"))
        self.DE_Vessel_Type__label_1.setText(_translate("SecondWindow", "선박 유형: "))
        self.DE_Marines_Electronics_Info_device_management_id__label_1.setText(
            _translate("SecondWindow", "장비 관리 고유 번호:"))
        self.DE_Marines_Electronics_Info_device_type__label_1.setText(_translate("SecondWindow", "장비 유형:"))
        self.DE_Marines_Electronics_Info_device_manufacturer__label_1.setText(_translate("SecondWindow", "장비 제조사:"))
        self.DE_Marines_Electronics_Info_device_model_name__label_1.setText(_translate("SecondWindow", "장비 모델명:"))
        self.DE_Marines_Electronics_Info_device_model_serial_number__label_1.setText(
            _translate("SecondWindow", "장비 모델 시리얼 넘버:"))
        self.DE_Marines_Electronics_Info_device_os_firmware__label_1.setText(
            _translate("SecondWindow", "장비 os firmware:"))
        self.DE_Marines_Electronics_Info_device_description__label_1.setText(_translate("SecondWindow", "장비 설명:"))
        self.DE_Marine_Electronics_Info__label_1.setText(_translate("SecondWindow", "   해양 장비 정보"))
        self.DE_Gather_Info__label_1.setText(_translate("SecondWindow", " 채증 정보"))
        self.DE_other_files__label_1.setText(_translate("SecondWindow", "기타 파일(jpg, mp4, txt, bin 등)"))
        self.DE_other_files__addButton_1.setText(_translate("SecondWindow", "+"))
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
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_4), _translate("SecondWindow", "Tab 1"))
        self.DE_Acquisition_Info__label_1.setText(_translate("SecondWindow", " 수집 정보"))
        self.DE_Acquisition_Info__addButton_1.setText(_translate("SecondWindow", "+추가"))
        self.DE_Authentication_ID__label_1.setText(_translate("SecondWindow", "수집 id"))
        self.DE_Acquisition_Info_acquisition_person_name__label_1.setText(_translate("SecondWindow", "수집자명:"))
        self.DE_Acquisition_Info_acquisition_date_time__label_1.setText(_translate("SecondWindow", "수집 시간:"))
        self.DE_Acquisition_Info_acquisition_date_time__lineEdit_1.setPlaceholderText(
            _translate("SecondWindow", "ex) 2021-11-30 19:58:13.829475+09:00"))
        self.DE_Acquisition_Info_acquisition_location__label_1.setText(_translate("SecondWindow", "수집 장소:"))
        self.DE_Acquisition_Info_acquisition_tool__label_1.setText(_translate("SecondWindow", "수집 도구:"))
        self.DE_Acquisition_Info_acquisition_tool_version__label_1.setText(_translate("SecondWindow", "수집 도구 버젼:"))
        self.DE_Authentication_Person_Party_Name__label_1.setText(_translate("SecondWindow", "수집 부서: "))
        self.DE_Acquisition_Info_DEF_serial_no__label_1.setText(_translate("SecondWindow", "일련 번호: "))
        self.DE_Acquisition_Info_DEF_management_id__label_1.setText(_translate("SecondWindow", "관리 번호:"))
        self.DE_Acquisition_Info_DEF_digital_evidence_type__label_1.setText(_translate("SecondWindow", "디지털 증거 유형:"))
        self.DE_Acquisition_Info_DEF_evidences_gathering_type__label_1.setText(_translate("SecondWindow", "증거 채증 유형:"))
        self.DE_Acquisition_Info_DEF_gather_no__label_1.setText(_translate("SecondWindow", "채증 번호"))
        self.DE_Acquisition_Info_DEF_browse__label_1.setText(_translate("SecondWindow", "파일입력:"))
        self.DE_Acquisition_Info_DEF_browse__browseButton_1.setText(_translate("SecondWindow", "Browse..."))
        self.DE_Acquisition_Info_DEF_browse__enterButton_1.setText(_translate("SecondWindow", "Enter"))
        self.DE_Acquisition_Info_DEF_digital_evidence_file_name__label_1.setText(
            _translate("SecondWindow", "디지털 증거 파일 이름:"))
        self.DE_Acquisition_Info_DEF_digital_evidence_file_path__label_1.setText(
            _translate("SecondWindow", "디지털 증거 파일 경로:"))
        self.DE_Acquisition_Info_DEF_hash_type__label_1.setText(_translate("SecondWindow", "해시 종류:"))
        self.DE_Acquisition_Info_DEF_hash_value__label_1.setText(_translate("SecondWindow", "해시값:"))
        self.DE_Acquisition_Info_DEF_sector_size__label_1.setText(_translate("SecondWindow", "섹터 크기: "))
        self.DE_Acquisition_Info_DEF_file_size__label_1.setText(_translate("SecondWindow", "파일 크기: "))
        self.DE_Acquisition_Info_DEF__metadata__label_1.setText(_translate("SecondWindow", "파일 메타데이터: "))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_9), _translate("SecondWindow", "Tab 1"))
        self.DE_Acquisition_Info_DEF__label_1.setText(_translate("SecondWindow", "디지털 증거 파일"))
        self.DE_Acquisition_Info_DEF__addButton_1.setText(_translate("SecondWindow", "+"))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_6), _translate("SecondWindow", "Tab 1"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), _translate("SecondWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DE_tab), _translate("SecondWindow", "Digital Evidences"))
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

#아직 완벽하진 않지만 많은 발전을 했음