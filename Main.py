import Produtos

menu = 0

while menu != 9:
    menu = input("Digite opção: "
                 "1 - Categorias")

    if menu == 1:
        produto = Produtos.Produto()
        produto.Cadastrar()