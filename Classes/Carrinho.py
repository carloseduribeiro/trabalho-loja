# coding=utf-8

class Carrinho:

    codigo = int
    codigo_produto = int
    quantidade = int

    def __init__(self, codigo = 0, codigo_produto = 0, quantidade=0):
        self.codigo_venda = codigo
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade

    def salvar(self):
        ultimo_codigo = 0
        # Percorre o arquivo para pegar o ultimo codigo cadastrado:
        # with open("banco/carrinho.txt", "r") as dados_banco:
        #     for car in dados_banco:
        #         print(car)
        #         ultimo_codigo = car.strip().split(";")[0]
        #     ultimo_codigo = int(ultimo_codigo) + 1
        #     self.codigo = ultimo_codigo

        # Adiciona um novo registro:
        with open("banco/carrinho.txt", "a+") as dados_banco:
            num_linhas = sum(1 for line in open("banco/carrinho.txt"))
            if num_linhas >= 1:
                dados_banco.writelines(f"\n{self.codigo_venda};{self.codigo_produto};{self.quantidade}")
            else:
                dados_banco.writelines(f"{self.codigo_venda};{self.codigo_produto};{self.quantidade}")

    # def apagar(self):
    #     produtos = []
    #
    #     if self.codigo > 0:
    #         # Salva os registros cadastrados em uma lista:
    #         with open("banco/carrinho.txt", "r") as dados_banco:
    #             produtos_banco = dados_banco.readlines()
    #
    #         # Salva os dados no banco:
    #         with open("banco/carrinho.txt", "w") as dados_banco:
    #             for i in range(len(produtos_banco)):
    #                 car = produtos_banco[i].strip().split(";")
    #                 if int(car[0]) != self.codigo:
    #                     car = str(';'.join(car))
    #                     car += "\n" if i != len(produtos_banco)-1 else ''
    #                     produtos.append(car)
    #             dados_banco.writelines(produtos)

