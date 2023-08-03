maior = 0
menor = 0

for p in range(1,7):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior:.2f}kg e o menor {menor:.2f}kg.')
