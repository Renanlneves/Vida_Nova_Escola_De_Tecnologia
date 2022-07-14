""" INCOMPLETO! - não está pegando o espaço quando entra a pergunta (linha 56)
Cada letra será trocada por sua posição no alfabeto"""

try:
    import pyperclip #pyperclip copia textos com se fosse ctrl c e ctrl z
except ImportError:
    pass #se o pyperclip não tiver instalado, não faça nada



def dict_letras_numeros(escolha = -1):
    numeros = list(range(1, 27)) #transformando numa lista os numeros no range
    numeros = list(map(str, numeros)) #map está aplicando a função str para cada iten na lista numeros
    
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
            
        
    return frase_codificada



frase_original = input("Qual será a frase a ser codificada?\n -> ").upper()
frase_num = frase_original.split("-")
print(frase_num)

frase_codificada = ""
codificar = dict_letras_numeros()
if frase_num[0].isnumeric(): 
    frase_codificada = codificador(frase_num, codificar)
else:
    frase_codificada = codificador(frase_original, codificar)
    

print(frase_codificada)

numeros = list(range(10))
numeros = list(map(str, numeros))

for i in frase_codificada:
    if i not in numeros:
        for i in frase_codificada:
            if i == "-":
                continue
            else:
                print(i, end="")
    break


try:
    pyperclip.copy(frase_codificada)
    print("\nTexto completo copiado para area de transferência")
except:
    pass #não faz nada se o pyperclip não estiver instalado

