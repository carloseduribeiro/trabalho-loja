from Classes.Categorias import Categorias


def listar_categorias():
    opcao = 0
    # Armazena a lista de ids e nomes das categorias cadastradas:
    ids = []
    nomes_categoria = []
    while opcao != 9:
        # Imprime as categorias cadastradas:
        print(f"\n{' CATEGORIAS ':=^30}")
        print(f"{'Id:':<4}\t{'Nome:'}")
        for cat in Categorias.listar():
            print(f"{cat[0]:<4}\t{cat[1]}")
            ids.append(int(cat[0]))
            nomes_categoria.append(cat[1])
        # Imprime o menu:
        print(f"{'':=^30}\n" +
              "Escolha uma opção:\n" +
              "1 - Cadastrar\n" +
              "2 - Editar\n" +
              "3 - Apagar\n" +
              "0 - Sair")
        try:
            opcao = int(input("Digite: "))

            if opcao == 1:
                # Cadastra uma nova categoria:
                print(f"\n{' NOVA CATEGORIA ':=^30}")
                nome_categoria = input("Insira o nome: ")
                print(f"{'':=^30}")

                # Verifica se já existe uma categoria com o mesmo nome:
                if nome_categoria not in nomes_categoria:
                    Categorias(nome_categoria).salvar()
                    print("Categoria cadastrada.")
                else:
                    print("Categoria NÃO cadastrada!")
                    print("Categoria já existe.\n")

            elif opcao == 2:
                # Edita uma categoria existente:
                print(f"\n{' EDITAR CATEGORIA ':=^30}")
                try:
                    id_categoria = int(input("Insira o id: "))
                    print(f"{'':=^30}")

                    if id_categoria in ids:
                        nome_categoria = input("Insira o novo nome: ")
                        # Salva as alterações
                        Categorias(nome_categoria, id_categoria).salvar()
                    else:
                        print("Id não existe! Tente novamente.")
                except ValueError:
                    print("Id inserido não existe!")

            elif opcao == 3:
                try:
                    # Apaga a categoria selecionada:
                    id_categoria = int(input("Insira o id: "))
                    print(f"{'':=^30}")

                    if id_categoria in ids:
                        Categorias('', id_categoria).apagar()
                        print("Categoria APAGADA!")
                    else:
                        print("Id não existe! Tente novamente.")
                except ValueError:
                    print("Id não existe! Tente novamente.")

            elif opcao < 0 or opcao > 3:
                print("Opção não existe! Tente novamente.")

            else:
                break
        except ValueError:
            print("Opção não existe! Tente novamente.")
