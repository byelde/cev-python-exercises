n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2

print(f'Sua média foi {m}, portanto, você está',end=' ')
if m>7:
    print('APROVADO(A).')
elif m<7 and m>=5:
    print('EM RECUPERAÇÃO.')
else:
    print('REPROVADO(A)')