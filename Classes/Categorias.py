# coding: latin-1

class Categorias:

    codigo = int
    nome = str

    def __init__(self, nome: str, codigo=0):
        self.codigo = codigo
        self.nome = nome

    def salvar(self):
        ultimo_codigo = 0
        # Caso o usuário não informe o código, cadastra um novo registro:
        if self.codigo <= 0:
            # Percorre o arquivo para pegar o ultimo codigo cadastrado:
            with open("banco/categorias.txt", "r") as dados_banco:
                for cat in dados_banco:
                    ultimo_codigo = cat.strip().split(";")[0]
                ultimo_codigo = int(ultimo_codigo) + 1
                self.codigo = ultimo_codigo

            # Adiciona um novo registro:
            with open("banco/categorias.txt", "a+") as dados_banco:
                num_linhas = sum(1 for line in open("../banco/categorias.txt"))
                if num_linhas >= 1:
                    dados_banco.writelines(f"\n{self.codigo};{self.nome}")
                else:
                    dados_banco.writelines(f"{self.codigo};{self.nome}")

        # Caso o usuário informa o código, edita um registro existnte:
        else:
            categorias = []
            # Salva os registros cadastrados em uma lista:
            with open("banco/categorias.txt", "r") as dados_banco:
                categorias_banco = dados_banco.readlines()

            # Salva os dados no banco:
            with open("banco/categorias.txt", "w") as dados_banco:
                for categoria in categorias_banco:
                    cat = categoria.strip().split(";")
                    if int(cat[0]) == self.codigo:
                        cat[1] = self.nome
                    cat = str(';'.join(cat)) + "\n"
                    categorias.append(cat)

                dados_banco.writelines(categorias)

    @staticmethod
    def listar() -> tuple:
        categorias = []
        with open("banco/categorias.txt", "r") as dados_banco:
            for cat_banco in dados_banco:
                categoria = tuple(cat_banco.strip().split(';'))
                categorias.append(categoria)
        return tuple(categorias)

    def apagar(self):
        categorias = []

        if self.codigo > 0:
            # Salva os registros cadastrados em uma lista:
            with open("banco/categorias.txt", "r") as dados_banco:
                categorias_banco = dados_banco.readlines()

            # Salva os dados no banco:
            with open("banco/categorias.txt", "w") as dados_banco:
                for categoria in categorias_banco:
                    cat = categoria.strip().split(";")
                    if int(cat[0]) != self.codigo:
                        cat = str(';'.join(cat)) + "\n"
                        categorias.append(cat)
                dados_banco.writelines(categorias)
