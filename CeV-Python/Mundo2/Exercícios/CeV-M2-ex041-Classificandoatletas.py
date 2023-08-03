from datetime import date

anon = int(input('Ano de nascimento: '))
anoa = date.today().year
idade = anoa-anon

print(f'O ateta tem {idade} anos.')

if idade > 4 and idade <= 9:
    print('Classificação:  MIRIM.')

elif idade > 9 and idade <= 14:
    print('Classificação: INAFANTIL.')

elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR.')

elif idade > 19 and idade <=25:
    print('Classificação:  SÊNIOR.') 

elif idade > 25:
    print('Classificação: MASTER.')
    
else:
    print('Idade INVÁLIDA.')