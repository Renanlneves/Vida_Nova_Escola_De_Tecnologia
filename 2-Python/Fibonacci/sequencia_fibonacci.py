#declarando os dois primeiros números e em seguida a soma dos mesmos. 
n1 = 0
n2 = 1
n3 = n1 + n2
#printando as variaveis declaradas e na terceira ilustrando uma conta de adição.
print(f"1° {n1}")
print(f"2° {n2}")
print(f"3° {n1} + {n2} = {n3}")
# Loop em "for" onde o segundo numero da conta anterior passa a ser o primeiro. 
# O segundo da conta anterior numero passa a ser o terceiro
# e a variavel num3 faz a soma das variaveis num1 e num2.
# O loop começa no 3° e vai até o 10°.
for i in range(3, 11):
    n1 = n2
    n2 = n3
    n3 = n1 + n2

    print(f"{i}° {n2} + {n1} = {n3}")