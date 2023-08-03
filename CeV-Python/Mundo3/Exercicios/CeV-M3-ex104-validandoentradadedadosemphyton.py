def leiaint(msg):
    while True:
        num = input(msg).strip()
        if num.isnumeric():
            return int(num)
        else:
            print('\033[0;31mERRO. Digite um inteiro número válido.\033[m')

#Programa Principal
n = leiaint('Número: ')
print(f'Você digitou o número: {n}.')