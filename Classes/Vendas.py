# coding=utf-8

class Vendas:

    codigo_venda = int
    cpf_cliente = int
    produtos = {}

    def __init__(self, cpf_cliente: str):
        self.cpf_cliente = cpf_cliente

        # Preocura o codigo da ultima venda:
        with open("banco/vendas.txt", "r") as banco:
            ultimo_codigo = 0
            for line in banco:
                ultimo_codigo = line.strip().split(";")[0]
            ultimo_codigo = int(ultimo_codigo) + 1
            self.codigo_venda = ultimo_codigo

    def adicionar_produto(self, codigo_produto, quantidade, vlr_unitario, nome):
        self.produtos[codigo_produto] = [self.codigo_venda, quantidade, vlr_unitario, nome]

    def remover_produtos(self, codigo_produto, quantidade):
        if quantidade < self.produtos[codigo_produto][1]:
            self.produtos[codigo_produto][1] -= quantidade
        else:
            self.produtos.pop(codigo_produto)

    def listar_produtos(self):
        return self.produtos

    # def finalizar_venda(self):
