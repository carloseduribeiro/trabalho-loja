from Classes.Produtos import Produtos

def listar_vendas():
    print("Iimprimir vendas")


def form_nova_venda():
    print("Form nova venda")


def listar_clientes():
    print("Imprimir clientes")


def form_cadastro_cliente():
    print("Form cadastro clientes")


def listar_produtos():
    print("Imprimir Produtos")
    try:
        Produtos.listar()
    except Exception as e:
        print("Erro" + str(e))
        print("Não foi possível listar")

def form_cadastro_produtos():
    try:
        nome_produto = input("Digite nome produto: ")
        preco_produto = input("Digite preço produto: ")
        Produtos.Cadastrar(nome_produto, preco_produto)

    except Exception as e:
        print("Erro: " + str(e))
        print("Produto não cadastrado!")

def listar_categorias():
    print("Exibir categorias")


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
        elif menu < 0 or menu > 7:
            print("Opção não existe! Tente novamente.")
        else:
            break

    except ValueError:
        print("Opção não existe! Tente novamente.")

print("Programa encerrado...")
