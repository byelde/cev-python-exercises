L = float(input('Qual é a largura da sua parede? '))
A = float(input('Qual é a altura da sua parede? '))
#quantidade de tinta 0.5L/1m^2
qtt =  (L*A)/2
print('As medidas da sua parede são {}x{}m'.format(L,A))
print('A quantidade de tinta necessária será {:.2f}L'.format(qtt))