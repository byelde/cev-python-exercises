while True:
    c = 1
    n = int(input('\nTabuada de: \n'))
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c}= {n*c}')
        c += 1
print('FINALIZANDO...')