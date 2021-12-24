# Tuplas
tupla = ( 'Homo sapiens', 'Canis familiaris', 'Felis catus')


# Listas
l1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
l2 = ['Xenopus laevis', 'ailuropoda melanoleuca']

l2_2 = l2 * 2
print(l2_2)

l1.append('Gorila gorila')
print(l1)

l1.remove('Felis catus')


for item in l2_2:
    print(item)