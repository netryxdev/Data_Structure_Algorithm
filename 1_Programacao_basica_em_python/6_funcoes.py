# Função sem passagem de parâmetro

def mensagem():
    print('Texto da função')

print(mensagem)

# Função com passagem de parâmetro

def mensagem(texto):
    print(texto)

def soma(a, b):
    print(a + b)

print(soma(3, 4))

# Função com passagem de parâmetros e retorno

def soma(a, b):
    return a + b
    
def calcula_energia_potencial_gravitacional(m, h, g = 10):
    '''
    Calcula a energia potencial gravitacional
    Argumentos:
    m: masssa, entrada como uma variável float
    h: altura, entrada como uma variável float

    Argumento opcional:
    g: aceleração gravitacional, com valor default de 10
    '''
    e = g * m * h
    return e

help(calcula_energia_potencial_gravitacional)
