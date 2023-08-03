fob = None
while fob != 'fim':
    print('-='*40)
    print(f'{"Interactive helping system in Python":^80}')
    print('-='*40)
    fob = input('Função ou Biblioteca: ').strip().lower()
    if fob != "fim":
        help(fob)
print('-='*40)
print('ATÉ LOGO')