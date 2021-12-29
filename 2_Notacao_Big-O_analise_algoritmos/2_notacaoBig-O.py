# Função 3 Este é mais letno pois aqui a lista é feita de forma manual

def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
        return lista

print(lista1())



# Função 4 Este é mais rápida pois é feita de uma forma nativa da linguagem

def lista2():
    return range(1000)

l = lista2()

for i in l:
    print(i) 

