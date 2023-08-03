def menu():
    '''MOSTRA UM MENO COM 3 OPÇÕES E RECEBE
    A ESCOLHA DO USUÁRIO.'''
    while True:
        try:
            print('='*30)
            print(f'{"MENU PRINCIPAL":^30}')
            print('='*30)
            print('1 - Ver pessoas cadastradas')
            print('2 - Cadastrar uma nova pessoa')
            print('3 - Sair do sistema')
            op = int(input('Sua opção: '))
            return op
        except (TypeError,ValueError):
            print('\nDigite um valor válido entre 1 e 3')

def op1(file):
    '''MOSTRA AS PESSOAS CADASTRADAS 
    NA LISTA DECLARADA NA OPÇÃO 2
    menu.op1(list)'''
    print('='*30)
    print(f'{"PESSOAS CADASTRADAS":^30}')
    print('='*30)
    try:
        a = open(file, 'rt')
    except:
        print('Aconteceu algum erro.')
    else:
        print(a.readlines())

def op2(group):
    '''CADASTRA AS PESSOAS NA LISTA DECLARADA
    menu.op2(list)'''
    print('='*30)
    print(f'{"CADASTRADAR NOVA PESSOA":^30}')
    print('='*30)
    group.append(input('Nome: ').capitalize())

def op3():
    '''IMPRIME A IMAGEM DE PROGRAMA SENDO FECHADO'''
    print('\nFechando programa...')