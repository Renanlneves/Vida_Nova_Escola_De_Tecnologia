qt_lugar = int(input("Usando apenas multiplos de 10, escreva quantos lugares teremos no cinema:"))

lugares = [" │_│ "] * qt_lugar

org_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

while " │_│ " in lugares:
    #imprime letras no topo
    for i in org_letras:
        print(" ",i," ", end='')

    #while para que se imprima um ultimo numero na ultima linha e depois pare.
    verificador = True
    while verificador == True:
        for x, l in enumerate(lugares):
            div_10 = x % 10 
            if div_10 == 0:
                print("%1.0f" %(x / 10))
                print("\n")

            
            print(l,end='')
        print("%1.0f" %(qt_lugar / 10 ))
        verificador = False

    verifica_2 = True
    while verifica_2 == True:
        #dados de linha e coluna
        linha = int(input("Escolha uma linha: "))
        coluna = input("Escolha uma coluna: ")
        coluna = coluna.upper().strip()

        #adicionando a posição da letra escrita em uma nova var
        coluna_num = org_letras.index(coluna)

        #nova variante que calcula a posição do item, usando da escolha da coluna e da linha
        lugar_escolhido = (linha * 10 - 10) + coluna_num

        #lugares[lugar_escolhido] = " │x│ "
        if lugares[lugar_escolhido] == " │x│ ":
            print("Esse lugar já está ocupado, por favor escolha outro.")
        else:
            lugares[lugar_escolhido] = " │x│ "
            verifica_2 = False

print("\n\t-- A sala está cheia! A sessão vai começar! --")
print("\n\n")


    
  
