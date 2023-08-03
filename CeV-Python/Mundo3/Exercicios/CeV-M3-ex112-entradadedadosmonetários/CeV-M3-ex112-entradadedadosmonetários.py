from utilidadescev import moeda
from utilidadescev import dado

numero = dado.leiadinheiro('Digite o preço: ')
acrescimo = float(input('Acréscimo: '))
dimi = float(input('Diminuição: '))
moeda.resumo(numero,acrescimo,dimi)