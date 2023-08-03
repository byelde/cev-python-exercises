from datetime import date

ano = int(input('Digite um ano qualquer (0 para esse ano): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Esse ano ({ano}) É bissexto.')
else:
    print(f'Esse ano ({ano}) NÃO É bissexto.')