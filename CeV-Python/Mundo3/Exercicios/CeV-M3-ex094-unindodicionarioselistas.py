tdsp = []
mulheres_cad = []
dados_pessoais = {}

somaid = 0

while True:
    nome = input('Nome: ')

    while True:
        sexo = input('Sexo [M/F]: ').upper()
        if sexo in 'MF':
            break
        else:
            print('ERRO! Digite apenas "M" ou "F".')

    if sexo == "F":               #ITEM C
        mulheres_cad.append(nome) #ITEM C

    idade = int(input('Idade: '))
    somaid += idade #ITEM B

    dados_pessoais["Nome"] = nome
    dados_pessoais["Sexo"] = sexo
    dados_pessoais["Idade"] = idade

    tdsp.append(dados_pessoais.copy())

    while True:
        resp = input('Quer continuar? [S/N] ').upper()
        if resp == "S" or "N":
            break
        else:
            print('ERRO! Digite apenas "S" ou "N".')
            
    if resp == "N":
        break

print('-='*30)

#ITEM A : TOTAL DE PESSOAS CADASTRADAS
print(f'A) Ao todo temos {len(tdsp)} pessoas cadastradas.')

#ITEM B : A MEDIA DE IDADE
print(f'A média de idade é de {somaid/len(tdsp)} anos.')

#ITEM C : AS MULHERRES CADASTRADAS
print(f'As mulheres cadastradas foram: {mulheres_cad}')

#ITEM D : PESSOAS QUE ESTÃO ACIMA DA MÉDIA DE IDADE
print('As pessoas que estão acima da média são: ')
for item_lista in tdsp:
    if item_lista['Idade'] > (somaid/len(tdsp)):
        print()
        for k, v in item_lista.items():
            print(f'{k} = {v};', end=' ')
