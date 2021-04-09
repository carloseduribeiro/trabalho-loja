class Clientes:

    codCliente = int
    nomeCliente = str
    CPFCliente = str
    idadeCliente = int

    def __init__(self, codCliente="", nomeCliente="", CPFCliente="", idadeCliente=0):
        self.codCliente = codCliente
        self.nomeCliente = nomeCliente
        self.CPFCliente = CPFCliente
        self.idadeCliente = idadeCliente

    @staticmethod
    def listar():
        print("Cod | Nome | CPF | Idade")
        with open("banco/clientes.txt", "r") as clientes:
            for line in clientes:
                print(tuple(line.strip().split(";")))

    def cadastrar(self):
        if self.codCliente.isdigit() and self.nomeCliente.isalpha() and self.CPFCliente.isdigit() and self.idadeCliente.isdigit():
            with open("banco/clientes.txt", "a") as clientes:
                clientes.write(self.codCliente + ";")
                clientes.write(self.nomeCliente + ";")
                clientes.write(self.CPFCliente + ";")
                clientes.write(self.idadeCliente + "\n")
        else:
            raise Exception("Favor digitar campos válidos !")

    def deletar(self):
        if self.codCliente.isdigit():
            with open("banco/clientes.txt", "r") as clientes:
                lines = clientes.readlines()
            with open("banco/clientes.txt", "w") as clientes:
                for line in lines:
                    if line.split(";")[0] != str(self.codCliente):
                        clientes.write(line)
        else:
            raise Exception("Favor digitar um código válido !")
