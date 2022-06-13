from funcoes_funcionario import *

lista_menu = ["1 - CADASTRAR FUNCIONÁRIO", "2 - DADOS DO FUNCIONÁRIO", "0 - SAIR"]
while True:
    resposta = menu(lista_menu)
    if resposta == 1:
        cabecalho("CADASTRAR FUNCIONÁRIO")
        dados = dados_funcionario()  
        lista_menu.insert(2, "3 - TRIBUTAÇÃO")
        
        
    elif resposta == 2:
        try:
            exibindo_dados(dados)
            print()
        except NameError:
            exibindo_dados()
    
    elif resposta == 3:
        
        aliquota_salario(dados[3])
     
    elif resposta == 0:
        cabecalho("Saindo do sistema")
        print()
        break
    else:
        print("Erro. Númerio invalido.")

