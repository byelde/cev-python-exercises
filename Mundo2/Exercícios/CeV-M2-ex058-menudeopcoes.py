r = 0
n1 = int(input('1° Número: '))
n2 = int(input('2° Número: '))

while r != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS.
    [5] SAIR DO PROGRAMA''')

    r = int(input('Qual é a sua escolha? '))

    if r == 1: 
        print(f'A soma desses valores é: {n1+n2}')
    elif r == 2: 
        print(f'A multiplicação desses valores é: {n1*n2}')
    elif r == 3:
        if n1 > n2:
            m = n1
        elif n2 > n1:
            m = n2
        else:
            m = 'nenhum. São iguais'
        print(f'O maior desses valores é {m}')
    elif r == 4:
        n1 = int(input('Novo valor do 1° Número: '))
        n2 = int(input('Novo valor do 2° Número: '))
    elif r == 5:
        print('Saindo...')
    else:
        print('ERRO. Tente novamente.')