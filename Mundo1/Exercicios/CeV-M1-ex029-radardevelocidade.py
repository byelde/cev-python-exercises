velocidade = float(input('Qual era a velocidade do carro? '))
lim = 80
if velocidade>80:
    multa = (velocidade-80)*7
    print(f'Você ultrapassou o limite de 80Km/h\nVocê deve pagar uma multa de R${multa:.2f}')
    print('Dirija com cuidado.')
else:
    print('Você estava dentro da velocidade permitida. Muito bem!')