lista = []

for contador in range (0,5):
    lista.append(int(input('Digite um valor: ')))

    if contador == 0:
        maior = lista[contador]
        menor = lista[contador]
    else:
        if lista[contador] > maior:
            maior = lista[contador]
        if lista[contador] < menor:
            menor = lista[contador]

print(f'\n{lista}')
print(f'\nO maior número foi o {maior}\nO menor número foi {menor}')