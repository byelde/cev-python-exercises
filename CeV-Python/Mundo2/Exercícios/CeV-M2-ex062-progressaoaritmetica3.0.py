a1 = int(input('1° termo: ')) #1° termo
r = int(input('Razão: ')) # Razão
resp = 1 #Variável que determina se e quantas vezes continua.
c1 = 0 #variável de controle (rebobina)
n = c1 #N° do termo -1 (contínuo)

while resp != 0:
    while c1 < 10:
        prog = a1 + r*n
        c1 += 1
        n += 1
        print(f'{prog} -> ', end='')
    print('PAUSA.')
    resp = int(input('\nMais  quantas vezes? '))
    c1 -= resp
