n = (int(input('N: ')),
     int(input('N: ')),
     int(input('N: ')),
     int(input('N: ')),)

print(f'O 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O 3 apareceu na posição {n.index(3)+1}')
else:
    print('O valor 3 não apareceu na tupla.')
print('Os números pares foram ', end ='')
for a in n:
    if a % 2 == 0:
        print(a, end =' ')