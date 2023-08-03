frase = ' Curso Em Vídeo Pyhton '

#seleção de caracteres
print(frase[::2])

#saber quantidade de caracteres
print(len(frase))

#upper: colocar em maiusculo, count: quantas vezes tem 'O'
print(frase.upper().count('O'))

#retirar espaços a frente e atras do texto
print(frase.strip())

#replace: substituir
print(frase.replace('em','de').strip())

#ver se existe uma cadeia de caractere dentro do  objeto
print('Curso' in frase)

#find: posição de algo no objeto;lower: deixar tudo em minusculo
print(frase.lower().find('em'))

#desmontar numa lista
print(frase.split())
lista = frase.split()
#[0] mostra o item '0' da lista; [4] mostra a letra '4' do item '0'
print(lista[0] [4])

#quantidade de um caractere numa string
print(frase.count('E'))

