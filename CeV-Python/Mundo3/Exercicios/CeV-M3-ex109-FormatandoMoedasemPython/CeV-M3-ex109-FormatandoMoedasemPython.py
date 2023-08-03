import moeda

numero = float((input('R$')))
variação = float(input('Variação: '))

print(f'O {moeda.moeda(numero)} com acréscimo de 10% é {moeda.aumentar(numero,variação,True)}')
print(f'O {moeda.moeda(numero)} com diminuição de 10% é {moeda.diminuir(numero,variação,True)}')
print(f'O dobro de {moeda.moeda(numero)} é {moeda.dobro(numero, True)}')
print(f'A metade de {moeda.moeda(numero,)} é {moeda.metade(numero, True)}')