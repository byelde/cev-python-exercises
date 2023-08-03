a = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão? '))

for n in range (0, 10):
    print(f'{a + r*n} >', end=' ')
print('ACABOU!')