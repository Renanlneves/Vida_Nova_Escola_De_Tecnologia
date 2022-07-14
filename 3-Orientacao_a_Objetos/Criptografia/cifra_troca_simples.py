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

def decodificador(txt, dic_codigo):
    frase_decodificada = ""

    for letra in txt:
        if letra in dic_codigo:
            letra_decodificada = dic_codigo[letra]
            frase_decodificada += letra_decodificada
        else:
            frase_decodificada += letra
    return frase_decodificada



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


original = decodificador(codigo, numeros_letras)
print(f"A frase descodificada ficou: \n {original}")
