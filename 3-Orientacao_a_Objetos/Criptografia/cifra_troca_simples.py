"""essa cifra troca letras por numeros que se parecem com elas."""

frase_secreta = input("Digite a frase que você gostaria de criptografar: \n -> ").upper()

letras_numeros = {
    "A" : "4",
    "E" : "3",
    "S" : "5",
    "I" : "1"
}

frase_codificada = ""

for letra in frase_secreta:
    if letra in letras_numeros:
        letra_codificada = letras_numeros[letra]
        frase_codificada += letra_codificada
    else:
        frase_codificada += letra

print(frase_codificada)