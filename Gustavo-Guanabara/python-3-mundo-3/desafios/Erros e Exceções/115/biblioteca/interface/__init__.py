def leiaInt (txt):
    while True:
        try:
            numero = int(input(txt))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número inteiro válido')
        except (KeyboardInterrupt):
            print('O usuário não informou nenhum valor')
            return 0
        else:
            return numero


def linha (largura = 42):
    print('-'* largura)
    
def cabeçalho (txt):
    linha()
    print(txt.center(42))
    linha()

def corpo (lista):
    cont = 1
    for posicao in lista:
        print(f'\033[1;32m{cont}\033[m -- \033[1;34m{posicao}\033[m')
        cont += 1
    opção = leiaInt('Escolha uma opção: ')
    return opção