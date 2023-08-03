def leiadinheiro(msg):
    while True:
        p = input(msg).strip().replace(',','.')
        if p.isalpha() or p == "":
            print(f'ERRO. "{p}" não é um preço válido.')
        else:
            return float(p)