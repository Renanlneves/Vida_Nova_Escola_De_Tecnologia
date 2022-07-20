
try:
    import pyperclip
except ImportError:
    pass
#ensaiando e conhecendo as funções ord()(que pega o numero do character no unicode)
#e depois usando o chr() para transformar esse numero num character novamente
lista_letras = []
for i in range(ord("A"), ord("Z") +1):
    lista_letras.append(chr(i))

def escolhendo_funcao():
    """escolhendo entre criptografar ou descriptografar uma mensagem - não são esperados paremetros"""
    escolha = -1
    while escolha < 0 or escolha > 3:
                escolha = int(input("""\tEscolha um número:
                1 - CRIPTOGRAFAR
                2 - DESCRIPTOGRAFAR\n -> """))
    return escolha

def coletando_chave():
    """não são esperados parametros. Verificando se a chave é um número inteiro valido"""
    while True:
        chave = input("insira a chave para ser usada:\n -> ")
        if not chave.isdecimal():#se não for um numero, volte para o loop
            continue
        if int(chave) > 0:# se o numero for maior que 0 transforme ele em inteiro e pare o loop
            chave = int(chave)
            break
    return chave


mensagem = input("escreva uma mensagem para ser codificada\n ->").upper()

def criptografar(lista_letras, chave, mensagem, escolha):
    """São esparados como parametros, uma lista, um número inteiro e uma string.
      Transforma a string em uma nova cadeia de letras. Trocando a letra por uma que 
      esteja no mesmo número de chaves a frente no alfabeto"""
    codificada = ""
    tamanho_letras = len(lista_letras)
    for letra in mensagem:
        if letra == " ":
            codificada += " "
            continue
        posicao = lista_letras.index(letra) 
        if escolha == 1:
            letra_cod = lista_letras[(posicao + chave)%tamanho_letras] #usando o mudulo ()% para que assim que chegar no número maximo da lista, recomeçe 
            codificada += letra_cod
            
        elif escolha == 2:
            letra_cod = lista_letras[(posicao - chave)%tamanho_letras]            
            codificada += letra_cod
    return codificada


cript = escolhendo_funcao()
key = coletando_chave()
criptografada = criptografar(lista_letras, key, mensagem, cript)

print("\n", criptografada)
try:
    pyperclip.copy(criptografada)
    print("\nA mensagem foi copiada para a área de transferencia")
except:
    pass