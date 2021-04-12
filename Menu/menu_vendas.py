from Classes.Vendas import Vendas
from Menu.menu_produtos import listar_produtos


def listar_vendas():
    print("Iimprimir vendas")


def form_nova_venda():
    opcao = int
    cliente_existe = False
    cpf_cliente = 99
    produtos = {}

    while cpf_cliente != '0':
        print(f"{' NOVA VENDA ':=^30}")
        print("Digite 0 para sair.")
        cpf_cliente = input("Insira o CPF do cliente: ")

        with open("banco/clientes.txt", "r") as dados_banco:
            lines = dados_banco.readlines()
            for line in lines:
                cliente = line.strip().split(";")

                if cliente[3] == cpf_cliente:
                    cliente_existe = True
                    venda = Vendas(cliente[3])
                    break
                else:
                    cliente_existe = False

        if cliente_existe:
            opcao = 99
            while opcao != 0:
                print("1 - Adicionar Produtos\n"
                      "2 - Remover Produtos\n"
                      "3 - Finalizar Venda\n"
                      "0 - Cancelar venda\n")
                opcao = input("Digite: ")

                if opcao == '1':
                    id_produto = 99
                    while id_produto != 0:
                        produtos = listar_produtos()
                        print(f"{'':=^30}")
                        print("Digite 0 para sair.")
                        cod_produto = input("Escolha o produto: ")
                        if cod_produto == '0':
                            break
                        if cod_produto in produtos.keys():
                            qtd_produto = int(input("Insira a quantidade: "))

                            venda.adicionar_produto(cod_produto, qtd_produto, produtos[cod_produto][1])
                        else:
                            print("Produto não existe! Tente novamente.")

                elif opcao == '2':
                    cod_produto = 99
                    while cod_produto != 0:
                        print(f"{' CARRINHO ':=^30}")
                        if len(venda.listar_produtos()) != 0:
                            print(f"{'Codigo':<6}\t{'Quantidade':<10}\t{'Valor':<10}")
                            for k, v in venda.listar_produtos().items():
                                vlr_total = float(v[1]) * float(v[2])
                                print(f"{k:<6}\t{v[1]:<10}\tR$ {str(vlr_total):<10}")
                        else:
                            print("Nenhum produto foi adicionado ao carrinho.")
                        print(f"{'':=^30}")

                        print("Digite 0 para sair.")
                        cod_produto = input("Escolha o produto: ")

                        if cod_produto == '0':
                            break
                        if cod_produto in produtos.keys():
                            try:
                                qtd_produto = int(input("Insira a quantidade: "))

                                venda.remover_produtos(cod_produto, qtd_produto)
                            except Exception as e:
                                print("Valor inválido. Tente novamente.")
                        else:
                            print("Produto não existe! Tente novamente.")

                elif opcao == '3':
                    menu = 99
                    while menu != 0:
                        print(f"{' FINALIZAR VENDA ':=^30}")
                        print(venda.listar_produtos())

                        if len(venda.listar_produtos()) != 0:
                            print(f"{'Cod.:':<6}{'nome':<20}{'Qtd.:':<10}{'Valor Un.:':<15}{'Total:':<10}")
                            for k, v in venda.listar_produtos().items():
                                vlr_total = float(v[1]) * float(v[2])
                                print(f"{k:<6}{v[0]:<20}{v[1]:<10}{'R$ ' + v[2]:<15}{'R$ ' + str(vlr_total):<10}")


                        else:
                            print("Nenhum produto foi adicionado ao carrinho.")
                            print(f"{'':=^30}")
                            break
                        print(f"{'':=^30}")
                        print("Escolha uma fomra de pagamento:\n"
                              "1 - Cartão\n"
                              "2 - Dinheiro\n")
                        menu = input("Digite: ")

                elif opcao == '0':
                    break
                else:
                    print("Opção não existe! Tente novamente.")
        else:
            print("Cliente não existe! Tente novamente.")
