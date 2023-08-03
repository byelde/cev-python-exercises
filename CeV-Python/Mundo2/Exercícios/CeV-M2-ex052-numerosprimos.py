n = int(input('Digite um número: '))
nd = 0

for d in range(1,n+1):
    if n % d == 0:
        print(f'>{d}<', end= ' ')
        nd += 1

    else:
        print(d, end= ' ')

print(f'\n\nO número {n} foi dividido {nd} vez(es).')
if nd == 2:
    print('\nEntão ele É um número PRIMO!')
else:
    print('\nEntão ele NÃO É um número PRIMO!')