from random import randint

tupla = (randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(tupla)

for pos, c in (enumerate(tupla)):
    if pos == 0:
        maior = c
        menor = c

    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
            
print(maior,menor)