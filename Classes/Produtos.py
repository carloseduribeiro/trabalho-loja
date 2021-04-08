class Produtos:

    # def __init__(self, nome):
    #     self.nome = nome

    def cadastrar(self, codProduto, nomeProduto, precoProduto):
        with open("banco/produtos.txt", "a") as produtos:
            produtos.write(codProduto + ",")
            produtos.write(nomeProduto + ",")
            produtos.write(precoProduto + "\n")

    def listar(self, codProduto):
        with open("banco/produto.txt", "r") as produtos:
            print("")

