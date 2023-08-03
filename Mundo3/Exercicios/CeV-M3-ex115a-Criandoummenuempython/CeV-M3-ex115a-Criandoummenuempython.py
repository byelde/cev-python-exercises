import os
from arquivo import arquivoexiste, criararquivo
import menu


arq = 'cev.txt'
if not arquivoexiste(arq):
    criararquivo(arq)


lista = []
esc = menu.menu()
while True:
    if esc == 1:
        os.system('cls')
        menu.op1(arq)
    elif esc == 2:
        os.system('cls')
        menu.op2(lista)
    elif esc == 3:
        menu.op3()
        break
    else:
        print('\nDigite um valor válido entre 1 e 3')
    esc = menu.menu()