import moeda

numero = float((input('R$')))

print(f'O {moeda.moeda(numero)} com acréscimo de 10% é {moeda.moeda(moeda.aumentar(numero))}')
print(f'O {moeda.moeda(numero)} com diminuição de 10% é {moeda.moeda(moeda.diminuir(numero))}')
print(f'O dobro de {moeda.moeda(numero)} é {moeda.moeda(moeda.dobro(numero))}')
print(f'A metade de {moeda.moeda(numero,)} é {moeda.moeda(moeda.metade(numero))}')