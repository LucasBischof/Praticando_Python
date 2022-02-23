from random import shuffle
a1 = str(input('Escreva o primero nome: '))
a2 = str(input('Escreva o segundo nome: '))
a3 = str(input('Escreva o terceiro nome: '))
a4 = str(input('Esvreva o quarto nome: '))
lista = [a1,a2,a3,a4]
shuffle(lista)
print('A ordem da apresentação sera')
print(lista)

