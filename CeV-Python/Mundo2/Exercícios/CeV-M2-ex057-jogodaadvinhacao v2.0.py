from random import randint

nm = randint(1,10)
nj = 0
nt = 0

print('Pensei em um número entre 1 e 10\nQual número você acha que é? ')
while nj != nm:
    nj = int(input(':'))
    if nj != nm:
        nt += 1
        print('{}... Tente mais uma vez.'.format('MENOS' if nj > nm else 'MAIS'))
    else:
        nt += 1
        print('ACERTOU!!')
        print(f'Você conseguiu em {nt} tentativa(s).')