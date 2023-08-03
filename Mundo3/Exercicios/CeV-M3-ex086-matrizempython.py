matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz [l][c] = int(input(f'V{l,c}: '))

print(matriz)

for l in range(0,3):
    print()
    for c in range(0,3):
        print(f'[{matriz[l][c]:^3}]',end='')