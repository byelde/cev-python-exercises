import random
n1 = input('Nome da primeira pessoa: ')
n2 = input('Nome da segunda pessoa: ')
n3 = input('Nome da terceira pessoa: ')
n4 = input('Nome da quarta pessoa: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ORDEM DE APRESENTAÇÃO É {}'.format(lista))