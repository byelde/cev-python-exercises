def contador(i,f,p):
    if i < f:
        for c in range(i,f+1,p):
            print(c,end=' ')
    if i > f:
        for c in range(i,f-1,p):
            print(c,end=' ')
    print()

def linha():
    print('-='*20)


linha()
contador(1,10,1)
linha()
contador(10,0,-2)
linha()

s = int(input(f'{"Início: ":<8}'))
e = int(input(f'{"Fim: ":<8}'))
d = int(input(f'{"Passo: ":<8}'))

linha()
contador(s,e,d)
linha()