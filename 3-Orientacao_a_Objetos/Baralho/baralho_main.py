class Carta():
    VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q", "J", "K"]
    NAIPES = ["COPAS", "ESPADAS", "OUROS", "PAUS"]

    def __init__(self, valor, naipe):
        
        self.valida_carta(valor, naipe)
        self.valor = valor
        self.naipe = naipe
         
    def valida_carta(self, valor, naipe):
        if valor not in self.VALORES:
            raise Exception(f"Esse não é um valor valido: {valor}")
        if naipe not in self.NAIPES:
            raise Exception(f"Esse não é um valor valido: {naipe}")



    def mostrar(self):
        print(f"{self.valor} de {self.naipe}")

    def mudar_letra_num(self, valor, outra_carta):
        
        if valor == "A":           
            self.valor = "1"
        elif outra_carta.valor == "A":            
            outra_carta.valor = "1"

        if valor == "Q":            
            self.valor = "11"
        elif outra_carta.valor == "Q":            
            outra_carta.valor = "11"

        if valor == "J":            
            self.valor = "12"
        elif outra_carta.valor == "J":            
            outra_carta.valor = "12"

        if valor == "K":            
            self.valor = "13"
        elif outra_carta.valor == "K":            
            outra_carta.valor = "13"

        

    def __gt__(self, outra_carta):
        self.mudar_letra_num(self.valor, outra_carta)
        return self.valor > outra_carta.valor


    def __lt__(self, outra_carta):
        self.mudar_letra_num(self.valor, outra_carta)
        return self.valor < outra_carta.valor
    
    def __eq__(self, outra_carta):
        self.mudar_letra_num(self.valor, outra_carta)
        return self.valor == outra_carta.valor

    


c1 = Carta("A", "COPAS")
c2 = Carta("A", "PAUS")

c1.mostrar()
c2.mostrar()
print(c1 > c2)
print(c1 < c2)
print(c1 == c2)
