# Implementar a classe de Vetores Não Ordenados

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = self.capacidade*[0] # diferente de []

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

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
    
    def duplicatas(self):
        lista_duplicados = []
        dic_duplicados = {}
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] not in dic_duplicados:
                dic_duplicados[self.valores[i]] = 1
            else:
                dic_duplicados[self.valores[i]] += 1
        
        for valor in dic_duplicados:
            if dic_duplicados[valor] > 1:
                lista_duplicados.append(valor)
        return lista_duplicados


                


# Chamando a Classe
vetor = VetorNaoOrdenado(8)

# =====================================
# ADICIONEM TESTES A PARTIR DAQUI
# =====================================

vetor.insere(0)
vetor.insere(2)
vetor.insere(6)
vetor.insere(3)
vetor.insere(4)
vetor.insere(2)
vetor.insere(6)
vetor.insere(6)

print(vetor.duplicatas())