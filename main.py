from models.funcionario import Funcionario
from models.cliente import Cliente
from models.veiculo import Veiculo
from ui.msg import Mensagens
from models.estoque import Estoque
from models.servico import Servico
import time
from utils.updateInput import valorInput


if __name__ == "__main__":
    cliente = Cliente("", "", "", "", 0)
    funcionario = Funcionario("", "", "", "",0)
    veiculo = Veiculo("", "", "", 1)
    estoque = Estoque("",0,0,0)
    servico = Servico(0,0,0,0,0,0,0,0,0)

    while True:
        Mensagens.inicio()
        oprg = input("")
        match oprg:
            # funcionario 
            case "1":
                    while True:
                        Mensagens.caso1_Inicio()
                        opr = input("")
                        match opr:
                            
                            # select - consultar funcionario
                            case "1":
                                print("")
                                dado = input("Insira a matricula do funcionario: ")
                                funcionario.select(dado)
                                time.sleep(2)

                            # insert - inserir funcionario
                            case "2":
                                print("")
                                nome = input("Insira o nome do funcionario: ")
                                rg = input("Insira o rg do funcionario: ")
                                cpf = input("Insira o cpf do funcionario: ")
                                telefone = input("Insira o telefone do funcionario: ")
                                funcionario.insert(nome, rg, cpf, telefone)
                                time.sleep(2)

                            # deletar
                            case "3":
                                dado = input("Insira matricula do funcionario: ")
                                print("")
                                funcionario.delete(dado)

                            # atualizar
                            case "4":
                                pass

                            case "0":
                                break

            # cliente
            case "2":
                 while True:

                        Mensagens.caso2_Inicio()
                        opr = input("")
                        match opr:

                            # consultar - select
                            case "1":
                                print("")
                                dado = input("Insira a matricula do cliente: ")
                                cliente.select(dado)
                                time.sleep(2)

                    
                            # cadastrar - insert
                            case "2":
                                print("")
                                nome = input("Insira o nome do cliente: ")
                                rg = input("Insira o rg do cliente: ")
                                cpf = input("Insira o cpf do cliente: ")
                                telefone = input("Insira o telefone do cliente: ")
                                cliente.insert(nome, rg, cpf, telefone)
                                time.sleep(2)

                            # excluir - delete
                            case "3":
                                dado = input("Insira matricula do cliente: ")
                                print("")
                                cliente.delete(dado)

                            # atualizar
                            case "4":
                                dado = input("Insira o ID do cliente: ")
                                cliente.select(dado)
                                nome = valorInput("Nome",cliente.getNome())
                                rg = valorInput("RG",cliente.getRg())
                                cpf = valorInput("CPF",cliente.getCpf())
                                telefone = valorInput("Telefone",cliente.getTelefone())
                                cliente = Cliente(nome,rg,cpf,telefone,dado)
                                cliente.update()

                            case "0":
                                break
            
            # veiculo
            case "3":
                while True:

                    Mensagens.caso3_Inicio()
                    opr = input()

                    match opr:

                        # consultar - insert
                        case "1":
                            print('consultar')
                            veiculo.select(int(input('Digite o identificador do veiculo: ')))

                        # cadastrar - insert 
                        case "2":
                            print('inserir')
                            marca = input("Digite a marca do veiculo: ")
                            modelo = input("Digite o modelo do veiculo: ")
                            placa = input("Digite a placa do veiculo: ")
                            veiculo.inserir(modelo,marca,placa)

                        # excluir - delete 
                        case "3":
                            print('excluir')
                            veiculo.delete(int(input('Digite o id do veiculo: ')))

                        # alterar - update
                        case "4":
                            print("Alterar")
                            dado = int(input("Digite o id do Veiculo: "))
                            veiculo.select(dado)
                            marca = valorInput("Marca",veiculo.getMarca())
                            modelo = valorInput("Modelo",veiculo.getModelo())
                            placa = valorInput("Placa",veiculo.getPlaca())
                            veiculo = Veiculo(marca,modelo,placa,dado)
                            veiculo.update()

                        case "0":
                            break

                        case _:
                            print('Operação invalida')
                            break


            
            # estoque
            case "4":
                while True:
                    Mensagens.caso4_Inicio()
                    opr = input()
                    match opr:

                        case "1":
                            #consultar 
                            dado = int(input("Digite o Id da peça"))
                            estoque.select(dado)
                            estoque.exibir()

                        case "2":
                            #inserir 
                            print('Inserir')
                            nome = input("Digite o nome da peça")
                            valor = float(input("Digite o valor da peça"))
                            qtd = int(input("Digite a quantidade de peças"))
                            estoque.insert(nome,valor,qtd)

                        case "3":
                            # deletar
                            print("Deletar")
                            dado = int(input("Digite o ID da peça: "))
                            estoque.delete(dado)

                        case "4":
                            dado = int(input("digite o id da peça: "))
                            estoque.select(dado)
                            nome = valorInput("Nome",estoque.getNome())
                            qtd = valorInput("Quantidade",estoque.getQtd())
                            valor = valorInput("Valor",estoque.getValor())
                            estoque = Estoque(dado,nome,valor,qtd)
                            estoque.update()
                
            # servico
            case "5":
                while True:
                    Mensagens.caso5_Inicio()
                    opr = input()
                    match opr:
                        
                        case "1":
                            #consultar 
                            dado = int(input("Digite o id do pedido: "))
                            servico.select(dado)
                            servico.exibir()
                            
                        case "2":
                            # inserir  
                            descricao = input("Digite a descrição do pedido: ")
                            prazo = input("Digite a data do prazo do pedido: ")
                            valor = float(input("Digite o valor do pedido: "))
                            dataInicio = input("Digite a data de cadastro do pedido: ")
                            idCliente = int(input("Digite o id do cliente: "))
                            idEstoque = int(input("Digite o id da peça do estoque: "))
                            idVeiculo = int(input("Digite o id do veiculo: "))
                            idFuncionario = int(input("Digite o id do Funcionario: "))
                            servico.insert(descricao,prazo,valor,dataInicio,idCliente,idEstoque,idVeiculo,idFuncionario)
                            servico.exibir()
                        
                        case "3":
                            # deletar 
                            dado = int(input("Digite o id do pedido: "))
                            servico.delete(dado)
                        
                        case "4":
                            # update
                            dado = int(input("digite o id do serviço: "))
                            servico.select(dado)
                            descricao = valorInput("Descrição",servico.getDescricao())
                            prazo = valorInput("Prazo",servico.getPrazo())
                            valor = valorInput("Valor",servico.getValor())
                            dataInicio = valorInput("Data Cadastro",servico.getDataCadastro())
                            idCliente = valorInput("Id do cliente",servico.getIdCliente())
                            idEstoque = valorInput("Id da peça",servico.getIdEstoque())
                            idVeiculo = valorInput("Id do veiculo",servico.getIdVeiculo())
                            idFuncionario = valorInput("Id do funcionario",servico.getIdfuncionario())
                            servico = Servico(dado,descricao,prazo,valor,dataInicio,idCliente,idEstoque,idVeiculo,idFuncionario)
                            servico.update()
                        case "0":
                            break
                
            case "0":

                print("")
                print("Saindo do sistema")
                for i in range(3):
                    time.sleep(1)
                    print(".")
                
                time.sleep(1)
                print("Saida efetuada")
                time.sleep(1)


                break