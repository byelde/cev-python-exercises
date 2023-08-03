nome = input('Digite o nome: ').strip().upper()
print('A quantidade de As é {}'.format(nome.count('A')))
print('A última letra A está na posição {}'.format(nome.rfind('A')+1))
print('A primeira letra A está na posição {}'.format(nome.find('A')+1))