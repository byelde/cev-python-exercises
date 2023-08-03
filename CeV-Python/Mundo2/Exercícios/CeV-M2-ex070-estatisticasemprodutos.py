total = np1000 = pmenor = 0
nmenor = ''

while True:
    nome_prod = input('\nNome do produto: ').upper()
    prec_prod = float(input('Preço: R$'))

    total += prec_prod

    if prec_prod > 1000:
        np1000 += 1

    if nmenor == '':
        pmenor = prec_prod
        nmenor = nome_prod

    if prec_prod < pmenor:
        pmenor = prec_prod
        nmenor = nome_prod

    resp = input('\nDeseja continuar? [S/N] ').upper()
    if resp == 'N':
        break

print(f'O gasto total foi R${total:.2f}')
print(f'{np1000} produto(s) passaram de R$1.000,00')
print(f'O produto {nmenor} foi o mais barato (R${pmenor:.2f})')