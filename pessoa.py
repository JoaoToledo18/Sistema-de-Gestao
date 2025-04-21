from id import *
from abc import ABC,abstractmethod

class Pessoa(Id, ABC):
    def __init__(self, nome, rg, cpf, telefone,id):
        super().__init__(id)
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__telefone = telefone

    def get_rg(self):
        return self.__rg
    
    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome
    
    def get_telefone(self):
        return self.__telefone