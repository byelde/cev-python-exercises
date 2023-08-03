lista = []
resp = ''

while True:

    if resp == 'N': #estrutura auxiliar do segundo While
        break

    lista.append(int(input('Digite um valor: ')))

    while True: #enquanto n houver resposta válida, a pergunta será refeita
        resp = input('\nDeseja continuar? [S/N]').upper()
        if resp == 'N':
            break # esse break com resp = N levará ao primeiro break, encerrando o programa
        elif resp == 'S':
            break
        else:
            print('\nErro. Resposta inválida.\n') #avancará para a pergunta novamente
        
print(f'O número de elementos é {len(lista)}')
print(f'Os valores em ordem decrescente: {sorted(lista, reverse=True)}')
print('Existe 5 na lista:',5 in lista)