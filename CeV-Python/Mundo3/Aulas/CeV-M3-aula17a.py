'''num = (2,3,4,5)
num[3] = 7''' #tupla é imutável

num = [2,3,4,5]
print(num)
num[0] = 3 # MUDANDO VALOR DO ITEM NA POSICÇÃO 0
print('A lista foi alterada para: ', num) #LISTAS são MUTÁVEIS

num.append(6)
print('Adicionando 6 à lista: ', num)

num.sort(reverse=True) #organizando de forma reversa
print('colocando em ordem reversa: ',num)

num.insert(0,1) #colocar naposição 0 o número 1
print(num)