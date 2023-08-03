vc = float(input('Qual é o valor da casa? R$'))
sal = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos o imóvel será financiado? '))

if vc/(anos*12) > sal*0.3:
    print('Empréstimo NEGADO.')
else:
    print('empréstimo aceito.')
    
print(f'Para pagar o empréstimo de uma casa de R${vc:.2f} em {anos} anos', end=' ')
print(f'será preciso para parcelas de R${(vc/(anos*12)):.2f}')
print(f'O valor máximo das parcelas é R${(sal*0.3):.2f}')