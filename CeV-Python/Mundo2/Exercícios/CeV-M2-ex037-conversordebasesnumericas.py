número = int(input('Digite um número: '))

print('''EScolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{número} em base BINÁRIA é {bin(número)[2:]}.')

elif opção == 2:
    print(f'{número} em base OCTAL é {oct(número)[2:]}.')

elif opção == 3:
    print(f'{número} em base HEXADECIMAL é {hex(número)[2:]}.')

else:
    print('Opção iinválida. Tente novamente.')