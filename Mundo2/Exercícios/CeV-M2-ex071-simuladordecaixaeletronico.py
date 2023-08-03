valor = int(input(': R$'))

qtd50 = valor // 50
valor -= qtd50*50

qtd20 = valor//20
valor -= qtd20*20

qtd10 = valor//10
valor -= qtd10*10

qtd1 = valor

print(f'''Serão:
{qtd50} notas de R$50,00
{qtd20} notas de R$20,00
{qtd10} notas de R$10,00
{qtd1} notas de R$1,00''')
