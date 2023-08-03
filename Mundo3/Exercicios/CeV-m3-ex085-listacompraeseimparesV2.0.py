tds = [[],[]]
v = 0

for c in range(0,7):
    v = int(input('N°: '))
    if v % 2 == 0:
        tds[0].append(v)
    else:
        tds[1].append(v)

print(f'Os números pares são: {sorted(tds[0])}')
print(f'Os números ímpares são: {sorted(tds[1])}')  