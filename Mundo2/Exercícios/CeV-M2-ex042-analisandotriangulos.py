l1 = float(input('Valor do primeiro lado: '))
l2 = float(input('Valor do segundo lado: '))
l3 = float(input('Valor do terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses lados PODEM FORMAR um triângulo', end=" ")
    if l1 == l2 == l3:
        print('EQUILÁTERO.')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')

else:
    print('Não é formado um trinângulo.')
