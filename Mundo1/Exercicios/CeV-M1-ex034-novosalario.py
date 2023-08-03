salario = float(input('Qual é o salário da pessoa em questão? R$'))
print(f'O salario dessa pessoa será R${salario*1.15 if salario<=1500 else salario*1.1}')