sig = 0 #Soma Idade do Grupo
nm20 = 0 #Número de Mulheres -20 anos

e = int(input('Quantas pessoas há no grupo? '))

for c in range(1, e + 1):
    print(f'---------{c}ª PESSOA--------')
    nome  =  input('NOME da pessoa: ').strip()
    sexo  =  input('SEXO da pessoa [F/M]: ').upper()
    idade =  int(input('IDADE: '))

    sig += idade

    if c == 1 and sexo == 'M':
        ihmv = idade #IDADE Homem Mais Velho
        nhmv = nome #NOME Homem Mais Velho
    
    if sexo == 'M':
        if idade > ihmv:
            ihmv = idade
            nhmv = nome
    
    if sexo == 'F' and idade < 20:
        nm20 += 1
    print(' ')

mig = sig/e #MÉDIA IDADE do Grupo
print(f'A média de idade desse grupo é de {mig} anos.')
print(f'O número de mulheres com menos de 20 anos é {nm20}.')
print(f'O homem mais velho é o {nhmv}, com {ihmv} anos')