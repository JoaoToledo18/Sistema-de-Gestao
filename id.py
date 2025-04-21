from conn import *
from abc import ABC, abstractmethod

class Id(ABC):
    def __init__(self, id):
        self.__id = id
    
    # metodo abstrato pois os campos dos objetos filhos sao diferentes um dos outros
    @abstractmethod
    def exibir(self):
        pass

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id