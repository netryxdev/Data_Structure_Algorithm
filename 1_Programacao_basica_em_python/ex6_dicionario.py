alunos = {}
for _ in range(1, 4):
    nome = input('Digite o nome: ')
    nota = float(input('Digite a nota: '))
    alunos[nome] = nota

    alunos.values()

    # Para realizar a média dos alunos:

    soma = 0
    for nota in alunos.values():
        #print(nota)
        soma += nota
        print('Média: ', soma / 3)