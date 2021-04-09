from Classes.Produtos import Produtos
from Classes.Categorias import Categorias
from Classes.Clientes import Clientes


def listar_vendas():
    print("Iimprimir vendas")


def form_nova_venda():
    print("Form nova venda")


def listar_clientes():
    print("Imprimir clientes")
    clientes = Clientes()
    try:
        clientes.listar()
    except Exception as e:
        print("Erro: " + str(e))
        print("Não foi possível listar os clientes !")


def form_cadastro_cliente():
    print("Form cadastro clientes")
    clientes = Clientes()
    try:
        clientes.codCliente = input("Digite o código do cliente: ")
        clientes.nomeCliente = input("Digite o nome: ")
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
    print("Imprimir Produtos")
    produtos = Produtos()
    try:
        produtos.listar()
    except Exception as e:
        print("Erro: " + str(e))
        print("Não foi possível listar!")


def form_cadastro_produtos():
    produtos = Produtos()
    listaCategorias = Categorias.listar()
    try:
        print(listaCategorias)
        print("Favor Selecionar uma categoria: ")
        produtos.codCategoria = input("Digite o código da categoria: ")
        for line in listaCategorias:
            if produtos.codCategoria in str(line).split(",")[0]:
                produtos.codProduto = input("Digite o codigo do produto: ")
                produtos.nomeProduto = input("Digite nome produto: ")
                produtos.precoProduto = input("Digite preço produto: ")
                produtos.cadastrar()
            else:
                raise Exception("Código categoria nao encontrado !")
    except Exception as e:
        print("Erro: " + str(e))
        print("Produto não cadastrado !")


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
              "1 - Apagar\n" +
              "2 - Cadastrar\n" +
              "3 - Editar\n" +
              "0 - Sair")

        try:
            opcao = int(input("Digite: "))

            if opcao == 1:
                try:
                    # Apaga a categoria selecionada:
                    id_categoria = int(input("Insira o id: "))
                    print(f"{'':=^30}")

                    if id_categoria in ids:
                        if Categorias('', id_categoria).apagar():
                            print("Categoria APAGADA com sucesso!")
                        else:
                            print("Categoria NÃO apagada.")
                    else:
                        print("Id não existe! Tente novamente.")
                except ValueError:
                    print("Id não existe! Tente novamente.")

            elif opcao == 2:
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

            elif opcao == 3:
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
1 - Hisórico de Vendas
2 - Nova Venda
3 - Clientes Cadastrados
4 - Cadastrar Cliente
5 - Produtos Cadastrados
6 - Cadastrar Produtos
7 - Categorias
0 - Sair
==============================""")
    menu = input("Digite opção: ")

    try:
        menu = int(menu)

        if menu == 1:
            listar_vendas()
        elif menu == 2:
            form_nova_venda()
        elif menu == 3:
            listar_clientes()
        elif menu == 4:
            form_cadastro_cliente()
        elif menu == 5:
            listar_produtos()
        elif menu == 6:
            form_cadastro_produtos()
        elif menu == 7:
            listar_categorias()
        elif menu == 99:
            deletar_produtos()
        elif menu == 98:
            deletar_clientes()
        # elif menu < 0 or menu > 7:
        #     print("Opção não existe! Tente novamente.")
        else:
            break
    except ValueError:
        print("Opção não existe! Tente novamente.")

print("Programa encerrado...")
