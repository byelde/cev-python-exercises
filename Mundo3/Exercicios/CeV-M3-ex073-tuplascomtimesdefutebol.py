brasileiro = ('Bosta Fogo', 'Flamengo', 'Grêmio', 'São Paulo', 'FluminenC',
'Palmeiras', 'Bragantino', 'Athletico-PR', 'Fortaleza', 'Cruzeiro')

print('Os 5 primeiros colocados:', brasileiro[:5])
print('Os 4 últimos colocados: ', brasileiro[-4:])
print(f'Em ordem alfabética:\n{sorted(brasileiro)}')
print('Posição do bragantino: ', brasileiro.index('Bragantino'))