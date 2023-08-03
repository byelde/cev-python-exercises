def somar(a=0,b=0,c=0):
    """
    -> faz as soma entre os três parametros e printa o resultado;
    :param a, b, c : variáveis da operação;
    :return: sem retorno
    """
    s = a + b + c
    return s


help(somar)
x = int(input('N1:'))
y = int(input('N2:'))
z = int(input('N3:'))

r1 = (somar(x,y)) #funciona como se r1 = s (escopo local)
r2 = (somar(x))
r3 = somar(x,y,z) #faz as respectivas ligações em ordem
r4 = somar(c=x,a=y) #segue a ordem expressada

print(f'As somas valem {r1}, {r2}, {r3} e {r4}')