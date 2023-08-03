n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua nota foi {m}')
if m<6:
    print('Você foi reprovado.')
else:
    print('Você foi aprovado.')