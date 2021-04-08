class Produtos:
    codProduto = int
    nomeProduto = str
    preccProduto = float

    def __init__(self, codProduto="0", nomeProduto="", precoProduto="0"):
        self.codProduto = codProduto
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto

    @staticmethod
    def listar():
        print("Cod | Descricao | Preco")
        with open("banco/produtos.txt", "r") as produtos:
            for line in produtos:
                print(tuple(line.strip().split(",")))

    def cadastrar(self):
        if self.codProduto.isdigit() and self.nomeProduto.isalpha() and self.precoProduto.isdigit():
            with open("banco/produtos.txt", "a") as produtos:
                produtos.write(self.codProduto + ", ")
                produtos.write(self.nomeProduto + ", ")
                produtos.write(self.precoProduto + " R$\n")
        else:
            raise Exception("Favor digitar campos válidos !")

    def deletar(self):
        if self.codProduto.isdigit():
            with open("banco/produtos.txt", "r") as produtos:
                lines = produtos.readlines()
            with open("banco/produtos.txt", "w") as produtos:
                for line in lines:
                    if line.split(",")[0] != str(self.codProduto):
                        produtos.write(line)
        else:
            raise Exception("Favor digitar um código válido")
