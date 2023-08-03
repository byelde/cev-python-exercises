import math
co = float(input('Qual é o valor do cateto oposto? '))
ca = float(input('Qual é o valor do cateto adjacente? '))
h = math.hypot(ca,co)
print ('A hipotenusa desse triangulo retangulo é {:.2f}'.format(h))