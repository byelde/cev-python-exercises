from datetime import date

dados = {"Nome": input('Nome: ').capitalize(),
         "anon" : int(input('Ano de nascimento: ')),
         "CTPS": int(input('Carteira de Trabalho (0 NÃO tem): '))}

if dados["CTPS"] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = int(input('Salário: R$'))
    dados['Aposentadoria'] = ((dados['Contratação'] - dados['anon']) + 35)

dados["Idade"] = (date.today().year - dados['anon'])

print()

for k, v in dados.items():
    print(f'{k} tem valor {v}')