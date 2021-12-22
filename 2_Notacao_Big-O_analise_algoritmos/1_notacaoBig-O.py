#Notação Big-O: 
#   Como comparar dois algoritmos?#
#   Comparação objetiva entre algoritmos
#   Considera diferenças entre poder de processamento, sistema operacional, linguagem de programção
#   O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas #

# Função 1 -O(n)

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i

    return soma

print(soma1(10))

import timeit #Para verificar em quanto tempo será feira a operação usamos o "timeit"
print(timeit.timeit("soma1(10)", setup="from __main__ import soma1"))
# E aí poderemos comparar com outros algoritmos o tempo para ver qual o mais otimizado e eficaz. Ambos os algoritmos trazendo o mesmo resultado a diferença estará no tempo de execução de cada um por conta do menor número de passos.

# Função 2 -O(3) O big-O dela é 3 por conta que ela possui 3 passos de execução no seu algoritmo.

def soma2(n):
    return (n * (n + 1)) / 2

soma2(10) 
print(soma2(10))

import timeit
print(timeit.timeit("soma1(10)", setup="from __main__ import soma1"))

# Em suma, a Função 2 vence como mais rápida e se mostra como algoritmo mais eficaz.