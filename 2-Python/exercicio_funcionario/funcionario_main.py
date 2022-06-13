import funcoes_funcionario


while True:
    resposta = funcoes_funcionario.menu(["CADASTRAR FUNCIONÁRIO", "DADOS DO FUNCIONÁRIO", "SAIR"])
    if resposta == 1:
        funcoes_funcionario.cabecalho("opc 1")
        print()
    elif resposta == 2:
        funcoes_funcionario.cabecalho("opc 2")
        print()
    elif resposta == 3:
        funcoes_funcionario.cabecalho("Saindo do sistema")
        print()
        break
    else:
        print("Erro. Númerio invalido.")




