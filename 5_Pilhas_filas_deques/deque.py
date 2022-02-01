import numpy as np

class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade - 1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1

    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return

        # Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Início estivar na primeira posição
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor
    
    def insere_final(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return
        
        # Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Final estiver na última posição
        elif self.final == self.capacidade -1:
            self.final = 0
        else:
            self.final += 1
