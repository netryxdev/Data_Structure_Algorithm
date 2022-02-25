# Enfileirar
# Desenfileirar
# Fila_vazia
# ver_inicio

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
    def mostrar_no(self):
        print(self.valor)

class FilaListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __fila_vazia(self):
        return self.primeiro == None

    def insere_final(self, valor): #Enfileirar
        novo = No(valor)
        if self.__fila_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self): #Desenfileirar
        if self.primeiro == None:
            print('A fila está vazia')
            return  
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp.valor

    def ver_inicio(self):
        if self.primeiro == None:
            return -1
        return self.primeiro.valor


fila = FilaListaEncadeadaExtremidadeDupla()
fila.insere_final(1)
fila.insere_final(2)
fila.insere_final(3)
fila.ver_inicio()
fila.excluir_inicio()
fila.ver_inicio()
