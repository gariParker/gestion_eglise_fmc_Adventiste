from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys,res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(853, 665)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setAcceptDrops(False)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 821, 631))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 391, 561))
        self.label.setStyleSheet("background-image:url(:/images/Eglise.jpg);\n"
"border-top-left-radius: 70px;\n"
"\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 391, 561))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,150);\n"
"border-top-left-radius: 70px;\n"
"\n"
"\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(386, 30, 401, 561))
        self.label_3.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius: 70px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(450, 90, 280, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 220, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 330, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(510, 450, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF,\n"
"        stop: 1 #FFFFFF);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    colo r: black;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #55AAFF, /* Bleu clair pour le hover */\n"
"        stop: 1 #0077CC); /* Bleu un peu plus foncé pour le hover */\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3399FF, /* Bleu clair pour le pressed */\n"
"        stop: 1 #0033AA); /* Bleu un peu plus foncé pour le pressed */\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(33, 260, 351, 171))
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,75);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 270, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(130, 320, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(240, 370, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(90, 30, 281, 165))
        self.label_9.setStyleSheet("background-image: url(:/images/R.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.Fonction_quitter = QtWidgets.QPushButton(self.widget)
        self.Fonction_quitter.setGeometry(QtCore.QRect(730, 30, 51, 51))
        self.Fonction_quitter.setStyleSheet("  background-image: url(:/images/Windows-Close-Program-icon.png);\n"
"  background-size: cover;\n"
"  background-repeat: no-repeat;\n"
"  background-position: center center;\n"
"  width: 20px;\n"
"  height: 20px;\n"
"\n"
"\n"
"")
        self.Fonction_quitter.setText("")
        self.Fonction_quitter.setObjectName("Fonction_quitter")
        # Connectez le clic du bouton à la fonction afficher_message
        self.Fonction_quitter.clicked.connect(self.afficher_message)
        self.pushButton.clicked.connect(self.test)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def afficher_message(self):
        QApplication.quit()

    def test(self):
        QApplication.quit()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Testt"))
        self.label_4.setText(_translate("Form", "AUTHENTIFICATION"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Nom"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Mot de passe"))
        self.pushButton.setText(_translate("Form", "Se connecter"))
        self.label_6.setText(_translate("Form", "FEDERATION"))
        self.label_7.setText(_translate("Form", "MADAGASCAR"))
        self.label_8.setText(_translate("Form", "CENTRE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
