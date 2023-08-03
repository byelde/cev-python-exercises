from datetime import date

npma = 0
npme = 0

for contador in range (0,7 ):
    nome = input('Qual é o nome da pessoa? ')
    anon = int(input('Qual é ano de nascimento dessa '))
    idade = date.today().year - anon


    if idade >= 18:
        print('essa pessoa é de MAIOR.')
        npma += 1
    else:
        print('Essa pessoa é de MENOR.')
        npme += 1

print(f'No total, {npma} pessoa(s) é(são) de MAIOR e {npme} é(são) de MENOR')       