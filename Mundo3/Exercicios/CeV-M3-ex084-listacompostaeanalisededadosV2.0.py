temp = []
prin = []
mai = men = 0

while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))

    if len(prin) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    prin.append(temp[:])
    temp.clear()
    resp = input('Continuar? ').upper()
    if resp == 'N':
        break

print(f'Foram cadastradas {len(prin)} pessoas.')

print(f'O menor peso foi {men}kg de: ',end='')
for pessoa in prin:
    if pessoa[1] == men:
        print(pessoa[0], end=' ')

print(f'\nO maior peso foi {mai}kg de: ', end='')
for pessoa in prin:
    if pessoa[1] == mai:
        print(pessoa[0], end='')