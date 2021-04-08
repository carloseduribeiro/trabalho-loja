from Classes.Produtos import Produtos

def listar_vendas():
    print("Iimprimir vendas")


def form_nova_venda():
    print("Form nova venda")


def listar_clientes():
    print("Imprimir clientes")


def form_cadastro_cliente():
    print("Form cadastro clientes")

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
    try:
        produtos.codProduto = input("Digite o codigo do produto: ")
        produtos.nomeProduto = input("Digite nome produto: ")
        produtos.precoProduto = input("Digite preço produto: ")
        produtos.cadastrar()
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
        elif menu == 99:
            deletar_produtos()
        # elif menu < 0 or menu > 7:
        #     print("Opção não existe! Tente novamente.")
        else:
            break

    except ValueError:
        print("Opção não existe! Tente novamente.")

print("Programa encerrado...")
