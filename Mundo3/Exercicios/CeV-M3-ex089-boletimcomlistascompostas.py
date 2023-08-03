ta = []
am = []
while True:
    am.append(input('Nome: '))
    am.append(float(input('Nota 1: ')))
    am.append(float(input('Nota 2: ')))
    am.append((am[1]+am[2])/2)
    ta.append(am[:])
    am.clear()
    resp1 = input('\nDeseja continuar? ').upper()    
    if resp1 == 'N':
        break

print('-==-'*20)
print('N° ','NOME       ','MÉDIA')
print('----'*7)
for x in range(0,len(ta)):
    print(f'{x:<4}{ta[x][0]:<12}{ta[x][3]}')
print('----'*7)

while True:
    resp2 = int(input('Mostrar nota de qual aluno? [999 p/ encerrar]: '))
    if resp2 == 999:
        break
    print(f'Notas de {ta[resp2][0]}: {ta[resp2][1]} e {ta[resp2][2]}\n')