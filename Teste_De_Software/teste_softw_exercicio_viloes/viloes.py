
class Marvel_viloes:
    def __init__(self, nome, poderes, perigo):
        self.nome = nome
        self.poderes = poderes
        self.perigo = perigo
        

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_poderes(self):
        return self.poderes

    def set_poderes(self, poderes):
        self.poderes = poderes

    def get_perigo(self):
        perigo = 0
        while perigo < 1 or perigo > 5:            
            try:
                perigo = int(input("Qual o nivel de perigo do vilão?"))
            except ValueError:
                continue
        return self.perigo

    def set_perigo(self, perigo):
        self.perigo = perigo
        
    


vilao1 = Marvel_viloes("Mau", ["voar", "raios"], 5)
vilao1.get_perigo()