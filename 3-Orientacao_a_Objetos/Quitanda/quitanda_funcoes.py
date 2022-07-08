from itertools import count


def verific_num_int(texto):
    """Faz a verificação do número digitado, afim de evitar erros."""
    while True:
        try:
            txt = int(input(texto))
        except (ValueError, TypeError):
            print("\n\t ** Por favor digite apenas números válidos. **")
        except (KeyboardInterrupt):
            print("\n\t** Nenhum número foi digitado **")
            
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

def sub_menu_fruta(nome, valor, unidades = 0):
    cabecalho(f"{nome} -> ${valor}")
    print("\t\tQuantas Unidades?")
    linhas_separacao()
    unidades = verific_num_int("-> ")
    return unidades

def total_frutas(unidades = 0, valor = 0): 
    total_uma_fruta = unidades * valor
    return total_uma_fruta

def menu(lista, texto):
    """função que organiza o menu de interação do programa
    precisa de doisa paremetros, sendo um uma lista, e e outro uma string
    """
    
    total_final = 0
    lista_total = []

    while True:
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

        #verificando se opção é menor do que os numeros no menu
        while True:
            try:
                opcao = verific_num_int("\n\tEscolha uma opção: ")
                quant_fruta = sub_menu_fruta(nomes_frutas[opcao - 1], valor_frutas[opcao - 1])
                break
            except IndexError:
                print("\n\t** Digite apenas os numeros que contem no menu. **")


        valor_uma_fruta = total_frutas(quant_fruta, valor_frutas[opcao - 1])
        cabecalho(f"""\tO total de {quant_fruta} {nomes_frutas[opcao - 1]}(s)
        \t\té de ${valor_uma_fruta}""" )
        
        #lista usada para o extrato final
        total_final += valor_uma_fruta  
        lista_total.append(quant_fruta)
        lista_total.append(nomes_frutas[opcao - 1])
        lista_total.append(valor_uma_fruta)


        terminar = input("\n\tGostaria de comprar mais alguma fruta (s / n)? -> ").lower()
        if terminar == "n":
            break    
    
    print("\n")
    cabecalho("** EXTRATO ** ")
    print("\tUNIDADES    FRUTA   VALOR UNITARIO\n")
    
    contador = 0
    for i in lista_total:
        contador += 1
        print("        ",i, end=" ")
        if contador % 3 == 0:
            print("\n")
    cabecalho("** TOTAL **")
    texto_total = str(total_final)
    cabecalho(f"$ {texto_total}")
    

    return total_final


        
def final_venda(total, lista_notas, valor_pago = ""):
    while not valor_pago.isnumeric():
        valor_pago = input(f"O total da compra é de ${total}. Qual valor você irá dar? -> ")

    
    valor_pago = int(valor_pago)
    troco = valor_pago - total
    troco_original = troco
    
    #criando uma lista com as notas necessarias para dar o troco
    notas_dadas_troco = []
    while True:
        for nota in lista_notas:      
            if nota <= troco:
                troco -= nota
                troco = round(troco, 2)
                notas_dadas_troco.append(nota)
                
                break           
        if troco == 0:
            break

    #contando a quantidade de notas e moedas de cada valor que será necessario e imprimindo
    lista_centavos = 0
    contagem = 0   
    cabecalho("NOTAS E MOEDAS PARA TROCO")
    for i in range(len(lista_notas)):
        if lista_notas[i] in notas_dadas_troco:
            contagem = notas_dadas_troco.count(lista_notas[i])
            if lista_notas[i] >= 1:
                print(f"\t    {contagem} nota(s)  de  {lista_notas[i]} Real(is)")
            else:
                lista_centavos = lista_notas[i] * 100 
                print(f"\t    {contagem} moeda(s)  de  {round(lista_centavos)} Centavos")
    cabecalho(F"TROCO TOTAL -> ${troco_original}")

            
    



    


