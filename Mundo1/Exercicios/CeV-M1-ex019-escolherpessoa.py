import random
n1 = input('Nome da primeira pessoa: ')
n2 = input('Nome da segunda pessoa: ')
n3 = input('Nome da terceira pessoa: ')
n4 = input('Nome da quarta pessoa: ')
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('A PESSOA ESCOLHIDA É {}'.format(escolhido))