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

def moeda(p=0,m='R$'):
    return f'{m}{p:.2f}'.replace('.',',')