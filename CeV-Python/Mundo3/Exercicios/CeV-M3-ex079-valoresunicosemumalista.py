lista = []
while True:
    for c in range(0,3):
        n = int(input('Digite um valor: '))
        if n in lista:
            print('Número já adicionado.')
        else:
            lista.append(n)

    resp = input('\nDeseja adicionar mais números? [S/N] ').upper()
    if resp == 'N':
        break
    elif resp == 'S':
        print('')
    else:
        print('Resposta inválida')
        break

print(f'\nValores: {sorted(lista)}')