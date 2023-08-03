p18 = 0
nhc = 0
mm20 = 0

while True:
    sexo = input('\nSexo: [M/F] ').upper()
    idade = int(input('Idade: '))
    print(f'Dados : Sexo {sexo}, Idade {idade}')

    if  idade > 18:
        p18 += 1

    if sexo == "M":
        nhc += 1

    if sexo == "F" and idade < 20:
        mm20 += 1
    
    resp = input('\nDeseja continuar? [S/N] ').upper()
    if resp == 'N':
        break
    
print(f'\nN° pessoas maiores de 18 anos: {p18}')
print(f'N° homens cadastrados: {nhc}')
print(f'N° mulheres com menos de 20 anos: {mm20}')