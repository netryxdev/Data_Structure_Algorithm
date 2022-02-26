
def bubbleSort(lista):
    
    for i in range(len(lista)-1, 0, -1):

        for j in range(0, i):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
    

print(bubbleSort([6,4,8,1,7, 12, 2, 3]))

"""
Ou você pode fazer assim também como abaixo:
"""

import numpy as np

def bubbleSort2(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp

    return vetor

bubbleSort2(np.array([15, 34, 8, 3]))