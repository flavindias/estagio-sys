import MySQLdb

connection = MySQLdb.connect(host="db4free.net", db="academicsys", user="desenvolvedores", passwd="acesso")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Aluno ( \
cpf CHAR(14) NOT NULL ,\
data_nascimento CHAR(8) NOT NULL ,\
sexo TINYINT(1)  NOT NULL ,\
nome VARCHAR(45) NOT NULL ,\
mae VARCHAR(45) NOT NULL ,\
pai VARCHAR(45) NULL ,\
cep CHAR(10) NOT NULL ,\
numero VARCHAR(8) NOT NULL ,\
complemento VARCHAR(45) NOT NULL ,\
endereco VARCHAR(45) NOT NULL ,\
bairro VARCHAR(30) NOT NULL ,\
cidade VARCHAR(30) NOT NULL ,\
uf CHAR(2) NOT NULL ,\
matricula VARCHAR(14) NOT NULL ,\
departamento VARCHAR(5) NOT NULL , \
curso VARCHAR(40) NOT NULL ,\
ano_conclusao CHAR(6) NOT NULL ,\
estagiando TINYINT(1)  NOT NULL ,\
manha TINYINT(1)  NULL ,\
tarde TINYINT(1)  NULL ,\
noite TINYINT(1)  NULL ,\
email VARCHAR(45) NULL ,\
telefone CHAR(13) NOT NULL ,\
celular CHAR(13) NOT NULL ,\
senha VARCHAR(12) NOT NULL ,\
PRIMARY KEY (cpf) ,\
UNIQUE INDEX cpf_UNIQUE (cpf) ,\
UNIQUE INDEX nome_UNIQUE (nome) );")

cursor.execute("CREATE  TABLE IF NOT EXISTS Empresa (\
cnpj CHAR(18) NOT NULL ,\
razao_social VARCHAR(45) NOT NULL ,\
nome_fantasia VARCHAR(45) NOT NULL ,\
cep CHAR(10) NOT NULL ,\
numero VARCHAR(8) NOT NULL ,\
complemento VARCHAR(45) NULL ,\
endereco VARCHAR(45) NOT NULL ,\
bairro VARCHAR(30) NOT NULL ,\
cidade VARCHAR(30) NOT NULL ,\
uf CHAR(2) NOT NULL ,\
nome_responsavel VARCHAR(45) NOT NULL ,\
email VARCHAR(45) NULL ,\
site VARCHAR(45) NOT NULL ,\
telefone VARCHAR(45) NOT NULL ,\
celular VARCHAR(45) NOT NULL ,\
senha VARCHAR(12) NOT NULL ,\
PRIMARY KEY (cnpj) ,\
UNIQUE INDEX cnpj_UNIQUE (cnpj) );")

cursor.execute("CREATE TABLE IF NOT EXISTS Funcionario (\
cpf CHAR(14) NOT NULL ,\
data_nascimento CHAR(8) NOT NULL ,\
sexo TINYINT(1)  NOT NULL ,\
nome VARCHAR(45) NOT NULL ,\
cep CHAR(10) NOT NULL ,\
numero VARCHAR(10) NOT NULL ,\
complemento VARCHAR(45) NULL ,\
endereco VARCHAR(45) NOT NULL ,\
bairro VARCHAR(45) NOT NULL ,\
cidade VARCHAR(45) NOT NULL ,\
uf CHAR(2) NOT NULL ,\
telefone CHAR(13) NOT NULL ,\
celular CHAR(13) NOT NULL ,\
tipo_usuario VARCHAR(8) NOT NULL ,\
senha VARCHAR(12) NOT NULL ,\
PRIMARY KEY (cpf) ,\
UNIQUE INDEX cpf_UNIQUE (cpf) );")

def createAluno():
    pass

def createFuncionario():
    pass

def createEmpresa():
    pass

def deleteAluno():
    pass

def deleteFuncionario():
    pass

def deleteEmpresa():
    pass

def alteraAluno():
    pass

def alteraFuncionario():
    pass

def alteraEmpresa():
    pass
