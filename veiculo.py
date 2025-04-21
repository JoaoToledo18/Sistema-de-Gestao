from id import *

class Veiculo(Id):
    def __init__(self,marca, modelo, placa, id):
        super().__init__(id)
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getPlaca(self):
        return self.__placa

    # funcao de exibir os valores do objeto
    def exibir(self):
        return print(f"Placa: {self.__placa},ID:{self.__id} , Marca: {self.__marca}, Modelo:{self.__modelo}")

    # funcao responsavel por executar um select no banco com base em um id
    def select(self, dado):
        try:   
            cursor.execute(f"select marca, modelo, placa from veiculo where idVeiculo = {dado}")
            
            # monta o objeto e logo em seguida exibe os dados
            for i in cursor:
                self.__marca = i[0]
                self.__modelo = i[1]
                self.__placa = i[2]

        except:
            print("Esse veiculo não existe")
        

    # funcao de inserir dados no banco utilizando os atributos passados
    def inserir(self, modelo, marca, placa):
        try:
            cursor.execute(f"insert into veiculo(marca, modelo, placa) values ('{marca}','{modelo}','{placa}')")
            bd.commit()
            print("Veiculo Cadastrado")
        except:
            print("Veiculo não cadastrado")

    # metodo de deletar um veiculo no banco de dados       
    def delete(self,dado):
        try:
            cursor.execute(f"delete from veiculo where idVeiculo = {dado}")
            bd.commit()
            print('Veiculo excluido')
        except:
            print('Veiculo não excluido')

    def update(self):
        try:
            cursor.execute(f"update veiculo set marca = '{self.__marca}', modelo = '{self.__modelo}', placa = '{self.__placa}' where idVeiculo = {self.getId()};")
            bd.commit()
        except mysql.connector.Error as err:
            print(err)