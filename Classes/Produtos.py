class Produtos:
    codProduto = int
    nomeProduto = str
    precoProduto = float
    codCategoria = int

    def __init__(self, codProduto=0, nomeProduto="", precoProduto=0, codCategoria = 0):
        self.codProduto = codProduto
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto
        self.codCategoria = codCategoria

    @staticmethod
    def listar():
        print("Cod | Descricao | Categoria | Preco")
        with open("banco/produtos.txt", "r") as produtos:
            for line in produtos:
                print(line.strip().split(","))

    def cadastrar(self):
        ultimo_codigo = 0

        if self.codProduto <= 0:
            with open("banco/produtos.txt", "r") as dados_banco:
                for cat in dados_banco:
                    ultimo_codigo = cat.strip().split(";")[0]
                ultimo_codigo = int(ultimo_codigo) + 1
                self.codProduto = ultimo_codigo
                num_linhas = sum(1 for line in open("banco/produtos.txt"))

            # Adiciona um novo registro:
            with open("banco/produtos.txt", "a+") as dados_banco:
                if num_linhas >= 1:
                    prod = f"\n{self.codProduto};{self.nomeProduto};{self.precoProduto};{self.codCategoria}"
                else:
                    prod = f"{self.codProduto};{self.nomeProduto};{self.precoProduto};{self.codCategoria}"

                dados_banco.write(prod)

        else:
            produtos = []
            # Salva os registros cadastrados em uma lista:
            with open("banco/produtos.txt", "r") as dados_banco:
                produtos_banco = dados_banco.readlines()
                num_linhas = sum(1 for line in open("banco/categorias.txt"))

            # Salva os dados no banco:
            with open("banco/produtos.txt", "w") as dados_banco:
                for line in range(len(produtos_banco)):
                    prod = produtos_banco[line].strip().split(";")
                    if int(prod[0]) == self.codProduto:
                        prod[1] = self.nomeProduto
                        prod[2] = str(self.precoProduto)
                        prod[3] = str(self.codCategoria)

                    if num_linhas >= 1 and line != 0:
                        prod = '\n' + ';'.join(prod)
                    else:
                        prod = ';'.join(prod)

                    dados_banco.write(prod)

    def deletar(self):
        with open("banco/produtos.txt", "r") as produtos:
            lines = produtos.readlines()
        with open("banco/produtos.txt", "w") as produtos:
            for line in lines:
                if line.split(";")[0] != str(self.codProduto):
                    produtos.write(line)
