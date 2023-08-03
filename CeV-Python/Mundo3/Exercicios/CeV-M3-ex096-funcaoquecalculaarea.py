def area (a,b):
    S = a*b
    print(f'A área {a:.2f}x{b:.2f} é igual a {S:.2f}m^2')


l = float(input('Largura[m]: '))
c = float(input('Comprimento[m]: '))
area(l,c)