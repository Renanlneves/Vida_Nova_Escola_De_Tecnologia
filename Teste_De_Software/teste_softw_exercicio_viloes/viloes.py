
class Marvel_viloes:
    def __init__(self, nome, poderes, perigo):
        self.nome = nome
        self.poderes = poderes
        self.perigo = int(perigo)
        

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_poderes(self):
        return self.poderes

    def set_poderes(self, poderes):
        self.poderes = poderes

    def get_perigo(self):
        return self.perigo

    def set_perigo(self, perigo):
        self.perigo = perigo

    def dominar_o_mundo(self, perigo):
        if perigo <= 2:
            return "Vilão Morto"
        elif perigo > 2 and perigo < 5:
            return "Vilão Preso"
        else:
            return "Vilão Dominou O Mundo!"

        
    


vilao1 = Marvel_viloes("Mau", ["voar", "raios"], 5)
tipo = type(vilao1.get_perigo())
print(tipo)