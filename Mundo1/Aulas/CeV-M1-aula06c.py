n = input('Digite algo: ')
print(type(n))
print('É alfa númerico? {}'.format(n.isalnum()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É um espaço? {}'.format(n.isspace()))
print('É decimal? {}'.format(n.isdecimal()))

