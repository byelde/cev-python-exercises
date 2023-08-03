def maior(*n):
    for c in n:
        print(c, end=" ")
    print()
    maior = 0
    for c in n:
        if c == 0:
            maior = c
        if c > maior:
            maior = c
    if len(n) != 0:
        print(f'Foram exibidos {len(n)} valores e o maior foi {maior}')
    else:
        print('Não foi exibido nenhum valor.')

#programa principal
maior(2,1,5,8,3)
maior()