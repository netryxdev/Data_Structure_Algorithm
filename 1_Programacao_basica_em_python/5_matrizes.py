import numpy as np

matriz = np.array([[2, 3, 1],
                   [4, 5, 7]])

matriz.shape

matriz[0] # indica linha 1
matriz[1] # indica linha 2

matriz[0][2] # Indica o elemento da linha 1 e coluna 3. No caso: 1.
matriz[1][2] # = 7

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])