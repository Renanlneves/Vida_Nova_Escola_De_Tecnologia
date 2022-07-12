def ifen_cep(cep):
    lista = list(cep)
    lista.insert(-3, "-")
    cep_ifen = "".join(lista)
    return cep_ifen


dados = ["Nome", "Logradouro", "Numero", "Complemento", "Bairro", "Cidade", "Estado", "CEP"]
dados_usuario = {}

for dado in dados:
    dados_usuario[dado] = input(f"Por favor insira seu {dado}: ").upper()


nome = dados_usuario['Nome']
logradouro = dados_usuario['Logradouro']
numero = dados_usuario['Numero']
complemento = dados_usuario['Complemento']
bairro = dados_usuario['Bairro']
cep = dados_usuario['CEP']
cep = ifen_cep(cep)
cidade = dados_usuario['Cidade']
estado = dados_usuario['Estado']


carta = f"""\t{nome}
\t{logradouro}, {numero} comp. {complemento}
\tBairro {bairro}
\tCEP {cep} - {cidade} - {estado}"""

print(carta)



