from random import randint
from time import sleep
from operator import itemgetter

jogadas = {}
cc = 1

for c in range(1,5):
    jogadas['Jogador-'+ str(c)] = randint(1,6)

for c in sorted(jogadas, key=jogadas.get, reverse=True):
    print(f'{cc}º lugar: {c} com {jogadas[c]} pontos.')
    cc += 1


'''print(sorted(jogadas)) #ordena, naturalmente, as chaves das listas
print(sorted(jogadas, key=jogadas.get)) #o 'key...get' muda o sentido da organização do dicionário: chave>valores'''