from models.pessoa import *

class Cliente(Pessoa):
    def __init__(self, nome, rg, cpf, telefone, id):
        super().__init__(nome, rg, cpf, telefone, id)

    def getNome(self):
        return self.__nome
    def getRg(self):
        return self.__rg
    def getCpf(self):
        return self.__cpf
    def getTelefone(self):
        return self.__telefone


    def exibir(self):
        return print(f"Nome: {self.__nome},ID:{self.__id} , RG: {self.__rg}, CPF:{self.__cpf}, Telefone: {self.__telefone}")

    def select(self, dado):

        try:
            #comando para a execução de um select dentro do banco de dados
            cursor.execute(f"select * from cliente where idcliente = {dado}")
            #função print das informações cadastradas no banco
            for dado in cursor:
                self.__nome = dado[1]
                self.__rg = dado[2]
                self.__cpf = dado[3]
                self.__telefone = dado[4]
                
        except:
            print("Esse cliente não existe")

    #Método que realiza um insert dentro do banco de dados com as informações fornecidas pelo usuario
    def insert(self, nome, rg, cpf, telefone):
        try:
            #comando que executa o insert no banco
            cursor.execute(f"insert into cliente(nome, rg, cpf, telefone) values('{nome}','{rg}','{cpf}','{telefone}')")
            bd.commit()
            print("")
            print("cliente cadastrado")

        except:
            print("")
            print('Erro no cadastro, por favor tente novamente')
    
    #Método que realiza um delete dentro do banco com base no id fornecido pelo usuario
    def delete(self,dado):
        try:
            #Comando que realiza o delete no banco
            cursor.execute(f"delete from cliente where idcliente = {dado}")
            bd.commit()
            print("")
            print("cliente deletado")
            
        except:
            print("")
            print("Este cliente nao existe")

    def update(self):

        try:
            cursor.execute(f"update cliente set nome = '{self.__nome}', rg = '{self.__rg}', cpf = '{self.__cpf}', telefone = '{self.__telefone}' where idCliente = {self.getId()};")
            bd.commit()
        except mysql.connector.Error as err:
            print(err)