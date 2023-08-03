n = int(input('Número: '))
no = n
fat = 1

while n != 1:
    print(f'{n}x', end='')
    fat = fat*n
    n -= 1
print(f'1 = {fat}')