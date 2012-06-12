
from db import db

class DadosPessoais:
    'Classe de gerenciamento dos dados pessoais'
    def __init__(self, CPF = None):
        self.__DataBase = db()
        if CPF is None:
            self.setNomeAluno(None)
            self.
