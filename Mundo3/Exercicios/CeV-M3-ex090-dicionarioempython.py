dados = {}

dados["nome"] = input('Nome: ').capitalize()
dados["media"] = float(input('Média: '))

if dados['media'] < 5:
    dados["situ"] = 'REPROVADO'
elif 5 <= dados['media'] < 7:
    dados["situ"] = 'EM RECUPERAÇÃO'
else:
    dados['situ'] = 'APROVADO'

print('-='*20)
print(f'A situação do(a) estudante {dados["nome"]} é: {dados["situ"]}')