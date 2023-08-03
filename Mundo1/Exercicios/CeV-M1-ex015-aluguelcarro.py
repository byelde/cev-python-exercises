d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km foram rodados? '))
v = d*60 + km*0.15
print('O valor desse aluguel foi R${:.2f}'.format(v))