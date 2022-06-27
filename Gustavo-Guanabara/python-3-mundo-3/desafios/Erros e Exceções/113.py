def leiaInt (txt):
    while True:
        try:
            numero = str(input(txt))
            int(numero)
            if numero.isnumeric():
                return numero
        except (ValueError, TypeError):
            print('Ocorreu um problema de dado')
        except ZeroDivisionError:
            print('Não é possível dividir um número por zero')
        except KeyboardInterrupt:
            print('O usuário não digitou')

def LeiaFloat(valor):
    while True:
        try:
            numero = str(input(valor))
            float(numero)
            if numero.isnumeric():
                return numero
        except (ValueError, TypeError):
            print('Ocorreu um problema de dado')
        except ZeroDivisionError:
            print('Não é possível dividir um número por zero')
        except KeyboardInterrupt:
            print('O usuário não digitou')
        


numero = leiaInt('Digite um número: ')
numero = LeiaFloat('Informe um valor flutuante: ')
print(f'O número informado foi o: {numero}') 