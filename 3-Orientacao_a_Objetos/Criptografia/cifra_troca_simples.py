"""essa cifra troca letras por numeros que se parecem com elas."""

def codificador(txt, dic_codigo):
    frase_codificada = ""

    for letra in txt:
        if letra in dic_codigo:
            letra_codificada = dic_codigo[letra]
            frase_codificada += letra_codificada
        else:
            frase_codificada += letra
    return frase_codificada

def descodificador(txt, dic_codigo):
    frase_descodificada = ""

    for letra in txt:
        if letra in dic_codigo:
            letra_descodificada = dic_codigo[letra]
            frase_descodificada += letra_descodificada
        else:
            frase_descodificada += letra
    return frase_descodificada



frase_secreta = input("Digite a frase que você gostaria de criptografar: \n -> ").upper()

letras_numeros = {
    "A" : "4",
    "E" : "3",
    "S" : "5",
    "I" : "1"
}
numeros_letras = {
    "4" : "A",
    "3" : "E",
    "5" : "S",
    "1" : "I"
}


codigo = codificador(frase_secreta, letras_numeros)
print(f"A frase codificada ficou: \n {codigo}")


original = descodificador(codigo, numeros_letras)
print(f"A frase descodificada ficou: \n {original}")
