# coding: latin-1

class Categoria:

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
            with open("../banco/categorias.txt", "r") as banco:
                for cat in banco:
                    ultimo_codigo = cat.strip().cat.split(";")[0]
                self.codigo = ultimo_codigo
            # Adiciona um novo registro:
            with open("../banco/categorias.txt", "a") as banco:
                banco.write(f"\n{self.codigo};{self.nome}")

        # Caso o usuário informa o código, edita um registro existnte:
        else:
            categorias = []
            # Salva os registros cadastrados em uma lista:
            with open("../banco/categorias.txt", "r") as banco:
                categorias_banco = list(banco)

            for categoria in categorias_banco:
                cat = categoria.strip().split(";")
                if int(cat[0]) == self.codigo:
                    cat[1] = self.nome

                new_cat = ';'.join(cat)
                categorias.append(new_cat)

            with open("../banco/categorias.txt", "w") as banco:
                banco.writelines(categorias)

    @staticmethod
    def listar() -> tuple:
        categorias = []
        with open("../banco/categorias.txt", "r") as banco:
            for cat_banco in banco:
                categoria = tuple(cat_banco.strip().split(';'))
                categorias.append(categoria)
        return tuple(categorias)

    # def apagar(self) -> bool:
