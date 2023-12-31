# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_logado.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Logado(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 625)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-370, -30, 100, 1080))
        self.label_8.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgba(40, 35, 53,0.9);\n"
"border-color: rgb(154, 153, 150);")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 271, 581))
        font = QtGui.QFont()
        font.setFamily("Rachana")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(26, 95, 180);\n"
"border-color: rgb(154, 153, 150);\n"
"border-radius:10px")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 40, 40))
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("img/profile-user.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.txt_nomeUsuario = QtWidgets.QLabel(self.centralwidget)
        self.txt_nomeUsuario.setGeometry(QtCore.QRect(70, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_nomeUsuario.setFont(font)
        self.txt_nomeUsuario.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.txt_nomeUsuario.setObjectName("txt_nomeUsuario")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(0, -150, 1920, 1080))
        self.label_9.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgba(53, 132, 228,0.9);\n"
"border-color: rgb(154, 153, 150);")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("img/Dumbbell.png"))
        self.label_9.setObjectName("label_9")
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(50, 90, 71, 21))
        self.btn_sair.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_sair.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.btn_sair.setFont(font)
        self.btn_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sair.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(230, 97, 0,0);\n"
"    \n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(230, 97, 0);\n"
"    background-color: rgba(230, 97, 0,0);\n"
"    \n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_sair.setIcon(icon)
        self.btn_sair.setObjectName("btn_sair")
        self.btn_verTodos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verTodos.setGeometry(QtCore.QRect(170, 200, 151, 31))
        self.btn_verTodos.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_verTodos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_verTodos.setFont(font)
        self.btn_verTodos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_verTodos.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(230, 97, 0,0);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(230, 97, 0);\n"
"    background-color: rgba(230, 97, 0,0);\n"
"    \n"
"}")
        self.btn_verTodos.setObjectName("btn_verTodos")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.btn_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrar.setGeometry(QtCore.QRect(460, 460, 151, 41))
        self.btn_entrar.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_entrar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet("QPushButton{    \n"
"    \n"
"    background-color: rgb(225, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(36, 31, 49);\n"
"}")
        self.btn_entrar.setObjectName("btn_entrar")
        self.btn_entrar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrar_2.setGeometry(QtCore.QRect(300, 460, 151, 41))
        self.btn_entrar_2.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_entrar_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_entrar_2.setFont(font)
        self.btn_entrar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_entrar_2.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    background-color: rgb(3, 235, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(36, 31, 49);\n"
"}")
        self.btn_entrar_2.setObjectName("btn_entrar_2")
        self.cref_2 = QtWidgets.QLabel(self.centralwidget)
        self.cref_2.setGeometry(QtCore.QRect(-180, -220, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cref_2.setFont(font)
        self.cref_2.setStyleSheet("font-weight: italic;\n"
"color: rgb(255, 255, 255);")
        self.cref_2.setObjectName("cref_2")
        self.txt_despesa = QtWidgets.QLabel(self.centralwidget)
        self.txt_despesa.setGeometry(QtCore.QRect(550, 50, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.txt_despesa.setFont(font)
        self.txt_despesa.setStyleSheet("font-weight: italic;\n"
"color: rgb(225, 0, 0);")
        self.txt_despesa.setObjectName("txt_despesa")
        self.nomePersonal_3 = QtWidgets.QLabel(self.centralwidget)
        self.nomePersonal_3.setGeometry(QtCore.QRect(70, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.nomePersonal_3.setFont(font)
        self.nomePersonal_3.setStyleSheet("color: rgb(86, 203, 255);\n"
"font-weight: bold;")
        self.nomePersonal_3.setObjectName("nomePersonal_3")
        self.txt_saldoAtual = QtWidgets.QLabel(self.centralwidget)
        self.txt_saldoAtual.setGeometry(QtCore.QRect(200, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.txt_saldoAtual.setFont(font)
        self.txt_saldoAtual.setStyleSheet("font-weight: italic;\n"
"color: rgb(86, 203, 255);")
        self.txt_saldoAtual.setObjectName("txt_saldoAtual")
        self.cref_5 = QtWidgets.QLabel(self.centralwidget)
        self.cref_5.setGeometry(QtCore.QRect(170, 70, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cref_5.setFont(font)
        self.cref_5.setStyleSheet("font-weight: italic;\n"
"color: rgb(86, 203, 255);")
        self.cref_5.setObjectName("cref_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 230, 271, 361))
        font = QtGui.QFont()
        font.setFamily("Rachana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(153, 193, 241);\n"
"border-color: rgb(154, 153, 150);\n"
"\n"
"border-radius:10px")
        self.label_10.setText("")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(330, 10, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Rachana")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(153, 193, 241);\n"
"border-color: rgb(154, 153, 150);\n"
"border-radius:10px")
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(153, 193, 241);\n"
"border-radius: 10px; \n"
"color: rgb(6, 24, 90);\n"
"font-weight: bold;\n"
"border: 0.5px solid dark blue;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(550, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(153, 193, 241);\n"
"border-radius: 10px; \n"
"color: rgb(6, 24, 90);\n"
"font-weight: bold;\n"
"border: 0.5px solid dark blue;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.txt_receita_2 = QtWidgets.QLabel(self.centralwidget)
        self.txt_receita_2.setGeometry(QtCore.QRect(390, 50, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.txt_receita_2.setFont(font)
        self.txt_receita_2.setStyleSheet("font-weight: italic;\n"
"color: rgb(3, 235, 0);")
        self.txt_receita_2.setObjectName("txt_receita_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 255, 271, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.txt_transacao2Valor = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2Valor.setGeometry(QtCore.QRect(200, 235, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao2Valor.setFont(font)
        self.txt_transacao2Valor.setStyleSheet("font-weight: italic;\n"
"\n"
"color: rgb(3, 235, 0);")
        self.txt_transacao2Valor.setObjectName("txt_transacao2Valor")
        self.txt_transacao2 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2.setGeometry(QtCore.QRect(60, 230, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_transacao2.setFont(font)
        self.txt_transacao2.setStyleSheet("color: rgb(6, 24, 90);\n"
"font-weight: bold;")
        self.txt_transacao2.setObjectName("txt_transacao2")
        self.txt_transacao2Data = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2Data.setGeometry(QtCore.QRect(60, 245, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao2Data.setFont(font)
        self.txt_transacao2Data.setStyleSheet("color: rgb(119, 118, 123);\n"
"font-weight: bold;")
        self.txt_transacao2Data.setObjectName("txt_transacao2Data")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 345, 271, 41))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.txt_transacao2Data_2 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2Data_2.setGeometry(QtCore.QRect(60, 335, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao2Data_2.setFont(font)
        self.txt_transacao2Data_2.setStyleSheet("color: rgb(119, 118, 123);\n"
"font-weight: bold;")
        self.txt_transacao2Data_2.setObjectName("txt_transacao2Data_2")
        self.txt_transacao2_2 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2_2.setGeometry(QtCore.QRect(60, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_transacao2_2.setFont(font)
        self.txt_transacao2_2.setStyleSheet("color: rgb(6, 24, 90);\n"
"font-weight: bold;")
        self.txt_transacao2_2.setObjectName("txt_transacao2_2")
        self.txt_transacao2Valor_2 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2Valor_2.setGeometry(QtCore.QRect(200, 325, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao2Valor_2.setFont(font)
        self.txt_transacao2Valor_2.setStyleSheet("font-weight: italic;\n"
"color: rgb(225, 0, 0);")
        self.txt_transacao2Valor_2.setObjectName("txt_transacao2Valor_2")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 304, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_6.setFont(font)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.txt_transacao1Valor_2 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1Valor_2.setGeometry(QtCore.QRect(200, 285, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao1Valor_2.setFont(font)
        self.txt_transacao1Valor_2.setStyleSheet("font-weight: italic;\n"
"color: rgb(225, 0, 0);")
        self.txt_transacao1Valor_2.setObjectName("txt_transacao1Valor_2")
        self.txt_transacao1Data_2 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1Data_2.setGeometry(QtCore.QRect(60, 295, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao1Data_2.setFont(font)
        self.txt_transacao1Data_2.setStyleSheet("color: rgb(119, 118, 123);\n"
"font-weight: bold;")
        self.txt_transacao1Data_2.setObjectName("txt_transacao1Data_2")
        self.txt_transacao1_2 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1_2.setGeometry(QtCore.QRect(60, 275, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_transacao1_2.setFont(font)
        self.txt_transacao1_2.setStyleSheet("color: rgb(6, 24, 90);\n"
"font-weight: bold;")
        self.txt_transacao1_2.setObjectName("txt_transacao1_2")
        self.txt_transacao2_3 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2_3.setGeometry(QtCore.QRect(60, 505, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_transacao2_3.setFont(font)
        self.txt_transacao2_3.setStyleSheet("color: rgb(6, 24, 90);\n"
"font-weight: bold;")
        self.txt_transacao2_3.setObjectName("txt_transacao2_3")
        self.txt_transacao2Data_3 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2Data_3.setGeometry(QtCore.QRect(60, 430, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao2Data_3.setFont(font)
        self.txt_transacao2Data_3.setStyleSheet("color: rgb(119, 118, 123);\n"
"font-weight: bold;")
        self.txt_transacao2Data_3.setObjectName("txt_transacao2Data_3")
        self.txt_transacao2_4 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2_4.setGeometry(QtCore.QRect(60, 415, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_transacao2_4.setFont(font)
        self.txt_transacao2_4.setStyleSheet("color: rgb(6, 24, 90);\n"
"font-weight: bold;")
        self.txt_transacao2_4.setObjectName("txt_transacao2_4")
        self.txt_transacao2Valor_3 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2Valor_3.setGeometry(QtCore.QRect(200, 420, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao2Valor_3.setFont(font)
        self.txt_transacao2Valor_3.setStyleSheet("font-weight: italic;\n"
"\n"
"color: rgb(3, 235, 0);")
        self.txt_transacao2Valor_3.setObjectName("txt_transacao2Valor_3")
        self.txt_transacao1Valor_3 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1Valor_3.setGeometry(QtCore.QRect(200, 470, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao1Valor_3.setFont(font)
        self.txt_transacao1Valor_3.setStyleSheet("font-weight: italic;\n"
"color: rgb(225, 0, 0);")
        self.txt_transacao1Valor_3.setObjectName("txt_transacao1Valor_3")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(10, 489, 271, 31))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 400, 271, 31))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.txt_transacao2Valor_4 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2Valor_4.setGeometry(QtCore.QRect(200, 510, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao2Valor_4.setFont(font)
        self.txt_transacao2Valor_4.setStyleSheet("font-weight: italic;\n"
"color: rgb(225, 0, 0);")
        self.txt_transacao2Valor_4.setObjectName("txt_transacao2Valor_4")
        self.txt_transacao1Valor_4 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1Valor_4.setGeometry(QtCore.QRect(200, 376, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao1Valor_4.setFont(font)
        self.txt_transacao1Valor_4.setStyleSheet("font-weight: italic;\n"
"color: rgb(225, 0, 0);")
        self.txt_transacao1Valor_4.setObjectName("txt_transacao1Valor_4")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(10, 530, 271, 41))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.txt_transacao1Data_3 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1Data_3.setGeometry(QtCore.QRect(60, 386, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao1Data_3.setFont(font)
        self.txt_transacao1Data_3.setStyleSheet("color: rgb(119, 118, 123);\n"
"font-weight: bold;")
        self.txt_transacao1Data_3.setObjectName("txt_transacao1Data_3")
        self.txt_transacao1_3 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1_3.setGeometry(QtCore.QRect(60, 460, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_transacao1_3.setFont(font)
        self.txt_transacao1_3.setStyleSheet("color: rgb(6, 24, 90);\n"
"font-weight: bold;")
        self.txt_transacao1_3.setObjectName("txt_transacao1_3")
        self.txt_transacao1_4 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1_4.setGeometry(QtCore.QRect(60, 366, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_transacao1_4.setFont(font)
        self.txt_transacao1_4.setStyleSheet("color: rgb(6, 24, 90);\n"
"font-weight: bold;")
        self.txt_transacao1_4.setObjectName("txt_transacao1_4")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(10, 450, 271, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.txt_transacao1Data_4 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1Data_4.setGeometry(QtCore.QRect(60, 480, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao1Data_4.setFont(font)
        self.txt_transacao1Data_4.setStyleSheet("color: rgb(119, 118, 123);\n"
"font-weight: bold;")
        self.txt_transacao1Data_4.setObjectName("txt_transacao1Data_4")
        self.txt_transacao1Data_6 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1Data_6.setGeometry(QtCore.QRect(60, 525, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao1Data_6.setFont(font)
        self.txt_transacao1Data_6.setStyleSheet("color: rgb(119, 118, 123);\n"
"font-weight: bold;")
        self.txt_transacao1Data_6.setObjectName("txt_transacao1Data_6")
        self.txt_transacao2Valor_5 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2Valor_5.setGeometry(QtCore.QRect(200, 555, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao2Valor_5.setFont(font)
        self.txt_transacao2Valor_5.setStyleSheet("font-weight: italic;\n"
"color: rgb(225, 0, 0);")
        self.txt_transacao2Valor_5.setObjectName("txt_transacao2Valor_5")
        self.txt_transacao1Data_7 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao1Data_7.setGeometry(QtCore.QRect(60, 570, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txt_transacao1Data_7.setFont(font)
        self.txt_transacao1Data_7.setStyleSheet("color: rgb(119, 118, 123);\n"
"font-weight: bold;")
        self.txt_transacao1Data_7.setObjectName("txt_transacao1Data_7")
        self.txt_transacao2_5 = QtWidgets.QLabel(self.centralwidget)
        self.txt_transacao2_5.setGeometry(QtCore.QRect(60, 550, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_transacao2_5.setFont(font)
        self.txt_transacao2_5.setStyleSheet("color: rgb(6, 24, 90);\n"
"font-weight: bold;")
        self.txt_transacao2_5.setObjectName("txt_transacao2_5")
        self.label_9.raise_()
        self.label_7.raise_()
        self.btn_sair.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.txt_nomeUsuario.raise_()
        self.btn_verTodos.raise_()
        self.label_2.raise_()
        self.btn_entrar.raise_()
        self.btn_entrar_2.raise_()
        self.cref_2.raise_()
        self.nomePersonal_3.raise_()
        self.txt_saldoAtual.raise_()
        self.cref_5.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.txt_despesa.raise_()
        self.txt_receita_2.raise_()
        self.line_4.raise_()
        self.txt_transacao2Valor.raise_()
        self.txt_transacao2.raise_()
        self.txt_transacao2Data.raise_()
        self.line_5.raise_()
        self.txt_transacao2Data_2.raise_()
        self.txt_transacao2_2.raise_()
        self.txt_transacao2Valor_2.raise_()
        self.line_6.raise_()
        self.txt_transacao1Valor_2.raise_()
        self.txt_transacao1Data_2.raise_()
        self.txt_transacao1_2.raise_()
        self.txt_transacao2_3.raise_()
        self.txt_transacao2Data_3.raise_()
        self.txt_transacao2_4.raise_()
        self.txt_transacao2Valor_3.raise_()
        self.txt_transacao1Valor_3.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.txt_transacao2Valor_4.raise_()
        self.txt_transacao1Valor_4.raise_()
        self.line_9.raise_()
        self.txt_transacao1Data_3.raise_()
        self.txt_transacao1_3.raise_()
        self.txt_transacao1_4.raise_()
        self.line_10.raise_()
        self.txt_transacao1Data_4.raise_()
        self.txt_transacao1Data_6.raise_()
        self.txt_transacao2Valor_5.raise_()
        self.txt_transacao1Data_7.raise_()
        self.txt_transacao2_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "\'"))
        self.txt_nomeUsuario.setText(_translate("MainWindow", "Hudson R. Bandeira"))
        self.btn_sair.setText(_translate("MainWindow", "Sair"))
        self.btn_verTodos.setText(_translate("MainWindow", "Ver todos"))
        self.label_2.setText(_translate("MainWindow", "Transações"))
        self.btn_entrar.setText(_translate("MainWindow", "Adicionar Despesa"))
        self.btn_entrar_2.setText(_translate("MainWindow", "Adicionar Ganho"))
        self.cref_2.setText(_translate("MainWindow", "R$"))
        self.txt_despesa.setText(_translate("MainWindow", "R$ 00,00"))
        self.nomePersonal_3.setText(_translate("MainWindow", "Saldo Atual:"))
        self.txt_saldoAtual.setText(_translate("MainWindow", "00,00"))
        self.cref_5.setText(_translate("MainWindow", "R$"))
        self.label_12.setText(_translate("MainWindow", "Receita"))
        self.label_13.setText(_translate("MainWindow", "Despesa"))
        self.txt_receita_2.setText(_translate("MainWindow", "R$ 00,00"))
        self.txt_transacao2Valor.setText(_translate("MainWindow", "R$ 00,00"))
        self.txt_transacao2.setText(_translate("MainWindow", "Conta de Luz"))
        self.txt_transacao2Data.setText(_translate("MainWindow", "23/11/2023"))
        self.txt_transacao2Data_2.setText(_translate("MainWindow", "23/11/2023"))
        self.txt_transacao2_2.setText(_translate("MainWindow", "Conta de Luz"))
        self.txt_transacao2Valor_2.setText(_translate("MainWindow", "R$ 00,00"))
        self.txt_transacao1Valor_2.setText(_translate("MainWindow", "R$ 00,00"))
        self.txt_transacao1Data_2.setText(_translate("MainWindow", "23/11/2023"))
        self.txt_transacao1_2.setText(_translate("MainWindow", "Academia"))
        self.txt_transacao2_3.setText(_translate("MainWindow", "Conta de Luz"))
        self.txt_transacao2Data_3.setText(_translate("MainWindow", "23/11/2023"))
        self.txt_transacao2_4.setText(_translate("MainWindow", "Conta de Luz"))
        self.txt_transacao2Valor_3.setText(_translate("MainWindow", "R$ 00,00"))
        self.txt_transacao1Valor_3.setText(_translate("MainWindow", "R$ 00,00"))
        self.txt_transacao2Valor_4.setText(_translate("MainWindow", "R$ 00,00"))
        self.txt_transacao1Valor_4.setText(_translate("MainWindow", "R$ 00,00"))
        self.txt_transacao1Data_3.setText(_translate("MainWindow", "23/11/2023"))
        self.txt_transacao1_3.setText(_translate("MainWindow", "Academia"))
        self.txt_transacao1_4.setText(_translate("MainWindow", "Academia"))
        self.txt_transacao1Data_4.setText(_translate("MainWindow", "23/11/2023"))
        self.txt_transacao1Data_6.setText(_translate("MainWindow", "23/11/2023"))
        self.txt_transacao2Valor_5.setText(_translate("MainWindow", "R$ 00,00"))
        self.txt_transacao1Data_7.setText(_translate("MainWindow", "23/11/2023"))
        self.txt_transacao2_5.setText(_translate("MainWindow", "Conta de Luz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Logado()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
