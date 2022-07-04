from random import randint

# verificando se o usuario colocou o par ou impar e iniciando o jogo
par_impar = ""
while par_impar != "par" and par_impar != "impar":
    par_impar = input("""\n\t\t  *BEM VINDO*
  \t Este é o jogo do Par ou Impar!
  \t Para começar nos diga:
  \t Sua escolha será \"PAR\" ou será \"IMPAR\"? -> """).lower().strip()


# verificando se o número está dentro da faixa pedida e se é um inteiro.
while True:
    try:
        num_usuario = 0
        while num_usuario <= 0 or num_usuario > 5:
            num_usuario = int(
                input("Agora diga um número (de 1 a 5) para sua jogada: -> "))
        break
    except ValueError:
        print("Apenas números inteiros validos.")

num_pc = randint(0, 5)

print(num_pc)
