lista = [6, 4,8,1,7, 12, 2, 3]
n = len(lista)


def ordenacao(lista):
    

    for j in range(0, len(lista)-1):
        min = j

        for i in range(j, len(lista)):
            if lista[i] < lista[min]:
                aux = lista[min]
                lista[min] = lista[i]
                lista[i] = aux
    return lista

print(ordenacao([6,4,8,1,7, 12, 2, 3]))
