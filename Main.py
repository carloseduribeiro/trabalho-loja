# coding=utf-8

from Menu.menu_vendas import form_nova_venda, listar_vendas
from Menu.menu_clientes import listar_clientes
from Menu.menu_produtos import menu_produtos
from Menu.menu_categorias import listar_categorias


# MENU PRINCIPAL:
menu = 0

while menu != 9:
    print("""
============ LOJA ============
1 - Nova Venda
2 - Hisórico de Vendas
3 - Clientes
4 - Produtos
5 - Categorias
0 - Sair
==============================""")
    menu = input("Digite opção: ")

    try:
        menu = int(menu)

        if menu == 1:
            form_nova_venda()
        elif menu == 2:
            listar_vendas()
        elif menu == 3:
            listar_clientes()
        elif menu == 4:
            menu_produtos()
        elif menu == 7:
            listar_categorias()
        elif menu < 0 or menu > 7:
            print("Opção não existe! Tente novamente.")
        else:
            break
    except ValueError:
        print("Opção não existe! Tente novamente.")

print("Programa encerrado...")
