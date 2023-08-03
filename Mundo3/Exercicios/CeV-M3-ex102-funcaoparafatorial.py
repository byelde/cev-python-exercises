def fatorial(x,show=False):
    """
    -> Calcula o fatorial de um número, retornando o valor de fatorial
    e, se preciso, mostrar o cálculo (se show = True)
    :param x: valor a ser processado
    :param f: acumula o valor do fatorial
    :param show: mostra cálculo
    :return: retorna o valor do fatorial
    """
    f = 1
    for c in range(x,0,-1):
        f *= c
        if show:
            if c == 1:
                print(f'{c} = ',end='')
            else:
                print(f'{c} x', end=" ")
    return f

print('-='*20)
print(fatorial(5, show=True))
print('-='*20)
help(fatorial)