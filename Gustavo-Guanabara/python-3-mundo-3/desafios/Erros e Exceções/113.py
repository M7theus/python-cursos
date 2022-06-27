def leiaInt (txt):
    while True:
        numero = str(input(txt))
        if numero.isnumeric():
            valor = int(numero)
            return numero
        print(f'\033[1;31mERRO! Digite apenas números\033[m')

def LeiaFloat (valor):
    while True:
        numero = str(input(valor))
        if numero // 1 != numero:
            print('Número flutuante')

numero = leiaInt('Digite um número: ')
flutuante = LeiaFloat('Digite um número: ')
print(f'O número informado foi o: {numero},{flutuante}') 