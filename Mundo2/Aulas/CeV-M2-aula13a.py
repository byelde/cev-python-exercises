for x in range(0, 11, 2):
    print(x)
print('-='*20)
for p in range(10, -1, -2):
    print(p)

e = int(input('Quer começar de quanto? '))
n = int(input('Quer contar até quanto? '))
dq = int(input('De quanto em quanto? '))
for c in range(e, n+1, dq):
    print(c)

s = 0
for k in range (0,6):
    n = int(input('Digite um valor: '))
    s += n
print(s)