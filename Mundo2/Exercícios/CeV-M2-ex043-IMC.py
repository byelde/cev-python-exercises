peso = float(input('Peso [kg]: '))
altura = float(input('Altura [m]: '))
imc = peso/(altura**2)

print(f'O IMC dessa pessoa é {imc:.2f}.')

if imc < 17:
    print('Você está MUITO ABAIXO do peso.')

elif imc >= 17 and imc<18.5:
    print('Você está ABAIXO do peso.')

elif imc >= 18.5 and imc < 25:
    print('Você está no peso IDEAL.')

elif imc >= 25 and imc < 30:
    print('Você está ACIMA do peso.')

elif imc >= 30:
    print('Você esta com OBESIDADE.')

