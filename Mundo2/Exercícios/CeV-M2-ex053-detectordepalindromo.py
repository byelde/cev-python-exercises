frase = input('Diga a frase: ').strip().upper() #retirar espaços da frente e trás
palavras =  frase.split() # separar a frase em palavras
junto = ''.join(palavras) # juntar todas as palavras
inverso = '' #criação de variável para frase inversa

for letra in range(len(junto) - 1, -1, -1 ):
    inverso += junto[letra]

print(f'{junto} {inverso}')

if junto == inverso:
    print('É um palindromo.')
else:
    print('NÃO é um palindromo')
