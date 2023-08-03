import moeda

numero = float((input('R$')))

print(f'O {numero} com acréscimo de 10% é {moeda.aumentar(numero)}')
print(f'O {numero} com diminuição de 10% é {moeda.diminuir(numero)}')
print(f'O dobro de {numero} é {moeda.dobro(numero)}')
print(f'A metade de {numero} é {moeda.metade(numero)}')