from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QVBoxLayout

from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QWidget
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QTabWidget
import sys,res
import  mysql.connector as mc


class Ui_Form(object):

    # Ajoutez cette fonction
    def load(self):
        # Appelez la fonction display_data pour afficher les données dans le tableau
        self.display_data()
        # Connexion à la base de données MySQL (remplacez ces informations par les vôtres)
        self.conn = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='qt5'
        )
        self.cur = self.conn.cursor()
        # Afficher tous les éléments au démarrage
        #self.afficher_tous_elements()
        # Connectez le signal itemSelectionChanged à la fonction update_lineedits
        self.Tableau_nouvelle_Eglise.itemSelectionChanged.connect(self.update_lineedits)
        self.Text_Recherche_Nouvelle_Eglise.textChanged.connect(self.rechercher)


    # Ajoutez cette fonction pour activer la sélection d'une ligne entière
    def enable_row_selection(self):
            self.Tableau_nouvelle_Eglise.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.Tableau_nouvelle_Eglise.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1222, 671)
        Form.setMaximumSize(QtCore.QSize(1222, 671))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(1, 1))
        self.tabWidget.setMaximumSize(QtCore.QSize(1226, 671))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 255), stop:0.5 rgba(0, 200, 255, 255), stop:1 rgba(0, 191, 255, 205));\n"
"background-size:auto;")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(-60, 0, 1311, 651))
        self.label.setStyleSheet("background-image: url(:/images/fond_trois.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(-30, 0, 1311, 651))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 20);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(-10, -10, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_12.setText("")
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.Text_nom_eglise = QtWidgets.QLineEdit(self.tab_2)
        self.Text_nom_eglise.setGeometry(QtCore.QRect(260, 80, 221, 31))
        self.Text_nom_eglise.setStyleSheet("background-color:#ffffff;")
        self.Text_nom_eglise.setObjectName("Text_nom_eglise")
        self.Text_Adresse_eglise = QtWidgets.QLineEdit(self.tab_2)
        self.Text_Adresse_eglise.setGeometry(QtCore.QRect(260, 140, 221, 31))
        self.Text_Adresse_eglise.setStyleSheet("background-color:#ffffff;")
        self.Text_Adresse_eglise.setObjectName("Text_Adresse_eglise")
        self.Text_mes_terrain_eglise = QtWidgets.QLineEdit(self.tab_2)
        self.Text_mes_terrain_eglise.setGeometry(QtCore.QRect(260, 330, 221, 31))
        self.Text_mes_terrain_eglise.setStyleSheet("background-color:#ffffff;")
        self.Text_mes_terrain_eglise.setObjectName("Text_mes_terrain_eglise")
        self.Text_mes_eglise = QtWidgets.QLineEdit(self.tab_2)
        self.Text_mes_eglise.setGeometry(QtCore.QRect(260, 400, 221, 31))
        self.Text_mes_eglise.setStyleSheet("background-color:#ffffff;")
        self.Text_mes_eglise.setObjectName("Text_mes_eglise")
        self.date_ouverture_eglise = QtWidgets.QDateEdit(self.tab_2)
        self.date_ouverture_eglise.setGeometry(QtCore.QRect(260, 200, 221, 31))
        self.date_ouverture_eglise.setStyleSheet("background-color:#ffffff;")
        self.date_ouverture_eglise.setObjectName("date_ouverture_eglise")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 80, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(20, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 200, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(20, 260, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_16.setObjectName("label_16")
        self.date_oraganisation_eglise = QtWidgets.QDateEdit(self.tab_2)
        self.date_oraganisation_eglise.setGeometry(QtCore.QRect(260, 260, 221, 31))
        self.date_oraganisation_eglise.setStyleSheet("background-color:#ffffff;")
        self.date_oraganisation_eglise.setObjectName("date_oraganisation_eglise")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(20, 330, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(20, 400, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(20, 460, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_19.setObjectName("label_19")
        self.Text_Reference_terrain = QtWidgets.QLineEdit(self.tab_2)
        self.Text_Reference_terrain.setGeometry(QtCore.QRect(260, 460, 221, 31))
        self.Text_Reference_terrain.setStyleSheet("background-color:#ffffff;")
        self.Text_Reference_terrain.setObjectName("Text_Reference_terrain")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(260, 10, 721, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_20.setObjectName("label_20")
        self.Tableau_nouvelle_Eglise = QtWidgets.QTableWidget(self.tab_2)
        self.Tableau_nouvelle_Eglise.setGeometry(QtCore.QRect(500, 170, 701, 431))
        self.Tableau_nouvelle_Eglise.setStyleSheet("background-color:#ffffff;")
        self.Tableau_nouvelle_Eglise.setColumnCount(8)
        self.Tableau_nouvelle_Eglise.setObjectName("Tableau_nouvelle_Eglise")
        self.Tableau_nouvelle_Eglise.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()

        self.Tableau_nouvelle_Eglise.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableau_nouvelle_Eglise.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableau_nouvelle_Eglise.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableau_nouvelle_Eglise.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableau_nouvelle_Eglise.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableau_nouvelle_Eglise.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableau_nouvelle_Eglise.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableau_nouvelle_Eglise.setHorizontalHeaderItem(7, item)
        self.Tableau_nouvelle_Eglise.horizontalHeader().setDefaultSectionSize(110)
        self.Tableau_nouvelle_Eglise.horizontalHeader().setMinimumSectionSize(50)
        self.Tableau_nouvelle_Eglise.verticalHeader().setDefaultSectionSize(31)
        self.Ajout_nouvelle_Eglise = QtWidgets.QPushButton(self.tab_2)
        self.Ajout_nouvelle_Eglise.setGeometry(QtCore.QRect(20, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Ajout_nouvelle_Eglise.setFont(font)
        self.Ajout_nouvelle_Eglise.setStyleSheet("QPushButton#Ajout_nouvelle_Eglise {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Ajout_nouvelle_Eglise:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Ajout_nouvelle_Eglise:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Ajout_nouvelle_Eglise.setObjectName("Ajout_nouvelle_Eglise")
        self.Ajout_nouvelle_Eglise.clicked.connect(self.insert_date)

        self.Modifier_nouvelle_eglise = QtWidgets.QPushButton(self.tab_2)
        self.Modifier_nouvelle_eglise.setGeometry(QtCore.QRect(180, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Modifier_nouvelle_eglise.setFont(font)
        self.Modifier_nouvelle_eglise.setStyleSheet("QPushButton#Modifier_nouvelle_eglise {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Modifier_nouvelle_eglise:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Modifier_nouvelle_eglise:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Modifier_nouvelle_eglise.setObjectName("Modifier_nouvelle_eglise")
        self.Modifier_nouvelle_eglise.clicked.connect(self.update_data)
        self.Supprimer_nouvelle_eglise = QtWidgets.QPushButton(self.tab_2)
        self.Supprimer_nouvelle_eglise.setGeometry(QtCore.QRect(350, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Supprimer_nouvelle_eglise.setFont(font)
        self.Supprimer_nouvelle_eglise.setStyleSheet("QPushButton#Supprimer_nouvelle_eglise {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Supprimer_nouvelle_eglise:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Supprimer_nouvelle_eglise:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Supprimer_nouvelle_eglise.setObjectName("Supprimer_nouvelle_eglise")
        # Connectez le bouton à la fonction delete_selected_item
        self.Supprimer_nouvelle_eglise.clicked.connect(self.confirm_delete)
        self.Text_Recherche_Nouvelle_Eglise = QtWidgets.QLineEdit(self.tab_2)


        self.Text_Recherche_Nouvelle_Eglise.setGeometry(QtCore.QRect(500, 100, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Text_Recherche_Nouvelle_Eglise.setFont(font)
        self.Text_Recherche_Nouvelle_Eglise.setStyleSheet("background-color:#ffffff;")
        self.Text_Recherche_Nouvelle_Eglise.setObjectName("Text_Recherche_Nouvelle_Eglise")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(-10, 0, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_11.setText("")
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(420, 160, 751, 361))
        self.tableWidget_2.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(31)
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(260, 10, 721, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_21.setObjectName("label_21")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 160, 221, 31))
        self.lineEdit_7.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(960, 110, 191, 41))
        self.comboBox.setStyleSheet("background-color:#ffffff;")
        self.comboBox.setObjectName("comboBox")
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(910, 70, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_22.setObjectName("label_22")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 230, 221, 31))
        self.lineEdit_8.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 300, 221, 31))
        self.lineEdit_9.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(170, 370, 221, 31))
        self.lineEdit_10.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(20, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        self.label_24.setGeometry(QtCore.QRect(20, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(20, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(20, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_26.setObjectName("label_26")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(420, 100, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_5:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_5:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(1030, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton#pushButton_6{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_6:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_6:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(-10, -10, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_10.setText("")
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setGeometry(QtCore.QRect(250, 20, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_27.setObjectName("label_27")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(440, 160, 751, 361))
        self.tableWidget_3.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(31)
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(20, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_28.setObjectName("label_28")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(210, 180, 221, 31))
        self.lineEdit_13.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(440, 90, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 540, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton#pushButton_7 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_7:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_7:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(210, 240, 221, 31))
        self.lineEdit_15.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(210, 310, 221, 31))
        self.lineEdit_16.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(210, 380, 221, 31))
        self.lineEdit_17.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(20, 240, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(20, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab_3)
        self.label_31.setGeometry(QtCore.QRect(20, 380, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_31.setObjectName("label_31")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_20.setGeometry(QtCore.QRect(270, 540, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton#pushButton_20 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_20:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_20:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_21.setGeometry(QtCore.QRect(1050, 540, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton#pushButton_21 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_21:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_21:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_21.setObjectName("pushButton_21")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setGeometry(QtCore.QRect(-10, 0, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_9.setText("")
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.label_32 = QtWidgets.QLabel(self.tab_5)
        self.label_32.setGeometry(QtCore.QRect(250, 10, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_32.setObjectName("label_32")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_18.setGeometry(QtCore.QRect(440, 100, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_33 = QtWidgets.QLabel(self.tab_5)
        self.label_33.setGeometry(QtCore.QRect(20, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_33.setObjectName("label_33")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_4.setGeometry(QtCore.QRect(440, 170, 751, 361))
        self.tableWidget_4.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_4.setColumnCount(6)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(31)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 570, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton#pushButton_8{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_8:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_8:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_19.setGeometry(QtCore.QRect(180, 190, 221, 31))
        self.lineEdit_19.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_45 = QtWidgets.QLabel(self.tab_5)
        self.label_45.setGeometry(QtCore.QRect(20, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_45.setObjectName("label_45")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_30.setGeometry(QtCore.QRect(180, 260, 221, 31))
        self.lineEdit_30.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.label_46 = QtWidgets.QLabel(self.tab_5)
        self.label_46.setGeometry(QtCore.QRect(20, 330, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_46.setObjectName("label_46")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_31.setGeometry(QtCore.QRect(180, 330, 221, 31))
        self.lineEdit_31.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.label_47 = QtWidgets.QLabel(self.tab_5)
        self.label_47.setGeometry(QtCore.QRect(20, 410, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_47.setObjectName("label_47")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_32.setGeometry(QtCore.QRect(180, 410, 221, 31))
        self.lineEdit_32.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_18.setGeometry(QtCore.QRect(240, 570, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton#pushButton_18 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_18:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_18:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_19.setGeometry(QtCore.QRect(1040, 570, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton#pushButton_19{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_19:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_19:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_49 = QtWidgets.QLabel(self.tab_5)
        self.label_49.setGeometry(QtCore.QRect(900, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_49.setObjectName("label_49")
        self.label_69 = QtWidgets.QLabel(self.tab_5)
        self.label_69.setGeometry(QtCore.QRect(1030, 100, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_69.setFont(font)
        self.label_69.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.tab_5)
        self.label_70.setGeometry(QtCore.QRect(20, 470, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_70.setFont(font)
        self.label_70.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_70.setObjectName("label_70")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.tab_5)
        self.dateEdit_5.setGeometry(QtCore.QRect(180, 470, 221, 22))
        self.dateEdit_5.setStyleSheet("background-color:#ffffff;")
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_8 = QtWidgets.QLabel(self.tab_6)
        self.label_8.setGeometry(QtCore.QRect(-10, 0, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_8.setText("")
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_20.setGeometry(QtCore.QRect(440, 100, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_34 = QtWidgets.QLabel(self.tab_6)
        self.label_34.setGeometry(QtCore.QRect(20, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_34.setObjectName("label_34")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_5.setGeometry(QtCore.QRect(440, 170, 751, 361))
        self.tableWidget_5.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(31)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton#pushButton_9 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_9:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_9:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_21.setGeometry(QtCore.QRect(180, 190, 221, 31))
        self.lineEdit_21.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_39 = QtWidgets.QLabel(self.tab_6)
        self.label_39.setGeometry(QtCore.QRect(270, 20, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_39.setObjectName("label_39")
        self.label_50 = QtWidgets.QLabel(self.tab_6)
        self.label_50.setGeometry(QtCore.QRect(910, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_50.setObjectName("label_50")
        self.label_65 = QtWidgets.QLabel(self.tab_6)
        self.label_65.setGeometry(QtCore.QRect(1030, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.tab_6)
        self.label_66.setGeometry(QtCore.QRect(20, 260, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_66.setObjectName("label_66")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_44.setGeometry(QtCore.QRect(180, 260, 221, 31))
        self.lineEdit_44.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.label_67 = QtWidgets.QLabel(self.tab_6)
        self.label_67.setGeometry(QtCore.QRect(20, 340, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_67.setObjectName("label_67")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_45.setGeometry(QtCore.QRect(180, 340, 221, 31))
        self.lineEdit_45.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.label_68 = QtWidgets.QLabel(self.tab_6)
        self.label_68.setGeometry(QtCore.QRect(20, 420, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_68.setFont(font)
        self.label_68.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_68.setObjectName("label_68")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_46.setGeometry(QtCore.QRect(180, 420, 221, 31))
        self.lineEdit_46.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.pushButton_30 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_30.setGeometry(QtCore.QRect(260, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("QPushButton#pushButton_30 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_30:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_30:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_31.setGeometry(QtCore.QRect(1040, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("QPushButton#pushButton_31 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_31:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_31:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_31.setObjectName("pushButton_31")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_7 = QtWidgets.QLabel(self.tab_7)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_7.setText("")
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_22.setGeometry(QtCore.QRect(440, 120, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_35 = QtWidgets.QLabel(self.tab_7)
        self.label_35.setGeometry(QtCore.QRect(10, 210, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_35.setObjectName("label_35")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_6.setGeometry(QtCore.QRect(440, 190, 751, 361))
        self.tableWidget_6.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_6.setColumnCount(4)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(186)
        self.tableWidget_6.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_6.verticalHeader().setDefaultSectionSize(31)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 570, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton#pushButton_10 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_10:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_10:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_23.setGeometry(QtCore.QRect(220, 210, 211, 31))
        self.lineEdit_23.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_40 = QtWidgets.QLabel(self.tab_7)
        self.label_40.setGeometry(QtCore.QRect(220, 40, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_40.setObjectName("label_40")
        self.label_51 = QtWidgets.QLabel(self.tab_7)
        self.label_51.setGeometry(QtCore.QRect(900, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_51.setObjectName("label_51")
        self.label_62 = QtWidgets.QLabel(self.tab_7)
        self.label_62.setGeometry(QtCore.QRect(10, 290, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_62.setObjectName("label_62")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_42.setGeometry(QtCore.QRect(220, 290, 211, 31))
        self.lineEdit_42.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.label_63 = QtWidgets.QLabel(self.tab_7)
        self.label_63.setGeometry(QtCore.QRect(10, 370, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_63.setObjectName("label_63")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_43.setGeometry(QtCore.QRect(220, 370, 211, 31))
        self.lineEdit_43.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_28.setGeometry(QtCore.QRect(260, 570, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("QPushButton#pushButton_28 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_28:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_28:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_29.setGeometry(QtCore.QRect(1050, 570, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("QPushButton#pushButton_29 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_29:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_29:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_29.setObjectName("pushButton_29")
        self.label_64 = QtWidgets.QLabel(self.tab_7)
        self.label_64.setGeometry(QtCore.QRect(1030, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_64.setObjectName("label_64")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_6 = QtWidgets.QLabel(self.tab_8)
        self.label_6.setGeometry(QtCore.QRect(-10, 0, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_6.setText("")
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_24.setGeometry(QtCore.QRect(440, 100, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_36 = QtWidgets.QLabel(self.tab_8)
        self.label_36.setGeometry(QtCore.QRect(0, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_36.setObjectName("label_36")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidget_7.setGeometry(QtCore.QRect(440, 170, 751, 361))
        self.tableWidget_7.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_7.setColumnCount(4)
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_7.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_7.verticalHeader().setDefaultSectionSize(31)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_11.setGeometry(QtCore.QRect(80, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton#pushButton_11 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_11:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_11:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_25.setGeometry(QtCore.QRect(210, 190, 221, 31))
        self.lineEdit_25.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.label_41 = QtWidgets.QLabel(self.tab_8)
        self.label_41.setGeometry(QtCore.QRect(280, 30, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_41.setObjectName("label_41")
        self.label_60 = QtWidgets.QLabel(self.tab_8)
        self.label_60.setGeometry(QtCore.QRect(0, 270, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_60.setObjectName("label_60")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_27.setGeometry(QtCore.QRect(210, 270, 221, 31))
        self.lineEdit_27.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_61 = QtWidgets.QLabel(self.tab_8)
        self.label_61.setGeometry(QtCore.QRect(0, 360, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_61.setObjectName("label_61")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_39.setGeometry(QtCore.QRect(210, 360, 221, 31))
        self.lineEdit_39.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_26.setGeometry(QtCore.QRect(260, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton#pushButton_26 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_26:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_26:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_27.setGeometry(QtCore.QRect(1050, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton#pushButton_27 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_27:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_27:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_27.setObjectName("pushButton_27")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.label_5 = QtWidgets.QLabel(self.tab_9)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_5.setText("")
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_26.setGeometry(QtCore.QRect(420, 90, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_37 = QtWidgets.QLabel(self.tab_9)
        self.label_37.setGeometry(QtCore.QRect(20, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_37.setObjectName("label_37")
        self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_9)
        self.tableWidget_8.setGeometry(QtCore.QRect(420, 160, 771, 361))
        self.tableWidget_8.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_8.setColumnCount(8)
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(7, item)
        self.tableWidget_8.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget_8.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_8.verticalHeader().setDefaultSectionSize(31)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_12.setGeometry(QtCore.QRect(40, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton#pushButton_12 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_12:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_12:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_42 = QtWidgets.QLabel(self.tab_9)
        self.label_42.setGeometry(QtCore.QRect(280, 20, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_42.setObjectName("label_42")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_36.setGeometry(QtCore.QRect(160, 150, 221, 31))
        self.lineEdit_36.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label_54 = QtWidgets.QLabel(self.tab_9)
        self.label_54.setGeometry(QtCore.QRect(20, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_54.setObjectName("label_54")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_37.setGeometry(QtCore.QRect(160, 210, 221, 31))
        self.lineEdit_37.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_55 = QtWidgets.QLabel(self.tab_9)
        self.label_55.setGeometry(QtCore.QRect(20, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_55.setObjectName("label_55")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_38.setGeometry(QtCore.QRect(160, 280, 221, 31))
        self.lineEdit_38.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.label_56 = QtWidgets.QLabel(self.tab_9)
        self.label_56.setGeometry(QtCore.QRect(20, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.tab_9)
        self.label_57.setGeometry(QtCore.QRect(20, 350, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_57.setObjectName("label_57")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_40.setGeometry(QtCore.QRect(160, 410, 221, 31))
        self.lineEdit_40.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.label_58 = QtWidgets.QLabel(self.tab_9)
        self.label_58.setGeometry(QtCore.QRect(20, 410, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_58.setObjectName("label_58")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_41.setGeometry(QtCore.QRect(160, 480, 221, 31))
        self.lineEdit_41.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_59 = QtWidgets.QLabel(self.tab_9)
        self.label_59.setGeometry(QtCore.QRect(20, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_59.setObjectName("label_59")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.tab_9)
        self.dateEdit_3.setGeometry(QtCore.QRect(160, 350, 221, 22))
        self.dateEdit_3.setStyleSheet("background-color:#ffffff;")
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.tab_9)
        self.dateEdit_4.setGeometry(QtCore.QRect(160, 90, 221, 22))
        self.dateEdit_4.setStyleSheet("background-color:#ffffff;")
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_24.setGeometry(QtCore.QRect(240, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton#pushButton_24 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_24:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_24:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_25.setGeometry(QtCore.QRect(1040, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton#pushButton_25 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_25:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_25:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_25.setObjectName("pushButton_25")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.label_4 = QtWidgets.QLabel(self.tab_10)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_4.setText("")
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_28.setGeometry(QtCore.QRect(440, 120, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.label_38 = QtWidgets.QLabel(self.tab_10)
        self.label_38.setGeometry(QtCore.QRect(10, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_38.setObjectName("label_38")
        self.tableWidget_9 = QtWidgets.QTableWidget(self.tab_10)
        self.tableWidget_9.setGeometry(QtCore.QRect(440, 190, 751, 361))
        self.tableWidget_9.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_9.setColumnCount(5)
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, item)
        self.tableWidget_9.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget_9.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_9.verticalHeader().setDefaultSectionSize(31)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_13.setGeometry(QtCore.QRect(40, 570, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton#pushButton_13 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_13:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_13:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_43 = QtWidgets.QLabel(self.tab_10)
        self.label_43.setGeometry(QtCore.QRect(270, 40, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_43.setObjectName("label_43")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_22.setGeometry(QtCore.QRect(260, 570, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("QPushButton#pushButton_22 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_22:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_23.setGeometry(QtCore.QRect(1050, 570, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("QPushButton#pushButton_23 {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_23:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_23:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_23.setObjectName("pushButton_23")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_33.setGeometry(QtCore.QRect(180, 190, 221, 31))
        self.lineEdit_33.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.label_48 = QtWidgets.QLabel(self.tab_10)
        self.label_48.setGeometry(QtCore.QRect(10, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_48.setObjectName("label_48")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_34.setGeometry(QtCore.QRect(180, 270, 221, 31))
        self.lineEdit_34.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.label_52 = QtWidgets.QLabel(self.tab_10)
        self.label_52.setGeometry(QtCore.QRect(10, 270, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_52.setObjectName("label_52")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_35.setGeometry(QtCore.QRect(180, 340, 221, 31))
        self.lineEdit_35.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.label_53 = QtWidgets.QLabel(self.tab_10)
        self.label_53.setGeometry(QtCore.QRect(10, 340, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_53.setObjectName("label_53")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_47.setGeometry(QtCore.QRect(180, 410, 221, 31))
        self.lineEdit_47.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.label_71 = QtWidgets.QLabel(self.tab_10)
        self.label_71.setGeometry(QtCore.QRect(10, 410, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_71.setFont(font)
        self.label_71.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_71.setObjectName("label_71")
        self.dateEdit_6 = QtWidgets.QDateEdit(self.tab_10)
        self.dateEdit_6.setGeometry(QtCore.QRect(180, 120, 221, 22))
        self.dateEdit_6.setStyleSheet("background-color:#ffffff;")
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.label_3 = QtWidgets.QLabel(self.tab_11)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1221, 651))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color:rgba(0,0,0,100);")
        self.label_3.setText("")
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.tab_11)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1191, 611))
        self.widget.setStyleSheet("background-color:rgba(0,0,0,10);")
        self.widget.setObjectName("widget")
        self.Panel_predication_formation = QtWidgets.QPushButton(self.widget)
        self.Panel_predication_formation.setGeometry(QtCore.QRect(20, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Panel_predication_formation.setFont(font)
        self.Panel_predication_formation.setStyleSheet("QPushButton#Panel_predication_formation{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Panel_predication_formation:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Panel_predication_formation:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Panel_predication_formation.setObjectName("Panel_predication_formation")
        self.label_44 = QtWidgets.QLabel(self.widget)
        self.label_44.setGeometry(QtCore.QRect(240, 40, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_44.setObjectName("label_44")
        self.Panel_predication_formation_2 = QtWidgets.QPushButton(self.widget)
        self.Panel_predication_formation_2.setGeometry(QtCore.QRect(1000, 560, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Panel_predication_formation_2.setFont(font)
        self.Panel_predication_formation_2.setStyleSheet("QPushButton#Panel_predication_formation_2{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Panel_predication_formation_2:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Panel_predication_formation_2:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Panel_predication_formation_2.setObjectName("Panel_predication_formation_2")
        self.Panel_predication_formation_3 = QtWidgets.QPushButton(self.widget)
        self.Panel_predication_formation_3.setGeometry(QtCore.QRect(200, 560, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Panel_predication_formation_3.setFont(font)
        self.Panel_predication_formation_3.setStyleSheet("QPushButton#Panel_predication_formation_3{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Panel_predication_formation_3:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Panel_predication_formation_3:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Panel_predication_formation_3.setObjectName("Panel_predication_formation_3")
        self.dateEdit_7 = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_7.setGeometry(QtCore.QRect(170, 220, 221, 22))
        self.dateEdit_7.setObjectName("dateEdit_7")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_29.setGeometry(QtCore.QRect(430, 130, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.tableWidget_10 = QtWidgets.QTableWidget(self.tab_11)
        self.tableWidget_10.setGeometry(QtCore.QRect(430, 190, 753, 361))
        self.tableWidget_10.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_10.setColumnCount(4)
        self.tableWidget_10.setObjectName("tableWidget_10")
        self.tableWidget_10.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(3, item)
        self.tableWidget_10.horizontalHeader().setDefaultSectionSize(188)
        self.tableWidget_10.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_10.verticalHeader().setDefaultSectionSize(31)
        self.lineEdit_49 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_49.setGeometry(QtCore.QRect(180, 310, 221, 31))
        self.lineEdit_49.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.label_73 = QtWidgets.QLabel(self.tab_11)
        self.label_73.setGeometry(QtCore.QRect(10, 380, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_73.setFont(font)
        self.label_73.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_73.setObjectName("label_73")
        self.label_76 = QtWidgets.QLabel(self.tab_11)
        self.label_76.setGeometry(QtCore.QRect(10, 310, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_76.setObjectName("label_76")
        self.label_78 = QtWidgets.QLabel(self.tab_11)
        self.label_78.setGeometry(QtCore.QRect(10, 230, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_78.setFont(font)
        self.label_78.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_78.setObjectName("label_78")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_51.setGeometry(QtCore.QRect(180, 380, 221, 31))
        self.lineEdit_51.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.widget_2 = QtWidgets.QWidget(self.tab_14)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1201, 631))
        self.widget_2.setStyleSheet("background-color:rgba(0,0,0,90);")
        self.widget_2.setObjectName("widget_2")
        self.label_72 = QtWidgets.QLabel(self.widget_2)
        self.label_72.setGeometry(QtCore.QRect(240, 40, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_72.setFont(font)
        self.label_72.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_72.setObjectName("label_72")
        self.Btn_enregistrer_seminaire = QtWidgets.QPushButton(self.widget_2)
        self.Btn_enregistrer_seminaire.setGeometry(QtCore.QRect(30, 580, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_enregistrer_seminaire.setFont(font)
        self.Btn_enregistrer_seminaire.setStyleSheet("QPushButton#Btn_enregistrer_seminaire{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Btn_enregistrer_seminaire:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Btn_enregistrer_seminaire:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Btn_enregistrer_seminaire.setObjectName("Btn_enregistrer_seminaire")
        self.lineEdit_67 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_67.setGeometry(QtCore.QRect(180, 490, 221, 31))
        self.lineEdit_67.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.label_91 = QtWidgets.QLabel(self.widget_2)
        self.label_91.setGeometry(QtCore.QRect(10, 490, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_91.setFont(font)
        self.label_91.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_91.setObjectName("label_91")
        self.Btn_enregistrer_seminaire_2 = QtWidgets.QPushButton(self.widget_2)
        self.Btn_enregistrer_seminaire_2.setGeometry(QtCore.QRect(300, 580, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_enregistrer_seminaire_2.setFont(font)
        self.Btn_enregistrer_seminaire_2.setStyleSheet("QPushButton#Btn_enregistrer_seminaire_2{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Btn_enregistrer_seminaire_2:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Btn_enregistrer_seminaire_2:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Btn_enregistrer_seminaire_2.setObjectName("Btn_enregistrer_seminaire_2")
        self.Btn_enregistrer_seminaire_3 = QtWidgets.QPushButton(self.widget_2)
        self.Btn_enregistrer_seminaire_3.setGeometry(QtCore.QRect(950, 580, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_enregistrer_seminaire_3.setFont(font)
        self.Btn_enregistrer_seminaire_3.setStyleSheet("QPushButton#Btn_enregistrer_seminaire_3{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Btn_enregistrer_seminaire_3:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Btn_enregistrer_seminaire_3:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Btn_enregistrer_seminaire_3.setObjectName("Btn_enregistrer_seminaire_3")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_52.setGeometry(QtCore.QRect(180, 200, 221, 31))
        self.lineEdit_52.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_53.setGeometry(QtCore.QRect(440, 130, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_53.setFont(font)
        self.lineEdit_53.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.tableWidget_11 = QtWidgets.QTableWidget(self.tab_14)
        self.tableWidget_11.setGeometry(QtCore.QRect(440, 200, 751, 361))
        self.tableWidget_11.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_11.setColumnCount(6)
        self.tableWidget_11.setObjectName("tableWidget_11")
        self.tableWidget_11.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(5, item)
        self.tableWidget_11.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget_11.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_11.verticalHeader().setDefaultSectionSize(31)
        self.lineEdit_54 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_54.setGeometry(QtCore.QRect(180, 280, 221, 31))
        self.lineEdit_54.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.label_79 = QtWidgets.QLabel(self.tab_14)
        self.label_79.setGeometry(QtCore.QRect(10, 350, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.tab_14)
        self.label_80.setGeometry(QtCore.QRect(10, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.tab_14)
        self.label_81.setGeometry(QtCore.QRect(10, 420, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_81.setObjectName("label_81")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_55.setGeometry(QtCore.QRect(180, 420, 221, 31))
        self.lineEdit_55.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.label_82 = QtWidgets.QLabel(self.tab_14)
        self.label_82.setGeometry(QtCore.QRect(10, 200, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_82.setObjectName("label_82")
        self.lineEdit_56 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_56.setGeometry(QtCore.QRect(180, 350, 221, 31))
        self.lineEdit_56.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.tabWidget.addTab(self.tab_14, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.widget_3 = QtWidgets.QWidget(self.tab_13)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 1201, 631))
        self.widget_3.setStyleSheet("background-color:rgba(0,0,0,90);")
        self.widget_3.setObjectName("widget_3")
        self.pushButton_34 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_34.setGeometry(QtCore.QRect(20, 560, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("QPushButton#pushButton_34{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_34:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton_34:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.pushButton_34.setObjectName("pushButton_34")
        self.label_75 = QtWidgets.QLabel(self.widget_3)
        self.label_75.setGeometry(QtCore.QRect(230, 20, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_75.setObjectName("label_75")
        self.lineEdit_68 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_68.setGeometry(QtCore.QRect(180, 390, 221, 31))
        self.lineEdit_68.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_68.setText("")
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.label_92 = QtWidgets.QLabel(self.widget_3)
        self.label_92.setGeometry(QtCore.QRect(10, 390, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_92.setFont(font)
        self.label_92.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_92.setObjectName("label_92")
        self.lineEdit_69 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_69.setGeometry(QtCore.QRect(180, 460, 221, 31))
        self.lineEdit_69.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_69.setText("")
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.label_93 = QtWidgets.QLabel(self.widget_3)
        self.label_93.setGeometry(QtCore.QRect(10, 460, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_93.setFont(font)
        self.label_93.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_93.setObjectName("label_93")
        self.Modifier_courrier = QtWidgets.QPushButton(self.widget_3)
        self.Modifier_courrier.setGeometry(QtCore.QRect(220, 560, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Modifier_courrier.setFont(font)
        self.Modifier_courrier.setStyleSheet("QPushButton#Modifier_courrier{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Modifier_courrier:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Modifier_courrier:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Modifier_courrier.setObjectName("Modifier_courrier")
        self.Supprimer_courrier = QtWidgets.QPushButton(self.widget_3)
        self.Supprimer_courrier.setGeometry(QtCore.QRect(1030, 560, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Supprimer_courrier.setFont(font)
        self.Supprimer_courrier.setStyleSheet("QPushButton#Supprimer_courrier{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Supprimer_courrier:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Supprimer_courrier:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Supprimer_courrier.setObjectName("Supprimer_courrier")
        self.lineEdit_57 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_57.setGeometry(QtCore.QRect(180, 110, 221, 31))
        self.lineEdit_57.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_57.setText("")
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.lineEdit_58 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_58.setGeometry(QtCore.QRect(440, 90, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_58.setFont(font)
        self.lineEdit_58.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.tableWidget_12 = QtWidgets.QTableWidget(self.tab_13)
        self.tableWidget_12.setGeometry(QtCore.QRect(440, 160, 751, 361))
        self.tableWidget_12.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_12.setColumnCount(7)
        self.tableWidget_12.setObjectName("tableWidget_12")
        self.tableWidget_12.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(6, item)
        self.tableWidget_12.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget_12.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_12.verticalHeader().setDefaultSectionSize(31)
        self.lineEdit_59 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_59.setGeometry(QtCore.QRect(180, 190, 221, 31))
        self.lineEdit_59.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_59.setText("")
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.label_83 = QtWidgets.QLabel(self.tab_13)
        self.label_83.setGeometry(QtCore.QRect(10, 260, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.tab_13)
        self.label_84.setGeometry(QtCore.QRect(10, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.tab_13)
        self.label_85.setGeometry(QtCore.QRect(10, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_85.setFont(font)
        self.label_85.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_85.setObjectName("label_85")
        self.lineEdit_60 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_60.setGeometry(QtCore.QRect(180, 330, 221, 31))
        self.lineEdit_60.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_60.setText("")
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.label_86 = QtWidgets.QLabel(self.tab_13)
        self.label_86.setGeometry(QtCore.QRect(10, 110, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_86.setObjectName("label_86")
        self.lineEdit_61 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_61.setGeometry(QtCore.QRect(180, 260, 221, 31))
        self.lineEdit_61.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_61.setText("")
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.widget_4 = QtWidgets.QWidget(self.tab_12)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 1201, 631))
        self.widget_4.setStyleSheet("background-color:rgba(0,0,0,90);")
        self.widget_4.setObjectName("widget_4")
        self.Enregistrer_min_comite = QtWidgets.QPushButton(self.widget_4)
        self.Enregistrer_min_comite.setGeometry(QtCore.QRect(10, 570, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Enregistrer_min_comite.setFont(font)
        self.Enregistrer_min_comite.setStyleSheet("QPushButton#Enregistrer_min_comite{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Enregistrer_min_comite:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Enregistrer_min_comite:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Enregistrer_min_comite.setObjectName("Enregistrer_min_comite")
        self.label_74 = QtWidgets.QLabel(self.widget_4)
        self.label_74.setGeometry(QtCore.QRect(240, 20, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_74.setFont(font)
        self.label_74.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);\n"
"")
        self.label_74.setObjectName("label_74")
        self.Modifier_min_comite = QtWidgets.QPushButton(self.widget_4)
        self.Modifier_min_comite.setGeometry(QtCore.QRect(250, 570, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Modifier_min_comite.setFont(font)
        self.Modifier_min_comite.setStyleSheet("QPushButton#Modifier_min_comite{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Modifier_min_comite:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Modifier_min_comite:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Modifier_min_comite.setObjectName("Modifier_min_comite")
        self.Supprimer_min_comite = QtWidgets.QPushButton(self.widget_4)
        self.Supprimer_min_comite.setGeometry(QtCore.QRect(1000, 570, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Supprimer_min_comite.setFont(font)
        self.Supprimer_min_comite.setStyleSheet("QPushButton#Supprimer_min_comite{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: white;\n"
"}\n"
"\n"
"QPushButton#Supprimer_min_comite:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#Supprimer_min_comite:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: green;\n"
"}\n"
"")
        self.Supprimer_min_comite.setObjectName("Supprimer_min_comite")
        self.lineEdit_62 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_62.setGeometry(QtCore.QRect(180, 160, 221, 31))
        self.lineEdit_62.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.lineEdit_63 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_63.setGeometry(QtCore.QRect(430, 90, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_63.setFont(font)
        self.lineEdit_63.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.tableWidget_13 = QtWidgets.QTableWidget(self.tab_12)
        self.tableWidget_13.setGeometry(QtCore.QRect(430, 140, 761, 391))
        self.tableWidget_13.setStyleSheet("background-color:#ffffff;")
        self.tableWidget_13.setColumnCount(5)
        self.tableWidget_13.setObjectName("tableWidget_13")
        self.tableWidget_13.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(4, item)
        self.tableWidget_13.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidget_13.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_13.verticalHeader().setDefaultSectionSize(31)
        self.lineEdit_64 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_64.setGeometry(QtCore.QRect(180, 240, 221, 31))
        self.lineEdit_64.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.label_87 = QtWidgets.QLabel(self.tab_12)
        self.label_87.setGeometry(QtCore.QRect(10, 310, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_87.setObjectName("label_87")
        self.label_88 = QtWidgets.QLabel(self.tab_12)
        self.label_88.setGeometry(QtCore.QRect(10, 240, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_88.setObjectName("label_88")
        self.label_89 = QtWidgets.QLabel(self.tab_12)
        self.label_89.setGeometry(QtCore.QRect(10, 380, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_89.setFont(font)
        self.label_89.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_89.setObjectName("label_89")
        self.lineEdit_65 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_65.setGeometry(QtCore.QRect(180, 380, 221, 31))
        self.lineEdit_65.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.label_90 = QtWidgets.QLabel(self.tab_12)
        self.label_90.setGeometry(QtCore.QRect(10, 160, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("color:white;\n"
"background-color:rgba(0,0,0,50);")
        self.label_90.setObjectName("label_90")
        self.lineEdit_66 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_66.setGeometry(QtCore.QRect(180, 310, 221, 31))
        self.lineEdit_66.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.tabWidget.addTab(self.tab_12, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def insert_date(self):
            try:
                    mydb = mc.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="qt5"
                    )
                    mycursor = mydb.cursor()

                    nom = self.Text_nom_eglise.text()
                    prenom = self.Text_Adresse_eglise.text()

                    query = "INSERT INTO table_test (nom_test, prenom_test) VALUES (%s, %s)"
                    value = (nom, prenom)

                    mycursor.execute(query, value)

                    mydb.commit()  # Valider la transaction

                    # Maintenant, vous pouvez ajouter les données au QTableWidget
                    row_position = self.Tableau_nouvelle_Eglise.rowCount()  # Obtenir la position de la prochaine ligne disponible
                    self.Tableau_nouvelle_Eglise.insertRow(row_position)  # Insérer une nouvelle ligne

                    # Remplir les cellules avec les données
                    self.Tableau_nouvelle_Eglise.setItem(row_position, 0, QTableWidgetItem(nom))
                    self.Tableau_nouvelle_Eglise.setItem(row_position, 1, QTableWidgetItem(prenom))

                    # Effacez les QLineEdit après l'ajout
                    self.Text_nom_eglise.clear()
                    self.Text_Adresse_eglise.clear()

            except mc.Error as e:
                    print(f"Erreur MySQL: {e}")
            finally:
                    mydb.close()  # Fermer la connexion à la base de données

    #Fonction pour afficher
    def display_data(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="donnee_personne"
            )
            mycursor = mydb.cursor()

            query = "SELECT nom_etd, prenom_etd, Adress_etd, age_etd FROM tableau_enregistrement"
            mycursor.execute(query)

            for row_data in mycursor.fetchall():
                nom, prenom, adressetd, ageetd = row_data

                row_position = self.Tableau_nouvelle_Eglise.rowCount()
                self.Tableau_nouvelle_Eglise.insertRow(row_position)
                self.Tableau_nouvelle_Eglise.setItem(row_position, 1, QTableWidgetItem(nom))
                self.Tableau_nouvelle_Eglise.setItem(row_position, 2, QTableWidgetItem(prenom))
                self.Tableau_nouvelle_Eglise.setItem(row_position, 3, QTableWidgetItem(adressetd))
                self.Tableau_nouvelle_Eglise.setItem(row_position, 4, QTableWidgetItem(ageetd))

        except mc.Error as e:
            print(f"Erreur MySQL: {e}")
        finally:
            mydb.close()

    def confirm_delete(self):
        # Créez une boîte de dialogue de confirmation
        confirm_box = QMessageBox()
        confirm_box.setIcon(QMessageBox.Question)
        confirm_box.setWindowTitle("Confirmation de suppression")
        confirm_box.setText("Êtes-vous sûr de vouloir supprimer l'élément sélectionné?")
        confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Exécutez la boîte de dialogue et vérifiez la réponse de l'utilisateur
        response = confirm_box.exec_()

        if response == QMessageBox.Yes:
            # L'utilisateur a cliqué sur "Oui", donc nous pouvons supprimer l'élément
            self.delete_selected_item()
        else:
            # L'utilisateur a cliqué sur "Non" ou a fermé la boîte de dialogue
            print("Suppression annulée.")

    def delete_selected_item(self):
            try:
                    mydb = mc.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="qt5"
                    )
                    mycursor = mydb.cursor()

                    selected_row = self.Tableau_nouvelle_Eglise.currentRow()  # Obtenez l'indice de la ligne sélectionnée

                    if selected_row >= 0:
                            nom = self.Tableau_nouvelle_Eglise.item(selected_row,
                                                                    0).text()  # Obtenez le nom de la colonne 0
                            prenom = self.Tableau_nouvelle_Eglise.item(selected_row,
                                                                       1).text()  # Obtenez le nom de la colonne 1

                            # Requête SQL DELETE pour supprimer l'élément sélectionné
                            query = "DELETE FROM table_test WHERE nom_test = %s AND prenom_test = %s"
                            value = (nom, prenom)

                            mycursor.execute(query, value)
                            mydb.commit()  # Valider la transaction

                            # Supprimez la ligne du QTableWidget
                            self.Tableau_nouvelle_Eglise.removeRow(selected_row)

                    else:
                            print("Aucune ligne sélectionnée.")

            except mc.Error as e:
                    print(f"Erreur MySQL: {e}")
            finally:
                    mydb.close()  # Fermer la connexion à la base de données






    def update_lineedits(self):
        selected_items = self.Tableau_nouvelle_Eglise.selectedItems()

        if len(selected_items) == 2:  # Supposons que vous avez deux colonnes dans votre QTableWidget
            nom = selected_items[0].text()
            prenom = selected_items[1].text()
            self.Text_nom_eglise.setText(nom)
            self.Text_Adresse_eglise.setText(prenom)
        else:
            # Effacez les QLineEdit si aucune ligne n'est sélectionnée ou si la sélection est invalide
            self.Text_nom_eglise.clear()
            self.Text_Adresse_eglise.clear()

    def rechercher(self):
            try:
                    recherche_texte = self.Text_Recherche_Nouvelle_Eglise.text()
                    self.Tableau_nouvelle_Eglise.setRowCount(0)  # Effacer le contenu actuel du tableau

                    if recherche_texte:
                            # Requête SQL pour rechercher des correspondances dans la base de données MySQL
                            query = "SELECT nom_test, prenom_test FROM table_test WHERE nom_test LIKE %s OR prenom_test LIKE %s"
                            self.cur.execute(query, ('%' + recherche_texte + '%', '%' + recherche_texte + '%'))
                    else:
                            # Si le champ de recherche est vide, affichez tous les éléments
                            #self.afficher_tous_elements()
                            self.display_data()

                    for row_number, row_data in enumerate(self.cur.fetchall()):
                            self.Tableau_nouvelle_Eglise.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                    item = QTableWidgetItem(str(data))
                                    self.Tableau_nouvelle_Eglise.setItem(row_number, column_number, item)
            except Exception as e:
                    print("Erreur dans la fonction rechercher:", str(e))



    def afficher_tous_elements(self):
        self.cur.execute("SELECT nom_test, prenom_test FROM table_test")
        for row_number, row_data in enumerate(self.cur.fetchall()):
            self.Tableau_nouvelle_Eglise.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.Tableau_nouvelle_Eglise.setItem(row_number, column_number, item)


    #Fonction pour modifier les éléments dans lineEdit
    def update_data(self):
            selected_items = self.Tableau_nouvelle_Eglise.selectedItems()

            if len(selected_items) == 2:  # Assurez-vous que deux colonnes sont sélectionnées
                    nom = selected_items[0].text()
                    prenom = self.Text_Adresse_eglise.text()

                    try:
                            mydb = mc.connect(
                                    host="localhost",
                                    user="root",
                                    password="",
                                    database="qt5"
                            )
                            mycursor = mydb.cursor()

                            # Effectuer la mise à jour en utilisant le nom sélectionné
                            query = "UPDATE table_test SET prenom_test = %s WHERE nom_test = %s"
                            mycursor.execute(query, (prenom, nom))
                            mydb.commit()  # Valider la transaction

                            # Mettre à jour le QTableWidget avec les nouvelles données
                            for row in range(self.Tableau_nouvelle_Eglise.rowCount()):
                                    item = self.Tableau_nouvelle_Eglise.item(row, 0)
                                    if item and item.text() == nom:
                                            self.Tableau_nouvelle_Eglise.setItem(row, 1, QTableWidgetItem(prenom))
                                            break

                            # Effacer le QLineEdit après la mise à jour
                            self.Text_Adresse_eglise.clear()
                            self.Text_nom_eglise.clear()
                    except mc.Error as e:
                            print(f"Erreur MySQL: {e}")
                    finally:
                            mydb.close()
            else:
                    print("Sélectionnez une ligne contenant le nom à mettre à jour.")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "travail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "ACCUEIL"))
        self.label_13.setText(_translate("Form", "Nom de l\'Eglise"))
        self.label_14.setText(_translate("Form", "Adresse"))
        self.label_15.setText(_translate("Form", "Date d\'ouverture"))
        self.label_16.setText(_translate("Form", "Date d\'organisation"))
        self.label_17.setText(_translate("Form", "Mesure du terrain"))
        self.label_18.setText(_translate("Form", "Mesure de l\'Eglise"))
        self.label_19.setText(_translate("Form", "Référence du terrain"))
        self.label_20.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Nouvelle Église</span></p></body></html>"))
        item = self.Tableau_nouvelle_Eglise.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.Tableau_nouvelle_Eglise.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nom"))
        item = self.Tableau_nouvelle_Eglise.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Adresse"))
        item = self.Tableau_nouvelle_Eglise.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Date ouverture"))
        item = self.Tableau_nouvelle_Eglise.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Date org°"))
        item = self.Tableau_nouvelle_Eglise.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Ms Terrain"))
        item = self.Tableau_nouvelle_Eglise.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Ms Eglise"))
        item = self.Tableau_nouvelle_Eglise.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Référence"))
        self.Ajout_nouvelle_Eglise.setText(_translate("Form", "Enregistrer"))
        self.Modifier_nouvelle_eglise.setText(_translate("Form", "Modifier"))
        self.Supprimer_nouvelle_eglise.setText(_translate("Form", "Supprimer"))
        self.Text_Recherche_Nouvelle_Eglise.setPlaceholderText(_translate("Form", "RECHERCHER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "NOUVEAU"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "EGLISE"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "NOM Ps"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "PRENOM(S) Ps"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "COORDONNEE"))
        self.label_21.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ADMINISTRATEUR DES EGLISES</span></p></body></html>"))
        self.label_22.setText(_translate("Form", "Séléctionner leur catégorie"))
        self.label_23.setText(_translate("Form", "Eglise"))
        self.label_24.setText(_translate("Form", "Nom"))
        self.label_25.setText(_translate("Form", "Prénom"))
        self.label_26.setText(_translate("Form", "Coordonnée"))
        self.lineEdit_11.setPlaceholderText(_translate("Form", "RECHERCHER"))
        self.pushButton_4.setText(_translate("Form", "Enregistrer"))
        self.pushButton_5.setText(_translate("Form", "Modifier"))
        self.pushButton_6.setText(_translate("Form", "Enregistrer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "ADMINISTRATEURS DES EGLISES"))
        self.label_27.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">OBJECTIFS DE FIDELITE EN DIMES ET OFFRANDES</span></p></body></html>"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "EGLISE"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "OBJECTIF en %"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "OBJECTIF DE DIMES"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "OBJECTIF D\'OFFRANDE"))
        self.label_28.setText(_translate("Form", "Eglises"))
        self.lineEdit_14.setPlaceholderText(_translate("Form", "RECHERCHER"))
        self.pushButton_7.setText(_translate("Form", "Enregistrer"))
        self.label_29.setText(_translate("Form", "Objectif en %"))
        self.label_30.setText(_translate("Form", "Objectif de Dimes"))
        self.label_31.setText(_translate("Form", "Objectif d\'offandes"))
        self.pushButton_20.setText(_translate("Form", "Modifier"))
        self.pushButton_21.setText(_translate("Form", "Supprimer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "OBJECTIF DE FIDELITE"))
        self.label_32.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">VERSEMENT DE DIMES ET OFFRANDES</span></p></body></html>"))
        self.lineEdit_18.setPlaceholderText(_translate("Form", "RECHERCHER"))
        self.label_33.setText(_translate("Form", "Eglise"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Form", "EGLISE"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Form", "OFFRANDES FMC"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("Form", "OFFANDRES EGLISE"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("Form", "DIME"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("Form", "DATE D\'ENVOYE"))
        self.pushButton_8.setText(_translate("Form", "Enregistrer"))
        self.label_45.setText(_translate("Form", "Offande FMC"))
        self.label_46.setText(_translate("Form", "Offrande Eglises"))
        self.label_47.setText(_translate("Form", "DIME"))
        self.pushButton_18.setText(_translate("Form", "Modifier"))
        self.pushButton_19.setText(_translate("Form", "Supprimer"))
        self.label_49.setText(_translate("Form", "Mois de :"))
        self.label_69.setText(_translate("Form", "0"))
        self.label_70.setText(_translate("Form", "Date d\'envoye"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "VERSEMENT O & D"))
        self.lineEdit_20.setPlaceholderText(_translate("Form", "RECHERCHER"))
        self.label_34.setText(_translate("Form", "Eglise"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("Form", "DATE"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("Form", "MEMBRES VISITES"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("Form", "SUJET DE PRIERE "))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("Form", "REMARQUE(S)"))
        self.pushButton_9.setText(_translate("Form", "Enregistrer"))
        self.label_39.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">VISITES DES MEMBRES MENSUELLES</span></p></body></html>"))
        self.label_50.setText(_translate("Form", "Mois de :"))
        self.label_65.setText(_translate("Form", "0"))
        self.label_66.setText(_translate("Form", "Mbre Visites"))
        self.label_67.setText(_translate("Form", "Sujet de prière"))
        self.label_68.setText(_translate("Form", "Remarques"))
        self.pushButton_30.setText(_translate("Form", "Modifier"))
        self.pushButton_31.setText(_translate("Form", "Supprimer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "VISITES DES MEMBRES"))
        self.lineEdit_22.setPlaceholderText(_translate("Form", "RECHERCHER"))
        self.label_35.setText(_translate("Form", "Eglise"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("Form", "EGLISE"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("Form", "NOMBRE DE BAPTEME"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("Form", "DATE DE BAPTEME"))
        self.pushButton_10.setText(_translate("Form", "Enregistrer"))
        self.label_40.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">BAPTEME MENSUELS</span></p></body></html>"))
        self.label_51.setText(_translate("Form", "Mois de :"))
        self.label_62.setText(_translate("Form", "Nombre de Baptême"))
        self.label_63.setText(_translate("Form", "Eglise"))
        self.pushButton_28.setText(_translate("Form", "Modifier"))
        self.pushButton_29.setText(_translate("Form", "Supprimer"))
        self.label_64.setText(_translate("Form", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "BAPTEME MENSUELS"))
        self.lineEdit_24.setPlaceholderText(_translate("Form", "RECHERCHER"))
        self.label_36.setText(_translate("Form", "Eglise"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("Form", "EGLISE"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("Form", "OBJECTIF DU BATEME"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("Form", "NOMBRE DU BAPTEME"))
        self.pushButton_11.setText(_translate("Form", "Enregistrer"))
        self.label_41.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">BAPTEME ANNUELS PAR EGLISE</span></p></body></html>"))
        self.label_60.setText(_translate("Form", "Objectif de Baptême"))
        self.label_61.setText(_translate("Form", "Nombre de Baptême"))
        self.pushButton_26.setText(_translate("Form", "Modifier"))
        self.pushButton_27.setText(_translate("Form", "Supprimer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Form", "BAPTEME ANNUEL"))
        self.lineEdit_26.setPlaceholderText(_translate("Form", "RECHERCHER"))
        self.label_37.setText(_translate("Form", "Eglise"))
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Date du baptême"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("Form", "M/F"))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Nom"))
        item = self.tableWidget_8.horizontalHeaderItem(4)
        item.setText(_translate("Form", "OBJECTIF D\'OFFRANDE"))
        item = self.tableWidget_8.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Prénom(s)"))
        item = self.tableWidget_8.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date de naissance"))
        item = self.tableWidget_8.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Coordonnée"))
        self.pushButton_12.setText(_translate("Form", "Enregistrer"))
        self.label_42.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">LISTE DES BATIPSES</span></p></body></html>"))
        self.label_54.setText(_translate("Form", "Eglise"))
        self.label_55.setText(_translate("Form", "Eglise"))
        self.label_56.setText(_translate("Form", "Eglise"))
        self.label_57.setText(_translate("Form", "Eglise"))
        self.label_58.setText(_translate("Form", "Eglise"))
        self.label_59.setText(_translate("Form", "Eglise"))
        self.pushButton_24.setText(_translate("Form", "Modifier"))
        self.pushButton_25.setText(_translate("Form", "Supprimer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Form", "LISTE BAPTISES"))
        self.lineEdit_28.setPlaceholderText(_translate("Form", "RECHERCHER"))
        self.label_38.setText(_translate("Form", "Date"))
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("Form", "DATE"))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("Form", "EGLISE"))
        item = self.tableWidget_9.horizontalHeaderItem(3)
        item.setText(_translate("Form", "LIBELLES"))
        item = self.tableWidget_9.horizontalHeaderItem(4)
        item.setText(_translate("Form", "N° Vote Comite"))
        self.pushButton_13.setText(_translate("Form", "Enregistrer"))
        self.label_43.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">JOURNAL FINANCIER DES EGLISES</span></p></body></html>"))
        self.pushButton_22.setText(_translate("Form", "Modifier"))
        self.pushButton_23.setText(_translate("Form", "Supprimer"))
        self.label_48.setText(_translate("Form", "Eglise"))
        self.label_52.setText(_translate("Form", "Dépenses"))
        self.label_53.setText(_translate("Form", "Libelles"))
        self.label_71.setText(_translate("Form", "N° Vote Comite"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("Form", "FINANCE"))
        self.Panel_predication_formation.setText(_translate("Form", "Enregistrer"))
        self.label_44.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">PREDICATIONS ET FORMATIONS</span></p></body></html>"))
        self.Panel_predication_formation_2.setText(_translate("Form", "Supprimer"))
        self.Panel_predication_formation_3.setText(_translate("Form", "Modifier"))
        self.lineEdit_29.setPlaceholderText(_translate("Form", "RECHERCHER"))
        item = self.tableWidget_10.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_10.horizontalHeaderItem(1)
        item.setText(_translate("Form", "DATE"))
        item = self.tableWidget_10.horizontalHeaderItem(2)
        item.setText(_translate("Form", "EGLISE"))
        item = self.tableWidget_10.horizontalHeaderItem(3)
        item.setText(_translate("Form", "THEME"))
        self.label_73.setText(_translate("Form", "Thème"))
        self.label_76.setText(_translate("Form", "Eglise"))
        self.label_78.setText(_translate("Form", "Date"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("Form", "PREDICATIONS ET FORMATIONS"))
        self.label_72.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">SEMINAIRES ET CONFERENCES</span></p></body></html>"))
        self.Btn_enregistrer_seminaire.setText(_translate("Form", "Enregistrer"))
        self.label_91.setText(_translate("Form", "Baptises"))
        self.Btn_enregistrer_seminaire_2.setText(_translate("Form", "Modifier"))
        self.Btn_enregistrer_seminaire_3.setText(_translate("Form", "Supprimer"))
        self.lineEdit_53.setPlaceholderText(_translate("Form", "RECHERCHER"))
        item = self.tableWidget_11.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_11.horizontalHeaderItem(1)
        item.setText(_translate("Form", "DATE"))
        item = self.tableWidget_11.horizontalHeaderItem(2)
        item.setText(_translate("Form", "THEMES"))
        item = self.tableWidget_11.horizontalHeaderItem(3)
        item.setText(_translate("Form", "EGLISE"))
        item = self.tableWidget_11.horizontalHeaderItem(4)
        item.setText(_translate("Form", "INTERESSES"))
        item = self.tableWidget_11.horizontalHeaderItem(5)
        item.setText(_translate("Form", "BAPTISES"))
        self.label_79.setText(_translate("Form", "Eglise"))
        self.label_80.setText(_translate("Form", "Thèmes"))
        self.label_81.setText(_translate("Form", "Intéressés"))
        self.label_82.setText(_translate("Form", "Date"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), _translate("Form", "SEMINAIRES ET CONFERENCES"))
        self.pushButton_34.setText(_translate("Form", "Enregistrer"))
        self.label_75.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ENVOI ET RECEPTION LIVRE/COURIER</span></p></body></html>"))
        self.label_92.setText(_translate("Form", "Départ"))
        self.label_93.setText(_translate("Form", "Remarque"))
        self.Modifier_courrier.setText(_translate("Form", "Modifier"))
        self.Supprimer_courrier.setText(_translate("Form", "Supprimer"))
        self.lineEdit_58.setPlaceholderText(_translate("Form", "RECHERCHER"))
        item = self.tableWidget_12.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_12.horizontalHeaderItem(1)
        item.setText(_translate("Form", "DATE"))
        item = self.tableWidget_12.horizontalHeaderItem(2)
        item.setText(_translate("Form", "DESIGNATION"))
        item = self.tableWidget_12.horizontalHeaderItem(3)
        item.setText(_translate("Form", "NOMBRE"))
        item = self.tableWidget_12.horizontalHeaderItem(4)
        item.setText(_translate("Form", "ARRIVEE"))
        item = self.tableWidget_12.horizontalHeaderItem(5)
        item.setText(_translate("Form", "DEPART"))
        item = self.tableWidget_12.horizontalHeaderItem(6)
        item.setText(_translate("Form", "REMARQUE"))
        self.label_83.setText(_translate("Form", "Nombre"))
        self.label_84.setText(_translate("Form", "Designation"))
        self.label_85.setText(_translate("Form", "Arrivee"))
        self.label_86.setText(_translate("Form", "Date"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("Form", "ENVOI ET RECEPTION LIVRE/COURRIER"))
        self.Enregistrer_min_comite.setText(_translate("Form", "Enregistrer"))
        self.label_74.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">MINUTES DU COMITE</span></p></body></html>"))
        self.Modifier_min_comite.setText(_translate("Form", "Modifier"))
        self.Supprimer_min_comite.setText(_translate("Form", "Supprimer"))
        self.lineEdit_63.setPlaceholderText(_translate("Form", "RECHERCHER"))
        item = self.tableWidget_13.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#N°"))
        item = self.tableWidget_13.horizontalHeaderItem(1)
        item.setText(_translate("Form", "N° DE VOTE"))
        item = self.tableWidget_13.horizontalHeaderItem(2)
        item.setText(_translate("Form", "EGLISE"))
        item = self.tableWidget_13.horizontalHeaderItem(3)
        item.setText(_translate("Form", "DECISIONS PRISES"))
        item = self.tableWidget_13.horizontalHeaderItem(4)
        item.setText(_translate("Form", "RESPONSABLES"))
        self.label_87.setText(_translate("Form", "Décisions prises"))
        self.label_88.setText(_translate("Form", "Eglise"))
        self.label_89.setText(_translate("Form", "Responsables"))
        self.label_90.setText(_translate("Form", "N° de vote"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("Form", "MINUTES DU COMITE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    # Chargez les données en appelant la fonction load
    ui.load()
    # Activez la sélection d'une ligne entière en appelant la fonction
    ui.enable_row_selection()

    sys.exit(app.exec_())
