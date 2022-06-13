#declarando funções

def linhas_separacao(x = "-"):
    """função com linhas que podem ser usadas para dividir determinados itens na tela.
    ela pode receber uma outra string para imprimir no lugar da predefinida. """
    print("\t", end='')
    return x * 35

def verific_num_int(texto):
    while True:
        try:
            txt = int(input(texto))
        except (ValueError, TypeError):
            print("Por favor digite apenas números válidos.")
        except (KeyboardInterrupt):
            print("Nenhum número foi digitado")
            return 0
        else:
            return txt
    
def exibindo_dados(l = ["Sem dados", "Sem dados", "Sem dados"]):
    """função para exibir os dados previamente colocados na função dados_funcionario.
    não é esperado nenhum paramentro."""
    
    linhas_separacao("=")
    print("\t\tNome: ", l[0])
    linhas_separacao()
    print("\t\tSobrenome: ", l[1])
    linhas_separacao()
    print("\t\tCargo: ", l[2])
    linhas_separacao("=")
    

def dados_funcionario(nome = "Nome não definido", sobrenome = "Sobrenome não definido", cargo = "Cargo não definido"):
    """função que coleta dados do funcionario a ser cadastrado. Ela retorna inputs que 
    esperam entradas do usuario no parametro. e retorna uma lista com esses dados."""
    nome = input("Qual o nome do funcionário? ").title().strip(), 
    sobrenome = input("Qual o sobrenome do funcionário? ").title().strip(),
    cargo = input("Qual o cargo que o funcionário ocupará? ").upper().strip()

    lista_dados = []
    lista_dados.extend(nome)
    lista_dados.extend(sobrenome)
    lista_dados.append(cargo)
    return lista_dados

def salario(info_salario = 0.0):
    """função para coletar o valor do salario para o funcionario. Um loop infinito é
    utilizado para iniciar uma verificação try/except. Que é encerrada pelo return, 
    caso seja digitado numeros na entrada.."""
    
    while True:
        try:
            info_salario = float(input("Digite o salário do funcionario cadastrado: "))
                      
        except ValueError:
            print("Por favor utilize apenas números!")
        else:
            return info_salario


def aliquota_salario(salario_bruto = 0.0):
    """Calcula o valor a ser descontado para o imposto de renda de acordo com a faixa salarial do funcionario cadastrado"""
    
    porcentagens = [0, 0.075, 0.15, 0.225, 0.275]
    if salario_bruto <= 1903.98:
        desconto = porcentagens[0]
    elif salario_bruto > 1903.98 and salario_bruto <= 2826.65:
        desconto = porcentagens[1]
    elif salario_bruto > 2826.65 and salario_bruto <= 3751.05:
        desconto = porcentagens[2]
    elif salario_bruto > 3751.05 and salario_bruto <= 4664.68:
        desconto = porcentagens[3]
    else:
        desconto = porcentagens[4]
    
    desconto_porcentagem = desconto * 100
    liquido = salario_bruto - (salario_bruto * desconto)
    print(f"Foi deduzido {desconto_porcentagem:.2f}% de R${salario_bruto} ")
    print(f"O salário liquido será de {liquido}")



def cabecalho(txt):
    """cabeçalho que da suporte para a função menu"""
    print(linhas_separacao())
    print("\t", txt.center(35))
    print(linhas_separacao())

def menu(lista):
    """função que organiza o menu de interação do programa"""
    cabecalho("ESCOLHA UMA OPÇÃO")
    x = 1
    for item in lista:
        print(f"\t  {x} - {item}")
        x += 1
    print(linhas_separacao())
    opcao = verific_num_int("Escolha uma opção: ")
    return opcao