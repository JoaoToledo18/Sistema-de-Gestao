from models.id import *

class Estoque(Id):

    def __init__(self, id,nome,valor,qtd):
        super().__init__(id)
        self.__nome = nome
        self.__valor = valor
        self.__qtd = qtd

    def getNome(self):
        return self.__nome
    def getValor(self):
        return self.__valor
    def getQtd(self):
        return self.__qtd

    def exibir(self):
        return print(f"Peça: {self.__nome},ID: {self.getId()},Valor: {self.__valor}, Quantidade: {self.__qtd}")

    def select(self,dado):
        
        try:
            cursor.execute(f"select idEstoque,nome,valorUnit,quantidade from estoque where idEstoque = {dado};")
            for estoque in cursor:
                self.__nome = estoque[1]
                self.__valor = estoque[2]
                self.__qtd = estoque[3]
                self.setId(estoque[0])
        except mysql.connector.Error as err :
            print(err)

    def delete(self,dado):
        
        try:
            cursor.execute(f"delete from estoque where idEstoque = {dado};")
        except mysql.connector.Error as err:
            print(err)

    def update(self):
        
        try:
            cursor.execute(f"UPDATE estoque SET nome = '{self.__nome}', valorUnit = {self.__valor}, quantidade = {self.__qtd} WHERE idEstoque = {self.getId()};")
            bd.commit()
        except mysql.connector.Error as err:
            print(err)

    def insert(self,nome,valor,qtd):
        
        try:
            cursor.execute(f"insert into estoque(nome,valorUnit,quantidade) values ('{nome}',{valor},{qtd});")
            bd.commit()
            print("Peça cadastrada")
        except mysql.connector.Error as err:
            print(err)