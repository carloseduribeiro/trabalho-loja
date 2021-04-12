from Classes.Produtos import Produtos
from Classes.Categorias import Categorias


def menu_produtos():
    opcao = int
    while opcao != 0:

        produtos = listar_produtos()

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
                id_categoria = int(input("Insira o id: "))

                if id_categoria == 0:
                    opcao = 0
                    break

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


def deletar_produtos():
    print("Deletar Produtos")
    produtos = Produtos()
    try:
        produtos.codProduto = input("Digite o código do produto: ")
        produtos.deletar()
    except Exception as e:
        print("Erro: " + str(e))
        print("Não foi possível excluir o produto!")


def listar_produtos() -> dict:
    categorias = {}

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

    return produtos




