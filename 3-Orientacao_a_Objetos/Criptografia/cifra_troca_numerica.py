""" INCOMPLETO!
Cada letra será trocada por sua posição no alfabeto"""
def dict_letras_numeros(escolha = -1):
    numeros = []
    for i in range(1, 27):
        i = str(i)
        numeros.append(i)

    letras = "ABCDEFGHIJKLMNOPQRSTWUVXYZ"
    list(letras)

    while escolha < 0 or escolha > 3:
        escolha = int(input("""\tEscolha um número:
        1 - CRIPTOGRAFAR
        2 - DESCRIPTOGRAFAR\n -> """))

    #usando zip para criar uma tupla a partir de duas listas e convertendo a tupla em dicionario
    if escolha == 1:
        dict_num_letras = dict(zip(letras, numeros))
        return dict_num_letras
    else:
        dict_num_letras = dict(zip(numeros, letras))
        return dict_num_letras

def codificador(txt, dic_codigo):
    frase_codificada = ""

    for letra in txt:
        if letra in dic_codigo:
            
            letra_codificada = dic_codigo[letra]
            frase_codificada += letra_codificada
            frase_codificada += "-"
            
        else:
            
            frase_codificada += letra
            frase_codificada += "-"
    return frase_codificada

frase_original = input("Qual será a frase a ser codificada?\n -> ").upper()

frase_codificada = ""
codificar = dict_letras_numeros()
frase_codificada = codificador(frase_original, codificar)
print(frase_codificada)


