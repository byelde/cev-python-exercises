a1 = int(input('1° termo: '))
r = int(input('Razão: '))
n = 0

while n < 10: #no lugar do dez, por EXATAMENTE O NÚMERO DE TERMOS QUE QUER.
    print(f'A{(n+1):2}: {a1 + r*n}')
    n += 1