def leiaInt (txt):
    while True:
        try:
            numero = int(input(txt))
        except (ValueError, TypeError):
            print('Ocorreu um problema de dado')
        except (KeyboardInterrupt):
            print('O usuário não digitou nenhum valor')
            return 0
        else:
            return numero

def LeiaFloat(valor):
    while True:
        try:
            numero = float(input(valor))
        except (ValueError, TypeError):
            print('Ocorreu um problema de dado')
        except (KeyboardInterrupt):
            print('O usuário não digitou nehum valor')
            return 0
        else:
            return numero
        


n1 = leiaInt('Digite um número: ')
n2 = LeiaFloat('Informe um valor flutuante: ')
print(f'O número informado foi o: {n1},{n2}') 