a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o segundo número '))

#teste de menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#teste de maior
maior = a
if b>a and a>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O maior é {maior} e o menor é {menor}')