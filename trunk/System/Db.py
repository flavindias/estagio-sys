import MySQLdb

connection = MySQLdb.connect(host="db4free.net", db="academicsys", user="desenvolvedores", passwd="acesso")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Aluno ( \
cpf CHAR(14) NOT NULL ,\
data_nascimento CHAR(8) NOT NULL ,\
sexo TINYINT(1)  NOT NULL ,\
nome VARCHAR(45) NOT NULL ,\
mae VARCHAR(45) NOT NULL ,\
pai VARCHAR(45) NULL ,\
cep CHAR(10) NOT NULL ,\
numero VARCHAR(8) NOT NULL ,\
complemento VARCHAR(45) NOT NULL ,\
endereco VARCHAR(45) NOT NULL ,\
bairro VARCHAR(30) NOT NULL ,\
cidade VARCHAR(30) NOT NULL ,\
uf CHAR(2) NOT NULL ,\
matricula VARCHAR(14) NOT NULL ,\
departamento VARCHAR(5) NOT NULL , \
curso VARCHAR(40) NOT NULL ,\
ano_conclusao CHAR(6) NOT NULL ,\
estagiando TINYINT(1)  NOT NULL ,\
manha TINYINT(1)  NULL ,\
tarde TINYINT(1)  NULL ,\
noite TINYINT(1)  NULL ,\
email VARCHAR(45) NULL ,\
telefone CHAR(13) NOT NULL ,\
celular CHAR(13) NOT NULL ,\
senha VARCHAR(12) NOT NULL ,\
PRIMARY KEY (cpf) ,\
UNIQUE INDEX cpf_UNIQUE (cpf) ,\
UNIQUE INDEX nome_UNIQUE (nome) );")

cursor.execute("CREATE  TABLE IF NOT EXISTS Empresa (\
cnpj CHAR(18) NOT NULL ,\
razao_social VARCHAR(45) NOT NULL ,\
nome_fantasia VARCHAR(45) NOT NULL ,\
cep CHAR(10) NOT NULL ,\
numero VARCHAR(8) NOT NULL ,\
complemento VARCHAR(45) NULL ,\
endereco VARCHAR(45) NOT NULL ,\
bairro VARCHAR(30) NOT NULL ,\
cidade VARCHAR(30) NOT NULL ,\
uf CHAR(2) NOT NULL ,\
nome_responsavel VARCHAR(45) NOT NULL ,\
email VARCHAR(45) NULL ,\
site VARCHAR(45) NOT NULL ,\
telefone VARCHAR(45) NOT NULL ,\
celular VARCHAR(45) NOT NULL ,\
senha VARCHAR(12) NOT NULL ,\
PRIMARY KEY (cnpj) ,\
UNIQUE INDEX cnpj_UNIQUE (cnpj) );")


cursor.execute("CREATE TABLE IF NOT EXISTS Funcionario (\
cpf CHAR(14) NOT NULL ,\
data_nascimento CHAR(8) NOT NULL ,\
sexo TINYINT(1)  NOT NULL ,\
nome VARCHAR(45) NOT NULL ,\
cep CHAR(10) NOT NULL ,\
numero VARCHAR(10) NOT NULL ,\
complemento VARCHAR(45) NULL ,\
endereco VARCHAR(45) NOT NULL ,\
bairro VARCHAR(45) NOT NULL ,\
cidade VARCHAR(45) NOT NULL ,\
uf CHAR(2) NOT NULL ,\
telefone CHAR(13) NOT NULL ,\
celular CHAR(13) NOT NULL ,\
tipo_usuario VARCHAR(8) NOT NULL ,\
senha VARCHAR(12) NOT NULL ,\
PRIMARY KEY (cpf) ,\
UNIQUE INDEX cpf_UNIQUE (cpf) );")

def createAluno(cpf , data_nascimento, sexo, nome, mae, cep,\
                numero, endereco, bairro, cidade, uf, matricula, \
                departamento , curso, ano_conclusao,\
                estagiando, telefone, celular, senha, pai = None, \
                complemento = None, email= None, manha = None, tarde = None, noite = None):
    cursor.execute("INSERT INTO Aluno(cpf, data_nascimento, sexo, nome, mae, pai, cep, \
                    numero, complemento, endereco, bairro, cidade, uf, matricula, departamento, \
                    curso, ano_conclusao, estagiando, manha, tarde, noite, email, telefone, \
                    celular, senha) VALUES ('%s', '%s', '%s', '%s', '%s', NULL, '%s', \
                    '%s', NULL, '%s', '%s', '%s', '%s', '%s', '%s', \
                    '%s', '%s', '%s', NULL, NULL, NULL, NULL, '%s', \
                    '%s', '%s')  ; " %(str(cpf), str(data_nascimento), str(sexo), str(nome), str(mae), str(cep), \
                    str(numero), str(endereco), str(bairro), str(cidade), str(uf), str(matricula), str(departamento), \
                    str(curso), str(ano_conclusao), str(estagiando), str(telefone), \
                    str(celular), str(senha)))

    if pai != None:
        cursor.execute("UPDATE Aluno SET pai = '%s' WHERE cpf = '%s';" %(str(pai), str(cpf)))
    if complemento != None:
        cursor.execute("UPDATE Aluno SET complemento = '%s' WHERE cpf = '%s';" %(str(complemento), str(cpf)))
    if manha != None:
        cursor.execute("UPDATE Aluno SET manha = '%s' WHERE cpf = '%s';" %(str(manha), str(cpf)))
    if tarde != None:
        cursor.execute("UPDATE Aluno SET tarde = '%s' WHERE cpf = '%s';" %(str(tarde), str(cpf)))
    if noite != None:
        cursor.execute("UPDATE Aluno SET noite = '%s' WHERE cpf = '%s';" %(str(noite), str(cpf)))
    if email != None:
        cursor.execute("UPDATE Aluno SET email = '%s' WHERE cpf = '%s';" %(str(email), str(cpf)))

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
