
def insertion_sort(lista):
    n = len(lista)

    for i in range(1, n):
        marcado = lista[i]
        # Inserir lista[i] na sequência ordenada lista[1..i-1].
        j = i - 1
        while j >= 0 and marcado < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = marcado

    return lista

print(insertion_sort([6,4,8,1,7, 12, 2, 3]))
