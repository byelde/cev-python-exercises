def moeda(p=0,m='R$'):
    return f'{m}{p:.2f}'.replace('.',',')

def aumentar(n,taxa = 0, formatar = False):
    ret = n*(1+(taxa/100))
    return ret if formatar == False else moeda(ret)

def diminuir(n,taxa = 0, formatar = False):
    ret = n*(1-(taxa/100))
    return ret if formatar == False else moeda(ret)

def dobro(n, formatar = False):
    ret = n*2
    return ret if formatar == False else moeda(ret)

def metade(n, formatar = False):
    ret = n/2
    return ret if formatar == False else moeda(ret)

def resumo(p=0,a=10,d=5):
    print('-='*20)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-='*20)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p,True)}')
    print(f'Metade do preço: \t{metade(p,True)}')
    print(f'{a}% de aumento: \t{aumentar(p,a,True)}')
    print(f'{d}% de diminuição: \t{moeda(diminuir(p,d))}')