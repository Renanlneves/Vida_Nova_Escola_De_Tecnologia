<p align="center">
  <img src="https://user-images.githubusercontent.com/71992079/176956742-5c442712-2162-4068-a445-1d67ee47360a.png">
</p> 


# Exercício 1:
Implemente uma partida de par ou ímpar:
 - Pergunte ao usuário se ele prefere par ou ímpar
 - Valide a entrada dele (enquanto o usuário não digitar corretamente par ou ímpar ele deve continuar perguntando) 
 - Solicite ao usuário um número inteiro
 - Valide a entrada do usuário (verifique se não contém letras ou caracteres não-alfanuméricos)
 - Sorteie um número entre 0 e 5 para servir de número para o computador
 - Verifique o resultado e imprima na tela a mensagem correspondente
 - Por fim, transforme isso numa função que retorna 0 caso o jogador ganhe e 1 caso o computador ganhe

# Exercício 2:
Crie uma classe chamada Adversario:
 - Crie um atributo chamado nome que deve ser inicializado no momento da criação de um objeto dessa classe (na chamada do método __init__ )
 - Esse nome será o nome do usuário. Use-o para indicar quando o usuário vencer uma partida.
 - Implemente um método que joga par ou ímpar (aproveite o exercício anterior) uma única vez
 - Implemente um método chamado campeonato que, ao ser executado deve solicitar ao usuário quantas vezes (N) ele deseja competir.
 - Depois de jogar N vezes a classe deve imprimir na tela se o resultado foi uma vitória para o usuário (diga o nome dele), para o computador ou se houve empate
 - Dica: implemente os métodos de modo que para testar você não precise de nenhuma etapa adicional além de criar um objeto Adversario e rodar o método campeonato.
