class Produtos:
    codProduto = int
    nomeProduto = str
    precoProduto = float
    codCategoria = int

    def __init__(self, codProduto=0, nomeProduto="", precoProduto=0, codCategoria = 0):
        self.codProduto = codProduto
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto

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

            # Adiciona um novo registro:
            with open("banco/produtos.txt", "a") as dados_banco:
                num_linhas = sum(1 for line in open("banco/produtos.txt"))
                if num_linhas >= 1:
                    dados_banco.writelines(
                        f"\n{self.codProduto};{self.nomeProduto};{self.precoProduto};{self.codCategoria}")
                else:
                    dados_banco.writelines(
                        f"{self.codProduto};{self.nomeProduto};{self.precoProduto};{self.codCategoria}")

        else:
            produtos = []
            # Salva os registros cadastrados em uma lista:
            with open("banco/produtos.txt", "r") as dados_banco:
                produtos_banco = dados_banco.readlines()

            # Salva os dados no banco:
            with open("banco/produtos.txt", "w") as dados_banco:
                for line in produtos_banco:
                    cat = line.strip().split(";")
                    if int(cat[0]) == self.codProduto:
                        cat[1] = self.nomeProduto
                        cat[2] = self.precoProduto
                        cat[3] = str(self.codCategoria)
                    cat = ';'.join(cat)
                    produtos.append(cat)

                dados_banco.writelines(produtos)

    def deletar(self):
        with open("banco/produtos.txt", "r") as produtos:
            lines = produtos.readlines()
        with open("banco/produtos.txt", "w") as produtos:
            for line in lines:
                if line.split(";")[0] != str(self.codProduto):
                    produtos.write(line)