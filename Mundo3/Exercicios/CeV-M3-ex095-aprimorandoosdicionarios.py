team = []
while True:
    players = {"Nome": input('Nome: '),
               "NP": int(input('NP: '))}
    goals = []


    for contador in range(1,players["NP"]+1):
        goals.append(int(input(f'   Quantos gols ele fez na {contador}ª partida? ')))
    
    players["Gols"] = goals[:]

    print(players)

    team.append(players.copy())
    players.clear()

    while True:
        resp = input('Deseja continuar? [S/N] ').upper()
        if resp not in "SN":
            print('ERRO! Digite apenas "S" ou "N".')
        else:
            break
    if resp == "N":
        break
print(players)
print(team)


'''print('-='*25)
print(dados)
print('-='*25)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*25)
print(f'O playersador {dados["Nome"]} playersou {nump} partidas.')
for c,v in enumerate(qntg):
    print(f'    Na partida {c+1}, fez {v} gol(s).')
print(f'Foi um total de {dados["total"]} gol(s).')'''