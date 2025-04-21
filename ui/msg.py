# class para mensagens dos menus exibidas no main do sistema
class Mensagens():
    
    # exibidas assim que o programa for iniciado
    def inicio():
        print("")
        print("Bem vindo ao sistema de gerenciamento")
        print("Qual aba você deseja acessar?")
        print("")
        print("1 - Funcionarios")
        print("2 - Clientes")
        print("3 - Veiculo")
        print("4 - Estoque")
        print("5 - Pedido")
        print("0 - Sair do sistema")
        print("")

    # exibido caso o usuario escolha a aba de funcionarios
    def caso1_Inicio():
        print("")
        print("Você está na aba de funcionarios:")
        print("Selecione qual ação você deseja executar:")
        print("")
        print("1 - Consultar funcionarios")
        print("2 - Inserir funcionarios")
        print("3 - Excluir funcionarios")
        print("0 - Sair da aba")
        print("")
    
    # exibido caso o usuario escolha a aba de clientes
    def caso2_Inicio():
        print("")
        print("Você está na aba de clientes:")
        print("Selecione qual ação você deseja executar:")
        print("")
        print("1 - Consultar clientes")
        print("2 - Inserir clientes")
        print("3 - Excluir clientes")
        print("0 - Sair da aba")
        print("")

    # exibido caso o usuario escolha a aba veiculos
    def caso3_Inicio():
        print("")
        print("Você está na aba de veiculos:")
        print("Selecione qual ação você deseja executar:")
        print("")
        print("1 - Consultar veiculos")
        print("2 - Inserir veiculos")
        print("3 - Excluir veiculos")
        print("0 - Sair da aba")
        print("")
    # exibido caso o usuario escolha a aba estoque   
    def caso4_Inicio():
        print("")
        print("Você está na aba de estoque:")
        print("Selecione qual ação você deseja executar:")
        print("")
        print("1 - Consultar estoque")
        print("2 - Inserir item no estoque")
        print("3 - Excluir item do estoque")
        print("4 - atualizar informações de itens")
        print("0 - Sair da aba")
        print("")

    def caso5_Inicio():
        print("")
        print("Você está na aba de pedidos:")
        print("Selecione qual ação você deseja executar:")
        print("")
        print("1 - Consultar pedido")
        print("2 - Inserir pedido no sistema")
        print("3 - Excluir pedido no sistema")
        print("4 - atualizar informações do pedido")
        print("0 - Sair da aba")
        print("")