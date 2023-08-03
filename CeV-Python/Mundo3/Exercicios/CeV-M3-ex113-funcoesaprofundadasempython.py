def leiaint(msg):
    while True:
        try:
            num = int(input(msg).strip())
        except (ValueError,TypeError):
            print('\033[0;31mERRO. Digite um inteiro número válido.\033[m')
            continue
        else:
            return num

def leiareal(msg):
    while True:
        try:
            num = input(msg).strip()
            return float(num)
        except:
            print('\033[0;31mERRO. Digite um real número válido.\033[m')

#Programa Principal
i = leiaint('Número inteiro: ')
print(f'Você digitou o número inteiro: {i}.')

r = leiareal('Número real: ')
print(f'Você digitou o número real: {r}.')