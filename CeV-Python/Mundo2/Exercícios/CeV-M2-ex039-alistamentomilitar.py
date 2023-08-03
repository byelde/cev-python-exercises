from datetime import date

anon = int(input('Ano de nascimento: '))
anohj = date.today().year
idade = anohj-anon

if idade < 18:
    print(f'Você tem {idade} anos. Você deverá se alistar em {anon+18}, daqui a {(anon+18)-anohj} ano(s).')

elif idade == 18:
    print(f'Esse ano você completará 18 anos. Deve se alistar IMEDIATAMENTE.')
    
else:
    print(f'Você tem {idade} anos. Você deveria ter se alistado em {anon+18}, {anohj-(anon+18)} ano(s) atrás.')