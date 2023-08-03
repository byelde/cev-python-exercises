from calendar import isleap
ano = isleap(int(input('Escolha um ano qualquer: ')))
print('Esse ano É bissexto.' if ano == True else 'Esse ano NÃO É bissexto.')
