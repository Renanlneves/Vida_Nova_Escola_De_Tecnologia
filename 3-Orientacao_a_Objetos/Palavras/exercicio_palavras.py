palavras = []
alfabeto = list("abcdefghijklmnopqrstuvxz")

with open("palavras.txt", "r", encoding='utf-8') as f:
    for linha in f:
        palavras.append(linha.strip())

def letras_no_arquivo(l = []):  # Tente usar outro nome para listas. Apenas a letra l é muito fácil de confundir
    """verifica quantas vezes cada letra do alfabero aparece no 
    arquivo """
    # Como essa ação é executada em toda iteração do for, daria pra executá-la uma única vez antes do for. 
    # Assim economizamos tempo
    palavras_unidas = "".join(l) 
    for i in alfabeto:
        # s = ""
        # s = s.join(l) # Perceba que você executa isso em todas as iterações. Daria pra fazer antes do 
        print(f"A letra {i} aparece {palavras_unidas.count(i)} vezes")


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
            with open("palavras_iniciadas_com_3_letras.txt", "a") as f: # Não esqueça de colocar uma extensão no nome do arquivo
                f.write(palavra)
                f.write("\n")

def palavras_com_nome(l = [], nome = "renan"):
    """verifica quantas palavras tem o nome colocado no parametro"""
    for palavra in l:
        if nome in palavra:
            with open("palavras_com_meu_nome.txt", "a") as f: # aqui também
                f.write(palavra)
                f.write("\n")
    
            

def palindromos(l = []):
    for palavra in l:
        if palavra == palavra[::-1]:
            with open("palindromos", "a") as f:
                f.write(palavra)
                f.write("\n")







    

#print(f"Temos no arquivo {len(palavras)} palavras.")
#letras_no_arquivo(palavras)
# contar_iniciais(palavras)
# iniciadas_iguais(palavras, "ren")
# palavras_com_nome(palavras, "renan")
palindromos(palavras)

