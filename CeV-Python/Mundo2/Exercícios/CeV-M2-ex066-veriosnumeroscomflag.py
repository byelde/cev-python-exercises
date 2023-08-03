n = soma = 0

while n != 999:
    n = int(input('Digite um valor [999 p/ parar]: '))
    if n == 999:
        break
    soma += n
print(soma)