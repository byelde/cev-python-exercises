somatorio = 0
np = 0

for c in range (1, 7):
    n = int(input(f'{c}° NÚMERO: '))
    if n % 2 == 0:
        somatorio += n
        np += 1

print(f'\nO valor do somatório dos {np} valor(es) par(es) é {somatorio}.') 