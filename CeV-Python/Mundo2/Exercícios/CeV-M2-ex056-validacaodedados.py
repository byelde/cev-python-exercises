r = 'x'

while r != 'M' and r != 'F':
    r = input('\nQual é o seu sexo? [M/F] ').upper()
    if r != 'M' and r != 'F':
        print('ERRO. Tente novamente.')
        
print('Entendi.')