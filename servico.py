from id import *

class Servico(Id):

    def __init__(self, id,descr,prazo,valor,dataCadastr,idCliente,idEstoque,idVeiculo,idFunc):
        super().__init__(id)
        self.__descricao = descr
        self.__prazo = prazo
        self.__valor = valor
        self.__dataCadastro = dataCadastr
        self.__idEstoque = idEstoque
        self.__idVeiculo = idVeiculo
        self.__idFuncionario = idFunc
        self.__idCliente = idCliente

    def getDescricao(self):
        return self.__descricao
    def getPrazo(self):
        return self.__prazo
    def getValor(self):
        return self.__valor
    def getDataCadastro(self):
        return self.__dataCadastro
    def getIdEstoque(self):
        return self.__idEstoque
    def getIdVeiculo(self):
        return self.__idVeiculo
    def getIdfuncionario(self):
        return self.__idFuncionario
    def getIdCliente(self):
        return self.__idCliente    

    def exibir(self):
        
        return print(f"Descrição: {self.__descricao}, ID: {self.getId()},Data Cadastro: {self.__dataCadastro}, Prazo: {self.__prazo}, Valor: {self.__valor}")

    def select(self,dado):
        
        try:
            cursor.execute(f"select idPedido,descricao,prazo,valor,dataCadastro,Cliente_idCliente,estoque_idEstoque,Veiculo_idVeiculo,funcionario_idFuncionario from pedido where idPedido = {dado};")
            for pedido in cursor:
                self.setId(pedido[0])
                self.__descricao = pedido[1]
                self.__prazo = pedido[2]
                self.__valor = pedido[3]
                self.__dataCadastro = pedido[4]
                self.__idCliente = pedido[5]
                self.__idEstoque = pedido[6]
                self.__idVeiculo = pedido[7]
                self.__idFuncionario = pedido[8]
        except mysql.connector.Error as err:
            print(err)


    # inserir
    def insert(self,descricao,prazo,valor,dataInicio,idCliente,idEstoque,idVeiculo,idFuncionario):
        cursor.execute(f"insert into pedido(descricao,prazo,valor,dataCadastro,Cliente_idCliente,estoque_idEstoque,Veiculo_idVeiculo,funcionario_idFuncionario) values ('{descricao}','{prazo}',{valor},'{dataInicio}',{idCliente},{idEstoque},{idVeiculo},{idFuncionario});")
        bd.commit()
        print("Pedido cadastrado")

    # alterar
    def update(self):
        try:
            cursor.execute(f"update pedido set descricao = '{self.__descricao}',prazo = '{self.__prazo}', valor = {self.__valor}, dataCadastro = '{self.__dataCadastro}',Cliente_idCliente = {self.__idCliente}, estoque_idEstoque = {self.__idEstoque},  Veiculo_idVeiculo = {self.__idVeiculo}, funcionario_idFuncionario = {self.__idFuncionario}  where idPedido = {self.getId()};")
            bd.commit()
        except mysql.connector.Error as err:
            print(err)

    # deletar
        
    def delete(self,dado):

        try:
            cursor.execute(f"delete from pedido where idPedido ={dado}")
            bd.commit()
        except mysql.connector.Error as err:
            print(err)