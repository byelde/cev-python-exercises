from random import randint

lista = []
listatemp = []

qntj = int(input('Quantos jogos gostaria de gerar? '))

for jogos in range(0,qntj):
    for num in range (0,6):
        while True:
            n = randint(1,60)
            if n not in listatemp:
                listatemp.append(n)
                break
    lista.append(listatemp[:])
    listatemp.clear()

print('Os jogos formados foram:\n')
for num in range(0, len(lista)):
    print (f'Jogo {num+1}: {sorted(lista[num])}')