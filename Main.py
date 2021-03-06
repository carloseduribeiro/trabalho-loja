from Classes.Produtos import Produtos
from Classes.Categorias import Categorias
from Classes.Clientes import Clientes


def listar_vendas():
    print("Iimprimir vendas")


def form_nova_venda():
    print("Form nova venda")


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


def deletar_produtos():
    print("Deletar Produtos")
    produtos = Produtos()
    try:
        produtos.codProduto = input("Digite o código do produto: ")
        produtos.deletar()
    except Exception as e:
        print("Erro: " + str(e))
        print("Não foi possível excluir o produto!")


def listar_produtos():
    opcao = int
    categorias = {}

    while opcao != 0:

        # Armazena um dicionario de categorias:
        with open("banco/categorias.txt", "r") as categorias_banco:
            for line in categorias_banco:
                cat = line.strip().split(';')
                categorias[cat[0]] = cat[1]

        produtos = {}
        with open("banco/produtos.txt", "r") as dados_banco:
            for prod_banco in dados_banco:
                prod = prod_banco.strip().split(';')
                produtos[prod[0]] = list(prod[1:4])

        # Imprime os produtos cadastradas:
        print(f"\n{' PRODUTOS ':=^30}")

        print(f"{'Id:':<4} {'Nome:':<25} {'Preco:':<15} {'Categoria:':<15}")
        for cod, prod in produtos.items():
            if len(prod[2]) == 0:
                print(f"{cod:<4} {prod[0]:<25} R$ {prod[1]:<10} {'Sem categoria':<15}")
            else:
                print(f"{cod:<4} {prod[0]:<25} R$ {prod[1]:<10} {categorias[prod[2]]:<15}")

        # Imprime o menu:
        print(f"{'':=^30}\n" +
              "Escolha uma opção:\n" +
              "1 - Cadastrar\n" +
              "2 - Editar\n" +
              "3 - Apagar\n" +
              "0 - Sair")

        try:
            opcao = int(input("Digite: "))

            if opcao == 1:
                # Exibe o form de cadastro de produtos:
                form_cadastro_produtos()

            elif opcao == 2:
                # Cadastra uma nova categoria:
                print(f"\n{' EDITAR PRODUTO ':=^30}")
                cod_produto = int(input("Insira o código: "))
                print(f"{'':=^30}")

                if str(cod_produto) not in list(produtos.keys()):
                    print("Produto não existe! Tente novamente.")
                else:
                    nome_produto = input("Insira o nome: ")
                    preco_produto = float(input("Insira o preço: "))
                    cod_categoria = int(input("Insira o codigo da categoria: "))
                    Produtos(cod_produto, nome_produto, preco_produto, cod_categoria).cadastrar()

            elif opcao == 3:
                try:
                    # Apaga o produto selecionado:
                    id_produto = int(input("Insira o id: "))
                    print(f"{'':=^30}")

                    if str(id_produto) in list(produtos.keys()):
                        # Produtos('', id_produto).deletar()
                        print("Produto apagado (REVISAR)")
                    else:
                        print("Id não existe! Tente novamente.")
                except ValueError:
                    print("Id não existe! Tente novamente.")


            elif opcao < 0 or opcao > 3:

                print("Opção não existe! Tente novamente.")
            else:
                break
        except ValueError:
            print("Opção não existe! Tente novamente.")

def form_cadastro_produtos():
    opcao = int
    ids_categoria = []
    while opcao != 0:
        # Imprime as categorias cadastradas:
        print(f"\n{' CADASTRO DE PRODUTO ':=^30}")
        print("Selecione uma categoria:")
        print(f"{'Id:':<4}\t{'Nome:'}")
        for cat in Categorias.listar():
            print(f"{cat[0]:<4}\t{cat[1]}")
            ids_categoria.append(int(cat[0]))

        id_categoria = int
        while id_categoria != 0:
            try:
                print(f"{'':-^30}")
                print("Digite 0 para cancelar...")
                # Apaga a categoria selecionada:
                # id_categoria = int(input("Insira o id: "))
                #
                # if id_categoria == 0:
                #     opcao = 0
                #     break

                print(f"{'':=^30}")

                if id_categoria not in ids_categoria:
                    print("Id não existe! Tente novamente.")
                else:
                    # Cadastra um novo produto:
                    categoria_produto = id_categoria

                    while True:
                        nome_produto = input("Digite nome produto: ")
                        if len(nome_produto) < 2:
                            print("O nome deve ter pelo menos 3 caracteres.")
                        else:
                            break

                    while True:
                        try:
                            preco_produto = float(input("Digite preço produto: "))
                            break
                        except ValueError:
                            print("Valor inserido inválido! Tente novamente.")

                    # Cadastra o produto no Banco:
                    Produtos(0, nome_produto, preco_produto, categoria_produto).cadastrar()
                    print("Produto cadastrado")
                    break
            except ValueError:
                print("Id não existe! Tente novamente.")
        break


def listar_categorias():
    opcao = 0
    # Armazena a lista de ids e nomes das categorias cadastradas:
    ids = []
    nomes_categoria = []
    while opcao != 9:
        # Imprime as categorias cadastradas:
        print(f"\n{' CATEGORIAS ':=^30}")
        print(f"{'Id:':<4}\t{'Nome:'}")
        for cat in Categorias.listar():
            print(f"{cat[0]:<4}\t{cat[1]}")
            ids.append(int(cat[0]))
            nomes_categoria.append(cat[1])
        # Imprime o menu:
        print(f"{'':=^30}\n" +
              "Escolha uma opção:\n" +
              "1 - Cadastrar\n" +
              "2 - Editar\n" +
              "3 - Apagar\n" +
              "0 - Sair")
        try:
            opcao = int(input("Digite: "))

            if opcao == 1:
                # Cadastra uma nova categoria:
                print(f"\n{' NOVA CATEGORIA ':=^30}")
                nome_categoria = input("Insira o nome: ")
                print(f"{'':=^30}")

                # Verifica se já existe uma categoria com o mesmo nome:
                if nome_categoria not in nomes_categoria:
                    Categorias(nome_categoria).salvar()
                    print("Categoria cadastrada.")
                else:
                    print("Categoria NÃO cadastrada!")
                    print("Categoria já existe.\n")

            elif opcao == 2:
                # Edita uma categoria existente:
                print(f"\n{' EDITAR CATEGORIA ':=^30}")
                try:
                    id_categoria = int(input("Insira o id: "))
                    print(f"{'':=^30}")

                    if id_categoria in ids:
                        nome_categoria = input("Insira o novo nome: ")
                        # Salva as alterações
                        Categorias(nome_categoria, id_categoria).salvar()
                    else:
                        print("Id não existe! Tente novamente.")
                except ValueError:
                    print("Id inserido não existe!")

            elif opcao == 3:
                try:
                    # Apaga a categoria selecionada:
                    id_categoria = int(input("Insira o id: "))
                    print(f"{'':=^30}")

                    if id_categoria in ids:
                        Categorias('', id_categoria).apagar()
                        print("Categoria APAGADA!")
                    else:
                        print("Id não existe! Tente novamente.")
                except ValueError:
                    print("Id não existe! Tente novamente.")

            elif opcao < 0 or opcao > 3:
                print("Opção não existe! Tente novamente.")

            else:
                break
        except ValueError:
            print("Opção não existe! Tente novamente.")


# MENU PRINCIPAL:
menu = 0

while menu != 9:
    print("""
============ LOJA ============
1 - Nova Venda
2 - Hisórico de Vendas
3 - Clientes
4 - Produtos
5 - Categorias
0 - Sair
==============================""")
    menu = input("Digite opção: ")

    try:
        menu = int(menu)

        if menu == 1:
            form_nova_venda()
        elif menu == 2:
            listar_vendas()
        elif menu == 3:
            listar_clientes()
        elif menu == 4:
            listar_produtos()
        elif menu == 7:
            listar_categorias()
        elif menu < 0 or menu > 7:
            print("Opção não existe! Tente novamente.")
        else:
            break
    except ValueError:
        print("Opção não existe! Tente novamente.")

print("Programa encerrado...")
