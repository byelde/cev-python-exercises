c = 0
t1, t2 = 0, 1

nt = int(input('Quantos termos deseja ver? ')) #n° de termos

if nt > 0:
    print('Valor inválido.')

    if nt == 1:
        print('0 -> FIM.')

    else :
        while c < nt:
            print(f'{t1} ->', end = ' ')
            n3 = t1 + t2
            t1 = t2
            t2 = n3
            c += 1
        print('FIM.')
else:
    print('Valor inválido. Tente novamente.')