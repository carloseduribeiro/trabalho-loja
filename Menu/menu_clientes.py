from Classes.Clientes import Clientes


def listar_clientes():
    clientes = Clientes()
    opcao = 0

    clientList = {}
    while opcao != 9:

        try:
            with open("banco/clientes.txt", "r") as dados_banco:
                for cli_banco in dados_banco:
                    cli = cli_banco.strip().split(';')
                    clientList[cli[0]] = list(cli[1:5])

            print(f"{' Clientes ':=^30}")
            print(f"{'Id:':<4} {'Nome:':<20} {'Senha:':<10} {'CPF:':<10} {'Idade:':<10}")

            for cod, cli in clientList.items():
                print(f"{cod:<4}{cli[0]:<25}{cli[1]:<10}{cli[2]:<10}{cli[3]:<10}")

        except Exception as e:
            print("Erro: " + str(e))
            print("Não foi possível listar os clientes !")

        print(f"{'':=^30}\n" +
              "Escolha uma opção:\n" +
              "1 - Cadastrar\n"+
              "2 - Editar\n"
              "3 - Apagar\n"+
              "0 - Sair")

        opcao = int(input("Digite: "))

        if opcao == 1:
            form_cadastro_cliente()
        elif opcao == 2:
            alterar_cliente()
        elif opcao == 3:
            deletar_clientes()
        else:
            break


def alterar_cliente():
    print("Alterar Clientes")
    clientes = Clientes()
    try:
        clientes.codCliente = int(input("Digite o codigo do cliente: "))
        clientes.nomeCliente = input("Digite o nome: ")
        clientes.senhaCliente = input("Digite a senha: ")
        clientes.CPFCliente = input("Digite o CPF: ")
        clientes.idadeCliente = input("Digite a idade: ")
        clientes.cadastrar()
    except Exception as e:
        print("Erro: " + str(e))


def form_cadastro_cliente():
    print("Form cadastro clientes")
    clientes = Clientes()
    try:
        clientes.nomeCliente = input("Digite o nome: ")
        clientes.senhaCliente = input("Digite a senha: ")
        clientes.CPFCliente = input("Digite o CPF: ")
        clientes.idadeCliente = input("Digite a idade: ")
        clientes.cadastrar()
    except Exception as e:
        print("Erro: " + str(e))
        print("Não foi possível cadastrar os clientes !")


def deletar_clientes():
    print("Deletar clientes")
    clientes = Clientes()
    try:
        clientes.codCliente = input("Digite o código do cliente: ")
        clientes.deletar()
    except Exception as e:
        print("Erro: " + str(e))
        print("Não foi possível deletar os clientes !")
