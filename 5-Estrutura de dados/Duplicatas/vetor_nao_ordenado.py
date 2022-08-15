# Implementar a classe de Vetores Não Ordenados
class VetorNaoOrdenado:
    def __init__(self, capacidade, repetidos = False):
        self.repetidos = repetidos
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = self.capacidade*[0] 
        
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
        if self.repetidos == False:
            self.duplicatas(self.valores)


    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade máxima atingida")
        else:
            self.ultima_posicao = self.ultima_posicao + 1
            self.valores[self.ultima_posicao] = valor
    
    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao = self.ultima_posicao - 1
    

    def duplicatas(self, valores): 
        contador = 0
        lista_duplicados = []
        dic_duplicados = {}
        for i in valores:
            dic_duplicados[i] = dic_duplicados.get(i, 0) + 1
            contador += 1
        
        for valor in dic_duplicados:
            if dic_duplicados[valor] > 1:
                lista_duplicados.append(valor)
                contador += 1
        print(f"Os números: {lista_duplicados[:]} estão repetindo.")
        return lista_duplicados, contador
        


        
        



# Chamando a Classe
vetor = VetorNaoOrdenado(8, False)

# =====================================
# ADICIONEM TESTES A PARTIR DAQUI
# =====================================

vetor.insere(0)
vetor.insere(2)
vetor.insere(6)
vetor.insere(3)
vetor.insere(4)
vetor.insere(2)
vetor.insere(3)
vetor.insere(6)

vetor.imprime()

#print(vetor.duplicatas(vetor.valores))

