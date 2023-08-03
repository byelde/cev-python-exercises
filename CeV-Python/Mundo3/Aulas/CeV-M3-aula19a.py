pessoas = {'nome':'Gabryel', 'idade': 18, 'sexo':'M'}

print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['sexo'])

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys()) #mostrar os chave
print(pessoas.values()) #mostra o valor correspondente a cada chave
print(pessoas.items()) #mostra cada chave com seu valor (em forma de tuplas) dentro duma lista

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for i in pessoas.items():
    print(i)

del pessoas['sexo'] #deletar item
pessoas["nome"] = 'Adriano' #alterando valor da chave
pessoas["peso"] = 76 #alterando valor da chave (não precisa do 'append')

for k, v in pessoas.items(): #substitui o enumerate
    print(f'{k} = {v}')

nordeste = []
estado1 = {'UF': 'Alagoas', 'sigla':'AL'}
estado2 = {'UF': 'Pernambuco', 'sigla':'PE'}

nordeste.append(estado1)
nordeste.append(estado2)

print(nordeste[0]['UF'])
print(nordeste[1]['UF'])

estado = {}
nordeste = []

for c in range(0,2):
    estado['UF'] = input('Estado: ')
    estado['sigla'] = input('Sigla: ')
    nordeste.append(estado.copy()) #substitui o [:] das listas para realizar a cópia

for e in nordeste:
    for k, v in e.items():
        print(f'A sigla {k} corresponde ao estado de {v}')

for e in nordeste:
    for v in e.values():
        print(v, end='')
    print()