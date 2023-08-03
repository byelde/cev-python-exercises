par = []
imp = []

while True:
    n = int(input(': '))

    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)

    resp = input('Deseja continuar? [S/N]').upper()
    if resp == 'N':
        break

print(par)
print(imp)