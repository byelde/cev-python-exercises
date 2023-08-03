vc = float(input('Valor das compras: R$'))
print('''Escolha uma opção de pagamento: 
[1] À vista no dinheiro ou pix;
[2] À vista no cartão;
[3] Em até 2x no cartão;
[4] Em 3x ou mais no cartão. ''')

r = input('Opção: ')

if r in '1 2 3 4':
    print('O valor TOTAL das compras será: R$', end=' ')

    if r == '1':
        print(vc*0.9)

    elif r == '2':
        print(vc*0.95)

    elif r == '3':
        print(vc)
        print(f'Serão 2 parcelas de R${vc/2:.2f}')

    elif r == '4':
        print(vc*1.2)
        p = int(input('Em quantas parcelas? '))
        print(f'Serão {p} parcelas de R${(vc*1.2)/p:.2f}')

else:
    print('Escolha INVÁLIDA. Tente novamente.')

