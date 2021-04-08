import Produtos

menu = 0

while menu != 9:
    menu = input("Digite opção: \n"
                 "1 - Cadastrar Produtos:\n")

    # Cadastro de produtos #
    if menu == "1":
        produto = Produtos.Produto()
        try:
            nomeProduto = input("Digite nome produto:\n")
            precoProduto = input("Digite preço produto:\n")
            produto.Cadastrar(nomeProduto, precoProduto)
        except Exception as e:
            print(e)