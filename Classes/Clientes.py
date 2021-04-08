class Clientes:
    nomeCliente = str
    CPFCliente = str
    idadeCliente = int

    def __init__(self, nomeCliente="", CPFCliente="", idadeCliente=0):
        self.nomeCliente = nomeCliente
        self.CPFCliente = CPFCliente
        self.idadeCliente = idadeCliente

    @staticmethod
    def listar():
        print("Cod | Nome | CPF | Idade")
        with open("banco/clientes.txt", "r") as clientes:
            for line in clientes:
                print(tuple(line.strip().split(",")))

    def cadastrar(self):
        if self.codProduto.isdigit() and self.nomeProduto.isalpha() and self.precoProduto.isdigit() and self.codCategoria.isdigit():
            with open("banco/clientes.txt", "a") as clientes:
                clientes.write(self.nomeCliente + ", ")
                clientes.write(self.nomeProduto + ", ")
                clientes.write(self.codCategoria + ", ")
                clientes.write(self.precoProduto + " R$\n")
        else:
            raise Exception("Favor digitar campos válidos !")

    def deletar(self):
        print("")