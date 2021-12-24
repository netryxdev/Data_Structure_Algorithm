nota = soma = 0
numero = 1
while numero <= 5:
  nota = float(input('Digite a nota:'))
  soma += nota
  numero += 1
  print('A média é ', soma / 5)
