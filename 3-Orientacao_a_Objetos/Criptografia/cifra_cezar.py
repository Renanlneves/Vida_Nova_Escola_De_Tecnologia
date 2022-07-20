
#ensaiando e conhecendo as funções ord()(que pega o numero do character no unicode)
#e depois usando o chr() para transformar esse numero num character novamente
lista_letras = []
for i in range(ord("A"), ord("Z") +1):
    lista_letras.append(chr(i))


escolha = -1
while escolha < 0 or escolha > 3:
            escolha = int(input("""\tEscolha um número:
            1 - CRIPTOGRAFAR
            2 - DESCRIPTOGRAFAR\n -> """))

while True:
    chave = input("insira a chave para ser usada:\n -> ")
    if not chave.isdecimal():#se não for um numero, volte para o loop
        continue
    if int(chave) > 0:# se o numero for maior que 0 transforme ele em inteiro e pare o loop
        chave = int(chave)
        break


mensagem = input("escreva uma mensagem para ser codificada\n ->").upper()

def criptografar(lista_letras, chave, mensagem):
    codificada = ""
    tamanho_letras = len(lista_letras)
    for letra in mensagem:
        posicao = lista_letras.index(letra)
        letra_cod = lista_letras[(posicao + chave)%tamanho_letras] #usando o mudulo ()% para que assim que chegar no número maximo da lista, recomeçe 
        codificada += letra_cod
    return codificada


print(mensagem)
print(criptografar(lista_letras, chave, mensagem))