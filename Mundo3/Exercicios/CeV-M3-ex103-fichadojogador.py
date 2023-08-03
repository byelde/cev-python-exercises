def ficha(n= '<desconhecido>',g='0'):
    print(f'O jogador {n} fez {g} gols.')


nome = input('Nome: ').capitalize()
gols = input('N° de gols: ')
if gols.strip() == "":
    gols = 0
if nome.strip() == "":
    ficha(g=gols)
else:
    ficha(nome,gols)