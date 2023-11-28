import mysql.connector

class FinBD:
    def __init__(self, host, usuario, senha, banco_de_dados):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco_de_dados = banco_de_dados
        self.conexao = None
        self.conectar()

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco_de_dados
        )

    def criar_tabela_usuarios(self):
        cursor = self.conexao.cursor()

        criar_tabela_query = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_completo VARCHAR(255),
            data_nascimento VARCHAR(255),
            cpf VARCHAR(14),
            telefone VARCHAR(20),
            email VARCHAR(255),
            senha VARCHAR(255),
            saldo VARCHAR(255),
            despesas VARCHAR(255)
        );
        """
        cursor.execute(criar_tabela_query)
        self.conexao.commit()
        cursor.close()

    def registrar_usuario(self, nome_completo, data_nascimento, cpf, telefone, email, senha, saldo, despesa):
        cursor = self.conexao.cursor()
        inserir_query = """
        INSERT INTO usuarios (nome_completo, data_nascimento, cpf, telefone, email, senha, saldo, despesas)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        dados = (nome_completo, data_nascimento, cpf, telefone, email, senha, saldo, despesa)
        cursor.execute(inserir_query, dados)
        self.conexao.commit()
        cursor.close()

        
    def login(self, email, senha):
        cursor = self.conexao.cursor()
        consulta = """
        SELECT id FROM usuarios WHERE email = %s AND senha = %s;
        """
        dados = (email, senha)
        cursor.execute(consulta, dados)
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            return resultado[0]  # Retorna o ID do usuário se o login for bem-sucedido
        else:
            return None

    def fechar(self):
        if self.conexao:
            self.conexao.close()
