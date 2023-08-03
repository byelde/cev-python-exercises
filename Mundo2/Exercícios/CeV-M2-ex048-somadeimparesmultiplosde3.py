somatorio = 0
nvalores = 0

for contador in range (0,501,3):
    if contador % 2 == 1 and contador % 3 == 0:
        somatorio += contador
        nvalores += 1

print(f'O somatório de todos os {nvalores} valores é {somatorio}.')