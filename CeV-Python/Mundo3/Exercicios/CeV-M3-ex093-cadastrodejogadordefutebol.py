dados = {'Nome': input("Nome: ")}
qntg = []

nump = int(input(f'Quantos jogos {dados["Nome"]} jogou? '))

for c in range (1,nump+1):
    qntg.append(int(input(f'    Quantos gols na partida {c}? ')))

dados["gols"] = qntg
dados["total"] = sum(qntg)

print('-='*25)
print(dados)
print('-='*25)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*25)
print(f'O jogador {dados["Nome"]} jogou {nump} partidas.')
for c,v in enumerate(qntg):
    print(f'    Na partida {c+1}, fez {v} gol(s).')
print(f'Foi um total de {dados["total"]} gol(s).')