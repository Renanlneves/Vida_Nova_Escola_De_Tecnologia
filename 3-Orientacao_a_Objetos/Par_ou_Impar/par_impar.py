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
        num_usuario = -1
        while num_usuario < 0 or num_usuario > 5:
            num_usuario = int(
                input("\nAgora diga um número (de 0 a 5) para sua jogada: -> "))
        break
    except ValueError:
        print("Apenas números inteiros validos.")

num_pc = randint(0, 5)
print(f"\n\tO computador escolheu -> {num_pc}.")
print(f"\tE você escolheu -> {num_usuario}.")

# somando os números
total = num_pc + num_usuario

# verificando se deu par ou impar

if total % 2 == 0:
    print("\n\t***Deu \"PAR\"!!***")
    resultado = "par"
else:
    print("\n\t***Deu \"IMPAR\"!!***")
    resultado = "impar"


def vitoria(escolha, resultado):
    """função que retorna 1 ou 0, dependendo do resultado da partida."""
    if escolha == resultado:
        print("\n\t**PARABÉNS VOCÊ VENCEU!**")
        return 0
    else:
        print("\n\t**VOCÊ PERDEU!**")
        return 1


vitoria(par_impar, resultado)
