#perguntando um número para o usuario
pergunta = int(input("Até Que número você gostaria de fazer a sequencia fibonacci?\n"))

while pergunta != 0:
    #declarando os dois primeiros números e em seguida a soma dos mesmos. 
    n1 = 0
    n2 = 1
    n3 = n1 + n2
    #printando as variaveis declaradas e na terceira ilustrando uma conta de adição.
    print("-" * 60)
    if pergunta == 1:
        print(0)
    elif pergunta == 2:
        print(0)
        print(1)
    elif pergunta == 3:
        print(0)
        print(1)
        print("3° 0 + 1 = 1")
    else:
        print(f"1° {n1}")
        print(f"2° {n2}")
        print(f"3° {n1} + {n2} = {n3}")
        # Loop em "while" onde o segundo numero da conta anterior passa a ser o primeiro. 
        # O segundo da conta anterior numero passa a ser o terceiro
        # e a variavel num3 faz a soma das variaveis num1 e num2.
        # O loop começa no 4° e vai até o valor da variavel "pergunta".
        nx = 4
        while nx <= pergunta:
        
            n1 = n2
            n2 = n3
            n3 = n1 + n2

            print(f"{nx}° {n2} + {n1} = {n3}")

            nx += 1
    pergunta = int(input("\nDigite um novo número ou digite \"0\" para terminar\n\n"))