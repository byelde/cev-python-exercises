try: #é obrigatório
    a = int(input('a: '))
    b = int(input('b: '))
    c = a/b

except (ValueError, TypeError): #é obrigatório e pode haver vários
    print('Erro de valor. Digite o tipo certo de variável.')

except ZeroDivisionError: #é obrigatório e pode haver vários
    print('Não é possível realizar uma divisão por zero.')

except KeyboardInterrupt: #é obrigatório e pode haver vários
    print('O usuário abandonou o programa.')

except Exception as ex: #descobrir tipo de erro
    print(type(ex))

else: #é opcional
    print(f'A operação foi um sucesso, resultando em {c}')

finally: #é opcional, ocorre independente de erro ou não
    print('Até mais.')