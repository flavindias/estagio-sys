import MySQLLdb

class db:
    "Classe que gerencia o banco de dados"
    def __init__(self):
        "Parametros de conexao com o banco de dados"
        self.conection = MySQLdb.conect(host="db4free.net", db="testesys", user="flavindiasdev", passwd="senhabd")
        self.cursor = self.conection.cursor()

