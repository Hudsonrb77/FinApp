# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_senha.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Senha(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 565)
        font = QtGui.QFont()
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/Dumbbell.png"))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 20, 551, 511))
        font = QtGui.QFont()
        font.setFamily("Rachana")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(36, 31, 49);\n"
"border-color: rgb(154, 153, 150);")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Rachana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(181, 131, 90);\n"
"background-color: rgba(0, 0, 0,0);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rachana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(181, 131, 90);\n"
"background-color: rgba(0, 0, 0,0);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.btn_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrar.setGeometry(QtCore.QRect(260, 360, 241, 31))
        self.btn_entrar.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_entrar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(230, 97, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(36, 31, 49);\n"
"}")
        self.btn_entrar.setObjectName("btn_entrar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 110, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-180, -127, 1920, 1080))
        self.label_8.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label_8.setStyleSheet("background-color: rgba(40, 35, 53,0.9);\n"
"border-color: rgb(154, 153, 150);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("img/return.png"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(729, 219, 1801, 991))
        self.label_9.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label_9.setStyleSheet("background-color: rgba(40, 35, 53,0.9);\n"
"border-color: rgb(154, 153, 150);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(210, 190, 101, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_10.setObjectName("label_10")
        self.txt_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_senha.setGeometry(QtCore.QRect(200, 213, 351, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy)
        self.txt_senha.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 2px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgb(36, 31, 49);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"")
        self.txt_senha.setText("")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_senha.setDragEnabled(False)
        self.txt_senha.setReadOnly(False)
        self.txt_senha.setObjectName("txt_senha")
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
        self.btn_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_voltar.setGeometry(QtCore.QRect(305, 400, 151, 31))
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
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(210, 260, 141, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_11.setObjectName("label_11")
        self.txt_confSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_confSenha.setGeometry(QtCore.QRect(200, 280, 351, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_confSenha.sizePolicy().hasHeightForWidth())
        self.txt_confSenha.setSizePolicy(sizePolicy)
        self.txt_confSenha.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"    border: 2px solid orange;\n"
"    border-color: rgb(255, 255, 255);\n"
"    background-color: rgb(36, 31, 49);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"")
        self.txt_confSenha.setText("")
        self.txt_confSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_confSenha.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_confSenha.setDragEnabled(False)
        self.txt_confSenha.setReadOnly(False)
        self.txt_confSenha.setObjectName("txt_confSenha")
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.btn_entrar.raise_()
        self.label_10.raise_()
        self.txt_senha.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.txt_cref_8.raise_()
        self.txt_cref_9.raise_()
        self.label_17.raise_()
        self.btn_voltar.raise_()
        self.label_11.raise_()
        self.txt_confSenha.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_senha, self.txt_confSenha)
        MainWindow.setTabOrder(self.txt_confSenha, self.btn_entrar)
        MainWindow.setTabOrder(self.btn_entrar, self.txt_cref_9)
        MainWindow.setTabOrder(self.txt_cref_9, self.btn_voltar)
        MainWindow.setTabOrder(self.btn_voltar, self.txt_cref_8)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Registrar-se"))
        self.label.setText(_translate("MainWindow", "personalApp"))
        self.btn_entrar.setText(_translate("MainWindow", "Registrar-se"))
        self.label_5.setText(_translate("MainWindow", "Por favor, preencha com os campos."))
        self.label_9.setText(_translate("MainWindow", "\'"))
        self.label_10.setText(_translate("MainWindow", "Senha"))
        self.label_15.setText(_translate("MainWindow", "\'"))
        self.label_16.setText(_translate("MainWindow", "Senha"))
        self.label_17.setText(_translate("MainWindow", "Confirmar Senha"))
        self.btn_voltar.setText(_translate("MainWindow", "Voltar"))
        self.label_11.setText(_translate("MainWindow", "Confirme sua senha"))