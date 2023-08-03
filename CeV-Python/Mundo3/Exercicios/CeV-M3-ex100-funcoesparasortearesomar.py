from random import randint
def sorteio(l):
    for c in range(0,5):
        l.append(randint(0,10))
    print(f'a lista de números é {l}')
    return l

def somapar(l):
    soma = 0
    for c in l:
        if c % 2 == 0:
            soma += c
    print(f'A soma dospares é {soma}')

#programa principal
numeros = []
sorteio(numeros)
somapar(numeros)