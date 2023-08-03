resposta = ''
c = soma = maior = menor = 0

while resposta != 'N':
    c += 1
    n = int(input('Digite um número: '))

    if resposta == '':
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    soma += n
    resposta = input('Quer continuar? ').upper().strip()

media = soma/c
print(f'MAIOR:{maior}, MENOR:{menor} e MÉDIA: {media:.2f}')