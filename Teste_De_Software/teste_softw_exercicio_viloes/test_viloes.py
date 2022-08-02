from viloes import Marvel_viloes

vilao1 = Marvel_viloes("Mau", ["voar", "raios"], 5)
vilao2 = Marvel_viloes("Pé Sujo", ["Super chute sujo", "chulé"], 1)
vilao3 = Marvel_viloes("Pretty Prisioner", ["força", "Ser um preso bonito"], 4)



def test_get_nome():
    assert vilao1.get_nome() == "Mau"

def test_set_nome():
    vilao1.set_nome("mauzaum")
    assert vilao1.nome == "mauzaum"    

def test_get_poderes():
    assert vilao2.get_poderes() == ["Super chute sujo", "chulé"]

def test_set_poderes():
    vilao3.set_poderes(["força", "Ser um preso bonito", "Escapista"])
    assert vilao3.poderes == ["força", "Ser um preso bonito", "Escapista"]

def test_set_perigo():
    vilao1.set_perigo(3)
    assert vilao1.perigo == 3

def test_get_perigo():
    valor = vilao1.get_perigo()
    assert valor > 0 and valor <= 5 
    assert type(valor) is int

def test_dominar_o_mundo():
    n_perigo_v1 = vilao1.dominar_o_mundo(vilao1.perigo)
    if vilao1.perigo <= 2:
        assert n_perigo_v1 == "Vilão Morto"
    elif vilao1.perigo > 2 and vilao1.perigo < 5:
        assert n_perigo_v1 == "Vilão Preso"
    else:
        assert n_perigo_v1 == "Vilão Dominou O Mundo!"