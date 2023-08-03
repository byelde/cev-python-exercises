from random import randint

num_vitorias = 0

while True:
    lado_jogador = input('PAR ou ÍMPAR? ').upper()
    num_maq = randint(1,10)
    num_jogador = int(input(': '))
    total = num_maq + num_jogador
    poui = total%2

    print(f'A máquina escolheu {num_maq}.')

    if (lado_jogador == 'P' and poui == 0) or (lado_jogador == 'I' and poui == 1):
        print('\nVITÓRIA!!!')
        num_vitorias += 1
    else :
        print('\nDerrota.')
        break
print(f'Número de vitórias seguidas: {num_vitorias}')
