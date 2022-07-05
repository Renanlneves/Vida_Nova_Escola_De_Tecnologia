from random import randint


class Adversario:
    def __init__(self, nome):
        self.nome = nome

    def jogo_par_impar(self, escolha_jogador="", num_usuario=-1):

        while escolha_jogador != "par" and escolha_jogador != "impar":
            escolha_jogador = input("""\n\t\t  *BEM VINDO*
        \t Este é o jogo do Par ou Impar!
        \t Para começar nos diga:
        \t Sua escolha será \"PAR\" ou será \"IMPAR\"? -> """).lower().strip()

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

        if escolha_jogador == resultado:
            print("\n\t**PARABÉNS VOCÊ VENCEU!**")
            return 0
        else:
            print("\n\t**VOCÊ PERDEU!**")
            return 1

    def campeonato(self, competir=0):
        competir = int(
            input("Olá! Em quantas partidas você gostaria de competir? -> "))
        venceu = 0
        perdeu = 0
        for i in range(0, competir):
            pontos = self.jogo_par_impar()
            if pontos == 0:
                venceu += 1
            else:
                perdeu += 1
        if venceu > perdeu:
            print(
                f"\tPARABÉNS!! {self.nome}: {venceu} pts x Computador: {perdeu} pts")
        elif venceu == perdeu:
            print(
                f"\tEMPATOU!! {self.nome}: {venceu} pts x Computador: {perdeu} pts")
        else:
            print(
                f"\tDERROTA!! {self.nome}: {venceu} pts x Computador: {perdeu} pts")


Jogador1 = Adversario("renan")
Jogador1.campeonato()
