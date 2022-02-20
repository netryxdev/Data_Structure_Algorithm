class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class PilhaListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def __pilha_vazia(self):
        return self.primeiro == None

    def empilhar(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo
        
    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vazia.')
            return None
        else:
            temp = self.primeiro
            self.primeiro = self.primeiro.proximo
            return temp
            
    def ver_topo(self):
        if self.primeiro == None:
            return print('A pilha está vazia.')
        else:
            return self.primeiro.valor

pilha = PilhaListaEncadeada()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)
pilha.empilhar(6)
pilha.empilhar(7)
pilha.desempilhar()
pilha.ver_topo()
pilha.primeiro.proximo.proximo