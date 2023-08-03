import math
ang = float(input('Digite o valor do angulo: '))
angR = math.radians(ang)
print('Para o ângulo {}:\nO valor do seno é: {:.2f}\nO valor do cosseno é: {:.2f}\nO valor da tangente é: {:.2f}'.format(ang,math.sin(angR),math.cos(angR),math.tan(angR)))