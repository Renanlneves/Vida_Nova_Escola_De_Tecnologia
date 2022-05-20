#coletando dados 
s = int(input("Qual foi o Valor do salario bruto?\n"))

#verificando em qual categoria entra o salario do usuario
if s <= 1903.98:
    print("Esse valor é isento de imposto")
elif s >= 1903.99 and s <= 2826.65:
    #calculando a porcentagem e depois printando os resultados.
    percentual = 7.5 / 100.0
    valor_final = s - (percentual * s)
    print(f"\nforam descontados 7,5% ou R$ {percentual * s}\n")
    print(f"O valor liquido será de R$ {valor_final}\n")
elif s >= 2826.66 and s <= 3751.05:
    percentual = 15 / 100
    valor_final = s - (percentual * s)
    print(f"\nforam descontados 15% ou R$ {percentual * s}\n")
    print(f"O valor liquido será de R${valor_final}\n")
elif s >= 3751.06 and s <= 4664.68:
    percentual = 22.5 / 100
    valor_final = s - (percentual * s)
    print(f"\nforam descontados 22,5% ou R$ {percentual * s}\n")
    print(f"O valor liquido será de R${valor_final}\n")
else:
    percentual = 27.5 / 100
    valor_final = s - (percentual * s)
    print(f"\nforam descontados 27,5 % ou R$ {percentual * s}\n")
    print(f"O valor liquido será de R${valor_final}\n")