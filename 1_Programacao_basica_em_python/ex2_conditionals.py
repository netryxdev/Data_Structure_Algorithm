children = 0 <= 12
teen = 13 <= 17
adult = 18 <= 150 

age = int(input('Enter your age: ')) # O comando input serve para coletar o dado


if age < 13: 
    print('É uma criança.')
elif age > 13 | age <=17 : 
    print('Adolescente.')
else :
   print('É um adulto.')
