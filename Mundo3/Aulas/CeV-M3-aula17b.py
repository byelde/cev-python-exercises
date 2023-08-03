'''pessoa = []
print('1°s dados da lista "Pessoa"')
pessoa.append('Gabryel')
pessoa.append(18)
print(pessoa)

galera = []
galera.append(pessoa[:]) #adicionando uma lista dentro da outra. O ':' representa uma cópia, NÃO uma ligação.
print(f'\ngalera : {galera}')

pessoa[0] = 'Emylle'
pessoa[1] = 17
print(f'\nNovos dados da lista "pessoa": {pessoa}')

galera.append(pessoa[:]) #adiciionando novos dados dentro da lista (Não exclue os dados anteriores)
print(f'\nAtualização da lista "galera": {galera}')

pessoal = [['Gabryel', 18],['Luiza', 17],['Mika', 16],['Gueu', 16],['Samu', 21]]
print(f'\nPessoal: {pessoal}')
print(pessoal[1])
print(pessoal[1][0]) #selecionando sublista, termo da sublista
print(pessoal[1][1])

for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos.')'''

galera = []
dados = []

for pessoa in range(0,3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
    else:
        print(f'{pessoa[0]} é mienor de idade.')
