import sys
import mysql.connector

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,  QMessageBox
# from PyQt5.QtCore import QCoreAppication
from tela_main import Tela_Main
from finBd import FinBD
from tela_logado import Tela_Logado
from tela_cadastro import Tela_Cadastro
#from cliente import Cliente
#from cadastro import Cadastro
#from tela_log import Tela_Login



class Ui_Main(QtWidgets.QWidget):
    
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640, 480)  # definindo o tamanho da tela

        # pilha de interface que diz qual tela deve estar em evidencia em de
        self.QtStack = QtWidgets.QStackedLayout()

        # Temos 3 telas, logo teremos tres stacks
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_main = Tela_Main()
        # essa linha serve para linkar a stack0 a tela_inicial .. Quando voce quiser chamar a tela inicial, é só chamar o stack_0.
        self.tela_main.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        # essa linha serve para linkar a stack0 a tela_cadastro .. Quando voce quiser chamar a tela cadastro, é só chamar o stack_1.
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_login = Tela_Logado()
        self.tela_login.setupUi(self.stack2)

        # Adicionando as telas ao Qtwidgets
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

# Aqui se encontra toda a logica do Sistema


class Main(QMainWindow, Ui_Main):
    
    def __init__(self, parent=None):
        """
        Inicializa a classe e configura a interface gráfica.

        Parameters
        ----------
        parent : None, optional
            O objeto pai (default is None)
        """
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.MyBD = FinBD(host="localhost", usuario="root", senha="master.750", banco_de_dados="FinApp")


        # Funções dos botoes da tela
        self.tela_main.btn_entrar.clicked.connect(self.botaoLogin)  # funcos dos botoes da tela principal
        self.tela_main.btn_cadastrar.clicked.connect(self.abrirTelaCadastro)
        # self.tela_inicial.pushButton_3.clicked.connect(self.sair)

        self.tela_cadastro.btn_registrar.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.btn_voltar.clicked.connect(self.abrirTelaInicial)

        #self.tela_logado.btn_entrar.clicked.connect(self.botaoCadastroSenha)
        #self.tela_logado.btn_voltar.clicked.connect(self.abrirTelaCadastro)


    def botaoCadastra(self):
        self.MyBD.criar_tabela_usuarios()
        
        nome = self.tela_cadastro.txt_nome.text()
        dataNascimento = self.tela_cadastro.txt_datanasc.text()
        cpf = self.tela_cadastro.txt_cpf.text()
        telefone = self.tela_cadastro.txt_telefone.text()
        email = self.tela_cadastro.txt_email.text()
        senha = self.tela_cadastro.txt_senha.text()
        confirmar_senha = self.tela_cadastro.txt_senha2.text()

        
        if not (nome == '' or dataNascimento == '' or cpf == '' or telefone == '' or email == '' or senha == '' or confirmar_senha == ''):  
            self.MyBD.registrar_usuario(nome, dataNascimento, cpf, telefone, email, senha, '','')

            cont = 0
            if cont == 1:
                QMessageBox.information(
                    None, 'POOII', 'A pessoa informada já está na base de dados.')
            
            else:
                QMessageBox.information(
                    None, 'POOII', 'A pessoa foi cadastrada.')

        else:
            QMessageBox.information(
                None, 'POOII', 'Todos os valores devem ser preenchidos.')

        #cursor.execute(sql)
        #cursor.execute('INSERT INTO usuarios (cpf, senha, nome, endereco, dataNascimento) VALUES (?, ?, ?, ?, ?)', (cpf, senha, nome, endereco, nascimento))
        

        # A saída final 'commit()' do objeto de banco de dados
        #conexao.commit()

    #def verificarCREFExistente(self, cref):
    #    consulta = "SELECT COUNT(*) FROM personalTrainer WHERE cref = %s"
    #    cursor.execute(consulta, (cref,))
    #    resultado = cursor.fetchone()
    #    return resultado[0] > 0



    def botaoLogin(self):

        email = self.tela_main.txt_email.text()
        senha = self.tela_main.txt_senha.text()
        result = self.MyBD.login(email, senha)

        if result == None:
            QMessageBox.information(None, 'POOII', 'Conta não encontrada! Preencha os campos corretamente. \nPossui uma conta? Se não, Crie a sua conta!')
            return False
        else:
            print('Entrou tela login')
            self.abrirTelaLogado()
        # conexao tela login


    def abrirTelaInicial(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaLogado(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaSenha(self):
        self.QtStack.setCurrentIndex(3)


    def sair(self):
        self.MyBD.commit()
        self.MyBD.fechar()
        sys.exit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    app.exec_()