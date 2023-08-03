'''for c in range (1,4):
    print(c)
print('Fim.')'''

'''c = 1
while c < 4:
    print(c)
    c += 1
print('Fim.')'''

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    

print(f'O número de pares foi {par} e o número de ímpares foi {impar}.')
print('Fim.')

'''r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = input('Quer continuar? [S/N] ').upper()
print('Fim.')'''