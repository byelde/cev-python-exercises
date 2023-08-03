lista = []

for contador in range (0,5):
    lista.append(int(input('Digite um valor: ')))

print(lista)
print(f'Maior valor: {max(lista)}\nMenor valor: {min(lista)}')