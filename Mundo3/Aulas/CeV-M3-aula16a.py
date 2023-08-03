lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) #sorted = em ordem
print('Lanche 3: ', lanche[3])
print('Lanche -3: ', lanche[-3])
print('lanche [1:]: ',lanche [1:])
print('lanche [:2]: ',lanche [:2])
print('lanche[:-2]: ',lanche[:-2])
print('lanche[-2:]: ',lanche[-2:])

print('-='*35)

print('len(lanche): ',len(lanche)) #qnt de termos

print('-='*35)

for comida in lanche: #mostra cada item na tupla
    print(comida, end=' ')

print('\n','-='*35)

for pos, comida in enumerate(lanche): #mostra cada item na tupla e a posição I
    print(comida, f'na posição {pos}')

print('-='*35)

for cont in range (0, len(lanche)): #mostra cada item na tupla e a posição I
    print(lanche[cont], f'na posição {cont}')

print('-='*35)

almoço = ('Arroz', 'Feijão', 'Carne')
#organizam de formas diferentes (abaixo)
refeicao1 = almoço + lanche
refeicao2 = lanche + almoço 
print(refeicao1)
print('/'*35)
print(refeicao2)

print(refeicao1.index('Feijão')) #mostrar posição na tupla
print(refeicao1.count('Pizza')) #contar qunatas vezes aparece na tupla

del(refeicao2) #deletar algo (nesse caso, foi a tupla)