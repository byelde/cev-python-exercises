'''km = float(input('O destino está a quantos quilômetros? '))
if km<=200:
    print(f'A viagem custará R${km*0.5:.2f}')
else:
    print(f'A viagem custrá R${km*0.45:.2f}')'''

km = float(input('O seu destino está a quantos quilômetros? '))
preco = km*0.5 if km<=200 else km*0.45
print(f'O preço da passagem será R${preco:.2f}')