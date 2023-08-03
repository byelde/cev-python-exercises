num = []
par = []
imp = []

while True:
    num.append(int(input(': ')))

    resp = input('Deseja continuar? [S/N]').upper()
    if resp == 'N':
        break

for v in num:
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)

print(f'Todos os valores: {num}')
print(f'Os valores pares: {par}')
print(f'Os valores impares: {imp}')