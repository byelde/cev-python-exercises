n = int(input('Digite um número (1-9999999): '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
dm = n // 10000 % 10
cm = n // 100000 % 10
mm = n // 1000000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print('Dezena de milhar: {}'.format(dm))
print('Centena de milhar: {}'.format(cm))
print('Milhão: {}'.format(mm))