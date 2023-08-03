candidatos = []
todos_candidatos = []
p_mais_pes = p_menos_pes = ''
tcad = 0

while True:
    candidatos.append(input('Nome: '))
    candidatos.append(float(input('Peso(kg): ')))
    todos_candidatos.append(candidatos[:])
    candidatos.clear()

    tcad += 1

    resp = input('Deseja continuar? ').upper()
    if resp == "N":
        break

for p, pessoa in enumerate(todos_candidatos):
    if p == 0:
        pmaior = pessoa[1]
        pmenor = pessoa[1]
        
    if pessoa[1] >= pmaior:
        pmaior = pessoa[1]
        p_mais_pes = pessoa[0]

    if pessoa[1] <= pmenor:
        pmenor = pessoa[1]
        p_menos_pes = pessoa[0]
            
print(f'O total de candidatos foi {tcad}.')
print(f'O maior peso foi {pmaior}kg de {p_mais_pes}.')
print(f'O menor peso foi {pmenor}kg de {p_menos_pes}.')