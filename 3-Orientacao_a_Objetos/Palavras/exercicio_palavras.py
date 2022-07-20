palavras = []
alfabeto = list("abcdefghijklmnopqrstuvxz")

with open("palavras.txt", "r", encoding='utf-8') as f:
    for linha in f:
        palavras.append(linha.strip())

def letras_no_arquivo(l = []):
    """verifica quantas vezes cada letra do alfabero aparece no 
    arquivo """
    for i in alfabeto:
        s = ""
        s = s.join(l)
        print(f"A letra {i} aparece {s.count(i)} vezes")


def contar_iniciais(l = []):
    """verifica quantas palavras começam """
    contador = 0
    for letra in alfabeto:
        for palavra in l:            
            if palavra[0] == letra:
                contador += 1        
        print(f"{contador} palavras começam com a letra \"{letra}\"")
        contador = 0

def iniciadas_iguais(l = [], iniciais = "ren"):
    """verifica quantas palavras começam com as três letras informada
    e as salva em um arquivo a parte"""
    for palavra in l:
        if palavra[:3] == iniciais:
            with open("palavras_iniciadas_com_3_letras", "a") as f:
                f.write(palavra)
                f.write("\n")

def palavras_com_nome(l = [], nome = "renan"):
    """verifica quantas palavras tem o nome colocado no parametro"""
    for palavra in l:
        if nome in palavra:
            with open("palavras_com_meu_nome", "a") as f:
                f.write(palavra)
                f.write("\n")
    
            

def palindromos(l = []):
    for palavra in l:
        if palavra == palavra[::-1]:
            with open("palindromos.txt", "a") as f:
                f.write(palavra)
                f.write("\n")







    

#print(f"Temos no arquivo {len(palavras)} palavras.")
#letras_no_arquivo(palavras)
#contar_iniciais(palavras)
#iniciadas_iguais(palavras, "ren")
#palavras_com_nome(palavras, "renan")
palindromos(palavras)

