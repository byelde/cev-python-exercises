from datetime import date

def voto(x):
    idade = date.today().year - x
    print(f'Sua idade: {idade}')
    if idade < 16:
        return 'NEGADO'
    elif 16 < idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

#principal
resposta = voto(int(input('Ano de nascimento: ')))
print(f'Voto {resposta}')