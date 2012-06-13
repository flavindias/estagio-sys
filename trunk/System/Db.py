import MySQLdb

connection = MySQLdb.connect(host="db4free.net", db="academicsys", user="desenvolvedores", passwd="acesso")
cursor = connection.cursor()


#cursor.execute("CREATE TABLE IF NOT EXISTS Aluno(cpf CHAR(14) NOT NULL, data_nascimento CHAR(10) NOT NULL, sexo TINYINT(1) NOT NULL, nome VARCHAR(45) NOT NULL, mae VARCHAR(45) NOT NULL, pai VARCHAR(45) NULL, cep CHAR(10) NOT NULL, numero VARCHAR(8) NOT NULL, complemento VARCHAR(45), endereco VARCHAR(45) NOT NULL, bairro VARCHAR(30) NOT NULL, cidade VARCHAR(30) NOT NULL, uf CHAR(2) NOT NULL, matricula VARCHAR(14) NOT NULL, departamento VARCHAR(5) NOT NULL, curso VARCHAR(40) NOT NULL, ano_conclusao CHAR(6) NOT NULL, estagiando TINYINT(1) NOT NULL, manha TINYINT(1), tarde TINYINT(1), noite TINYINT(1), email VARCHAR(45), telefone CHAR(13) NOT NULL, celular CHAR(13) NOT NULL, senha VARCHAR(12) NOT NULL, PRIMARY KEY (cpf), UNIQUE (cpf), UNIQUE (nome) );")
#cursor.execute("CREATE TABLE IF NOT EXISTS Empresa (cnpj CHAR(18) NOT NULL, razao_social VARCHAR(45) NOT NULL, nome_fantasia VARCHAR(45) NOT NULL, cep CHAR(10) NOT NULL, numero VARCHAR(8) NOT NULL, complemento VARCHAR(45), endereco VARCHAR(45) NOT NULL, bairro VARCHAR(30) NOT NULL, cidade VARCHAR(30) NOT NULL, uf CHAR(2) NOT NULL, nome_responsavel VARCHAR(45) NOT NULL, email VARCHAR(45), site VARCHAR(45) NOT NULL, telefone VARCHAR(45) NOT NULL, celular VARCHAR(45) NOT NULL, login VARCHAR(18) NOT NULL, senha VARCHAR(12) NOT NULL, PRIMARY KEY (cnpj), UNIQUE (cnpj) ) ;")
#cursor.execute("CREATE TABLE IF NOT EXISTS Funcionario (cpf CHAR(14) NOT NULL, data_nascimento CHAR(10) NOT NULL, sexo TINYINT(1) NOT NULL, nome VARCHAR(45) NOT NULL, cep CHAR(10) NOT NULL, numero VARCHAR(10) NOT NULL, complemento VARCHAR(45), endereco VARCHAR(45) NOT NULL, bairro VARCHAR(45) NOT NULL, cidade VARCHAR(45) NOT NULL, uf CHAR(2) NOT NULL, telefone CHAR(13) NOT NULL, celular CHAR(13) NOT NULL, login VARCHAR(18) NOT NULL, tipo_usuario VARCHAR(8) NOT NULL, senha VARCHAR(12) NOT NULL, PRIMARY KEY (cpf), UNIQUE (cpf) ) ;")

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

def deleteAluno(cpf):
    """Deleta o aluno a partir de seu cpf"""
    cursor.execute("DELETE FROM Aluno WHERE cpf = '%s';" %(str(cpf)))

def deleteFuncionario():
    pass

def deleteEmpresa():
    pass

def alteraAluno(cpf, data_nascimento = None, sexo = None, nome = None, mae = None, \
                pai = None, cep = None, numero = None, complemento = None, \
                endereco = None, bairro = None, cidade = None, uf = None, \
                matricula = None, departamento = None, curso = None, ano_conclusao = None, \
                estagiando = None, manha = None, tarde = None, noite = None, email = None, \
                telefone = None, celular = None, senha = None):
    lista = []
    if data_nascimento != None:
        lista.append(('data_nascimento',data_nascimento))
    if sexo != None:
        lista.append(('sexo',sexo))
    if nome != None:
        lista.append(('nome',nome))
    if mae != None:
        lista.append(('mae',mae))
    if pai != None:
        lista.append(('pai',pai))
    if cep != None:
        lista.append(('cep',cep))
    if numero != None:
        lista.append(('numero', numero))
    if complemento != None:
        lista.append(('complemento',complemento))
    if endereco != None:
        lista.append(('endereco',endereco))
    if bairro != None:
        lista.append(('bairro',bairro))
    if cidade != None:
        lista.append(('cidade',cidade))
    if uf != None:
        lista.append(('uf',uf))
    if matricula != None:
        lista.append(('matricula', matricula))
    if departamento != None:
        lista.append(('departamento',departamento))
    if curso != None:
        lista.append(('curso', curso))
    if ano_conclusao != None:
        lista.append(('ano_conclusao',ano_conclusao))
    if estagiando != None:
        lista.append(('estagiando', estagiando))
    if manha != None:
        lista.append(('manha',manha))
    if tarde != None:
        lista.append(('tarde',tarde))
    if noite != None:
        lista.append(('noite',noite))
    if email != None:
        lista.append(('email', email))
    if telefone != None:
        lista.append(('telefone',telefone))
    if celular != None:
        lista.append(('celular',celular))
    if senha != None:
        lista.append(('senha',senha))

    for i in lista:
        cursor.execute("UPDATE Aluno SET '%s' = '%s' WHERE cpf = '%s';" %(str(i[0]), str(i[1]), str(cpf)))

def alteraFuncionario():
    pass

def alteraEmpresa():
    pass

def buscaAluno():
    pass

def buscaFuncionario():
    pass

def buscaEmpresa():
    pass
