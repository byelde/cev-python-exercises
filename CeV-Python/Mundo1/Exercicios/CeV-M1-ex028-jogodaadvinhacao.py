from random import randint

#computador pensando...
nm = randint(1,5)

#jogador tentando advinhar.
print('-=='*15)
nu = int(input('Em que número eu estou pensando [1-5]? '))
print('-=='*15)

if nm == nu:
    print('ACERTOU!')
else:
    print('ERROU KKKKKKKKKKKKKKKKK')