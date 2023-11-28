# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Cadastro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 607)
        font = QtGui.QFont()
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 20, 561, 531))
        font = QtGui.QFont()
        font.setFamily("Rachana")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(26, 95, 180);\n"
"border-color: rgb(154, 153, 150);")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.btn_registrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registrar.setGeometry(QtCore.QRect(260, 430, 241, 31))
        self.btn_registrar.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_registrar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_registrar.setFont(font)
        self.btn_registrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_registrar.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    background-color: rgb(86, 203, 255);\n"
"    color: rgb(255,255,255);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(36, 31, 49);\n"
"}")
        self.btn_registrar.setObjectName("btn_registrar")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-180, -127, 1920, 1080))
        self.label_8.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label_8.setStyleSheet("background-color: rgba(53, 132, 228,0.9);\n"
"border-color: rgb(154, 153, 150);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("img/return.png"))
        self.label_8.setObjectName("label_8")
        self.btn_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cadastrar.setGeometry(QtCore.QRect(170, 370, 141, 45))
        self.btn_cadastrar.setMinimumSize(QtCore.QSize(110, 45))
        self.btn_cadastrar.setMaximumSize(QtCore.QSize(232123, 123231))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet("QPushButton{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(230, 97, 0);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(140, 173, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_10.setObjectName("label_10")
        self.txt_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nome.setGeometry(QtCore.QRect(130, 193, 351, 31))
        self.txt_nome.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 0.5px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgba(154, 153, 150,0.1);\n"
"    border-radius:15px\n"
"    \n"
"}\n"
"\n"
"")
        self.txt_nome.setText("")
        self.txt_nome.setObjectName("txt_nome")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(140, 283, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(380, 230, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(140, 230, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(800, 410, 1920, 1080))
        self.label_15.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label_15.setStyleSheet("background-color: rgba(40, 35, 53,0.9);\n"
"border-color: rgb(154, 153, 150);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(380, 680, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_16.setObjectName("label_16")
        self.txt_cref_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cref_8.setGeometry(QtCore.QRect(370, 700, 161, 31))
        self.txt_cref_8.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 2px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgb(36, 31, 49);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"")
        self.txt_cref_8.setText("")
        self.txt_cref_8.setObjectName("txt_cref_8")
        self.txt_cref_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cref_9.setGeometry(QtCore.QRect(540, 700, 161, 31))
        self.txt_cref_9.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 2px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgb(36, 31, 49);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"")
        self.txt_cref_9.setText("")
        self.txt_cref_9.setObjectName("txt_cref_9")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(550, 680, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(500, 173, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_19.setObjectName("label_19")
        self.txt_datanasc = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_datanasc.setGeometry(QtCore.QRect(490, 193, 141, 31))
        self.txt_datanasc.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 0.5px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgba(154, 153, 150,0.1);\n"
"    border-radius:15px\n"
"    \n"
"}\n"
"\n"
"")
        self.txt_datanasc.setText("")
        self.txt_datanasc.setObjectName("txt_datanasc")
        self.txt_email = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_email.setGeometry(QtCore.QRect(130, 303, 501, 31))
        self.txt_email.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 0.5px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgba(154, 153, 150,0.1);\n"
"    border-radius:15px\n"
"    \n"
"}\n"
"\n"
"")
        self.txt_email.setText("")
        self.txt_email.setObjectName("txt_email")
        self.txt_telefone = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_telefone.setGeometry(QtCore.QRect(370, 250, 261, 31))
        self.txt_telefone.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 0.5px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgba(154, 153, 150,0.1);\n"
"    border-radius:15px\n"
"    \n"
"}\n"
"\n"
"")
        self.txt_telefone.setText("")
        self.txt_telefone.setObjectName("txt_telefone")
        self.btn_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_voltar.setGeometry(QtCore.QRect(305, 470, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_voltar.setFont(font)
        self.btn_voltar.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(61, 56, 70);\n"
"    \n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(230, 97, 0);\n"
"    background-color: rgb(61, 56, 70);\n"
"    \n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_voltar.setIcon(icon)
        self.btn_voltar.setObjectName("btn_voltar")
        self.txt_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cpf.setGeometry(QtCore.QRect(130, 250, 231, 31))
        self.txt_cpf.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 0.5px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgba(154, 153, 150,0.1);\n"
"    border-radius:15px\n"
"    \n"
"}\n"
"\n"
"")
        self.txt_cpf.setText("")
        self.txt_cpf.setObjectName("txt_cpf")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rachana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(120, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Rachana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(120, 120, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(120, 40, 31, 31))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("img/Dumbbell.png"))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(380, 340, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(140, 340, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_23.setObjectName("label_23")
        self.txt_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_senha.setGeometry(QtCore.QRect(130, 360, 231, 31))
        self.txt_senha.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 0.5px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgba(154, 153, 150,0.1);\n"
"    border-radius:15px\n"
"    \n"
"}\n"
"\n"
"")
        self.txt_senha.setText("")
        self.txt_senha.setObjectName("txt_senha")
        self.txt_senha2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_senha2.setGeometry(QtCore.QRect(370, 360, 261, 31))
        self.txt_senha2.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 0.5px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgba(154, 153, 150,0.1);\n"
"    border-radius:15px\n"
"    \n"
"}\n"
"\n"
"")
        self.txt_senha2.setText("")
        self.txt_senha2.setObjectName("txt_senha2")
        self.label_8.raise_()
        self.btn_cadastrar.raise_()
        self.label_7.raise_()
        self.btn_registrar.raise_()
        self.label_10.raise_()
        self.txt_nome.raise_()
        self.label_11.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.txt_cref_8.raise_()
        self.txt_cref_9.raise_()
        self.label_17.raise_()
        self.label_19.raise_()
        self.txt_datanasc.raise_()
        self.txt_email.raise_()
        self.txt_telefone.raise_()
        self.btn_voltar.raise_()
        self.txt_cpf.raise_()
        self.label_6.raise_()
        self.label_18.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.txt_senha.raise_()
        self.txt_senha2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_nome, self.txt_datanasc)
        MainWindow.setTabOrder(self.txt_datanasc, self.txt_cpf)
        MainWindow.setTabOrder(self.txt_cpf, self.txt_telefone)
        MainWindow.setTabOrder(self.txt_telefone, self.txt_email)
        MainWindow.setTabOrder(self.txt_email, self.btn_registrar)
        MainWindow.setTabOrder(self.btn_registrar, self.btn_voltar)
        MainWindow.setTabOrder(self.btn_voltar, self.txt_cref_8)
        MainWindow.setTabOrder(self.txt_cref_8, self.txt_cref_9)
        MainWindow.setTabOrder(self.txt_cref_9, self.btn_cadastrar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_registrar.setText(_translate("MainWindow", "Registrar-se"))
        self.btn_cadastrar.setText(_translate("MainWindow", "Registrar-se"))
        self.label_10.setText(_translate("MainWindow", "Nome Completo"))
        self.label_11.setText(_translate("MainWindow", "Email"))
        self.label_13.setText(_translate("MainWindow", "Telefone"))
        self.label_14.setText(_translate("MainWindow", "CPF"))
        self.label_15.setText(_translate("MainWindow", "\'"))
        self.label_16.setText(_translate("MainWindow", "Senha"))
        self.label_17.setText(_translate("MainWindow", "Confirmar Senha"))
        self.label_19.setText(_translate("MainWindow", "Data de Nascimento"))
        self.btn_voltar.setText(_translate("MainWindow", "Voltar"))
        self.label_6.setText(_translate("MainWindow", "finApp"))
        self.label_18.setText(_translate("MainWindow", "Entrar"))
        self.label_20.setText(_translate("MainWindow", "Por favor, preencha com os seus dados"))
        self.label_22.setText(_translate("MainWindow", "Confirme sua senha"))
        self.label_23.setText(_translate("MainWindow", "Senha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Cadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
