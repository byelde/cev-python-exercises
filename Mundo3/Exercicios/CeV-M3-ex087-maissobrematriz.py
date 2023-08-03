matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = 0
s3c = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'V{l,c}: '))
        
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

        if c == 2:
            s3c += matriz[l][c]

        if l == 1:
            if c == 0:
                maior2l = matriz[l][c]
            if matriz[l][c] > maior2l:
                maior2l = matriz[l][c]

print()

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print()

print(f'A soma dos valores pares é: {spar}')
print(f'A soma dos valores da 3° coluna é: {s3c}')
print(f'O maior valor da segunda linha é: {maior2l}')