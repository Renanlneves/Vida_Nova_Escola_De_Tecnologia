import re


def verific_num_int(texto):
    """Faz a verificação do número digitado, afim de evitar erros."""
    while True:
        try:
            txt = int(input(texto))
        except (ValueError, TypeError):
            print("Por favor digite apenas números válidos.")
        except (KeyboardInterrupt):
            print("Nenhum número foi digitado")
            return 0
        else:
            return txt

def linhas_separacao(x = "-"):
    """função com linhas que podem ser usadas para dividir determinados itens na tela.
    ela pode receber uma outra string para imprimir no lugar da predefinida. """
    print("\t", end='')
    return x * 35

def cabecalho(txt):
    """cabeçalho que da suporte para a função menu"""
    print(linhas_separacao())
    print("\t", txt.center(35))
    print(linhas_separacao())

def menu(lista, texto):
    """função que organiza o menu de interação do programa
    precisa de doisa paremetros, sendo um uma lista, e e outro uma string
    """
    cabecalho(texto)
    nomes_frutas = []
    valor_frutas = []
    x = 1
    for item in lista:
        print(f"\t\t {x} -> {item}: ${lista[item]}")
        x += 1
        nomes_frutas.append(item)
        valor_frutas.append(lista[item])
    print(linhas_separacao())
    opcao = verific_num_int("Escolha uma opção: ")

    quant_fruta = sub_menu_fruta(nomes_frutas[opcao - 1], valor_frutas[opcao - 1])
    valor_uma_fruta = total_frutas(quant_fruta, valor_frutas[opcao - 1])
    cabecalho(f"""\tO total de {quant_fruta} {nomes_frutas[opcao - 1]}(s)
    \t\té de ${valor_uma_fruta}""" )

    return opcao
    

def sub_menu_fruta(nome, valor, unidades = 0):
    cabecalho(f"{nome} -> ${valor}")
    print("\t\tQuantas Unidades?")
    linhas_separacao()
    unidades = int(input("-> "))
    return unidades

def total_frutas(unidades = 0, valor = 0): 
    total_uma_fruta = unidades * valor
    return total_uma_fruta