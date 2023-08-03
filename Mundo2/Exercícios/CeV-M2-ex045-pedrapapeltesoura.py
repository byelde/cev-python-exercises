from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
em = randint(0,2)
ej = int(input('''ESCOLHA:
[0] PEDRA
[1] PAPEL
[2] TESOURA
:'''))

if ej != 0 and ej != 1 and ej != 2:
    print('Jogada INVÁLIDA.')

else:
    print(f'Eu escolhi {itens[em]} e você escolheu {itens[ej]}.')

    # POSSIBILIDADE MÁQUINA CAMPEÃ.
    if em == 1 and ej == 0:
        print('EU venci! HAHAHA!')

    elif em == 0 and ej == 2:
        print('EU venci! HAHAHA!')

    elif em == 2 and ej == 1:
        print('EU venci! HAHAHA!')

    # POSSIBILIDADES JOGADOR CAMPEÃO
    elif em == 0 and ej == 1:
        print('Você venceu :(')

    elif em == 2 and ej == 0:
        print('Você venceu :(')

    elif em == 1 and ej == 2:
        print('Você venceu :(')

    # EMPATE
    else:
        print('EMPATE. VAMOS DENOVO!')