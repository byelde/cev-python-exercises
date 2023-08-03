'''cont = 1
while cont < 11:
    print(cont)
    cont += 1
print('Fim.')'''
'''cont = 1
while True:
    print(cont)
    cont += 1
print('Fim.')'''

cont = s = 0
while cont != 999:
    cont = int(input(': '))
    if cont == 999:
        break
    s += cont
print(s)