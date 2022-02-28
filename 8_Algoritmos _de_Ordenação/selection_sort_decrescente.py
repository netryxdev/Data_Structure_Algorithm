

def ordenacao(lista):
    

    for j in range(len(lista)):
        max = j

        for i in range(j, len(lista)):
            if lista[i] > lista[max]:
                aux = lista[max]
                lista[max] = lista[i]
                lista[i] = aux
    return lista

print(ordenacao([6,4,8,1,7, 12, 2, 3]))