from models.pessoa import *

class Funcionario(Pessoa):
    def __init__(self, nome, rg, cpf, telefone,id):
        super().__init__(nome, rg, cpf, telefone,id)

    def exibir(self):
        return print(f"Nome: {self.__nome}, Especialidade: {self.__servico},ID:{self.__id} , RG: {self.__rg}, CPF:{self.__cpf}, Telefone: {self.__telefone}")

    #Método que seleciona o funcionario com base no id fornecido pelo usuario
    def select(self, dado):

        try:
            #comando para a execução de um select dentro do banco de dados
            cursor.execute(f"select idfuncionario,nome,rg,cpf,telefone from funcionario where idfuncionario = {dado};")
            #função print das informações cadastradas no banco
            for func in cursor:
                print("Segue abaixo os dados do funcionario:")
                print("")
                print(f"Matricula: {func[0]}")
                print(f"Nome: {func[1]}")
                print(f"Rg: {func[2]}")
                print(f"Cpf: {func[3]}")
                print(f"Telefone: {func[4]}")
                
        except mysql.connector.Error as err:
            print(err)

    #Método que realiza um insert dentro do banco de dados com as informações fornecidas pelo usuario
    def insert(self,nome, rg, cpf, telefone):
        try:
            #comando que executa o insert no banco
            cursor.execute(f"insert into funcionario(nome, rg, cpf, telefone) values('{nome}','{rg}','{cpf}','{telefone}');")
            bd.commit()
            print("")
            print("Funcionaro cadastrado")

        except mysql.connector.Error as erro:
            print("")
            print('Erro no cadastro, por favor tente novamente')
            print(erro)
    
    #Método que realiza um delete dentro do banco com base no id fornecido pelo usuario
    def delete(self,dado):

        try: 
            #Comando que realiza o delete no banco
            cursor.execute(f"delete from funcionario where idfuncionario = {dado}")
            bd.commit()
            print("")
            print("Funcionaro deletado")  
        except mysql.connector.Error as erro :
            print("")
            print("Este funcionario nao existe")
            print(erro)

    def update(self):
        try:
            pass
        except:
            pass