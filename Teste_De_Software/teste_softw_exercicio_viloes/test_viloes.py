from viloes import Marvel_viloes

vilao1 = Marvel_viloes("Mau", ["voar", "raios"], 5)

def test_get_nome():
    assert vilao1.get_nome() == "Mau"

def test_set_nome():
    vilao1.set_nome("mauzaum")
    assert vilao1.nome == "mauzaum"    

def test_get_poderes():
    assert vilao1.get_poderes() == ["voar", "raios"]

def test_set_poderes():
    vilao1.set_poderes(["voar", "raios", "bafo"])
    assert vilao1.poderes == ["voar", "raios", "bafo"]

def test_get_perigo():
    assert vilao1.get_perigo() == 5
    #assert type(vilao1.get_perigo) is int

def test_set_perigo():
    vilao1.set_perigo(2)
    assert vilao1.perigo == 2