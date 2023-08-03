lista_palavras = ('python', 'computer', 'mouse', 'programming', 'wi-fi', 'java', 'smartphone')

for palavra in lista_palavras:
    print(f'\nNa palavra "{palavra.upper()}" existe:', end =' ')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')