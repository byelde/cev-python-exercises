def aumentar(n):
    return n*1.1

def diminuir(n):
    return n*0.9

def dobro(n):
    return n*2

def metade(n):
    return n/2

def moeda(p=0,m='R$'):
    return f'{m}{p:.2f}'.replace('.',',')