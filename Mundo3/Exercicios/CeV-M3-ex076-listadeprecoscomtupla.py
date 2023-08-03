lista = ('Lápis', 2.50,
         'Caneta', 3.50,
         'Caderno', 35.90,
         'Estojo', 12.90,
         'Régua', 5.70)

print('-=-'*11)
print(f'{"TABELA DE PREÇOS":^33}')
print('-=-'*11)

for item in range (0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:-<25}', end ='')
    else:
        print(f'R${lista[item]:>6.2f}')