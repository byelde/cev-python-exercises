'''def num(*n): # "*" = num de parametros indeterminados. coloca os valores em uma TUPLA
    for v in n:
        print(v, end=" > ")

    print(f'\nrecebi os valores {n} e foram, ao todo, {len(n)} valores.') #trata cada tupla por vez

num(1,2,1)
num(9,3,11,8)
num(1,3,2)
num(0)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

valores = [1,2,1]
dobra(valores)
print(valores)