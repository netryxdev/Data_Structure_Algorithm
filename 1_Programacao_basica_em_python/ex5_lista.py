lista = []
for _ in range(1, 6):
    valor = int(input('Digite o valor:'))
    lista.append(valor)

soma = 0
for i in range(len(lista)):
    print(lista[i])
    soma += lista[i]
    print('soma: ', soma)
    