tds = []

for x in range(0,7):
    tds.append(int(input('N°: ')))
    tds.sort()

print(f'Os números pares são: ', end='')
for x in tds:
    if x % 2 == 0:
        print(x, end=' ')

print(f'\nOs números ímpares são: ', end='')
for x in tds:
    if x % 2 == 1:
        print(x, end=' ')