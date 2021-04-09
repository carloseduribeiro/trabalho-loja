class Clientes:

    codCliente = int
    nomeCliente = str
    CPFCliente = str
    idadeCliente = int

    def __init__(self, codCliente=0, nomeCliente="", CPFCliente="", idadeCliente=0):
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
        ultimo_codigo = 0

        if self.codCliente <= 0:
            with open("banco/clientes.txt", "r") as dados_banco:
                for cat in dados_banco:
                    ultimo_codigo = cat.strip().split(";")[0]
                ultimo_codigo = int(ultimo_codigo) + 1
                self.codCliente = ultimo_codigo

            # Adiciona um novo registro:
            with open("banco/clientes.txt", "a") as dados_banco:
                num_linhas = sum(1 for line in open("banco/clientes.txt"))
                if num_linhas >= 1:
                    dados_banco.writelines(f"\n{self.codCliente};{self.nomeCliente};{self.CPFCliente};{self.idadeCliente}")
                else:
                    dados_banco.writelines(f"{self.codCliente};{self.nomeCliente};{self.CPFCliente};{self.idadeCliente}")

        else:
            clientes = []
            # Salva os registros cadastrados em uma lista:
            with open("banco/clientes.txt", "r") as dados_banco:
                clientes_banco = dados_banco.readlines()

            # Salva os dados no banco:
            with open("banco/clientes.txt", "w") as dados_banco:
                for line in clientes_banco:
                    cat = line.strip().split(";")
                    if int(cat[0]) == self.codCliente:
                        cat[1] = self.nomeCliente
                        cat[2] = self.CPFCliente
                        cat[3] = str(self.idadeCliente)
                    cat = ';'.join(cat)
                    clientes.append(cat)

                dados_banco.writelines(clientes)

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
