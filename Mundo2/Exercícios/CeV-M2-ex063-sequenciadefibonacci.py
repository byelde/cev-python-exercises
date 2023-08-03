c = 3 #contador
n1, n2 = 0, 1

nt = int(input(': ')) #n° de termos

if nt == 1:
    print('0 -> FIM.')

elif nt == 2:
    print('0 -> 1 -> FIM.')

else :
    print(f'{n1} -> {n2} -> ', end = '')
    while c < nt + 1:
        n3 = n1 + n2
        print(f'{n3} -> ', end='')
        n1 = n2
        n2 = n3
        c += 1
    print('FIM.')