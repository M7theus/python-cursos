def leiaInt (txt):
    while True:
        numero = str(input(txt))
        if numero.isnumeric():
            valor = int(numero)
            return numero
        print(f'\033[1;31mERRO! Digite apenas números\033[m')

cont = 0
while True:
    numero = str(input('Digite um número: '))
    cont += 1
    if numero.isnumeric():
        if (numero // 1 == numero):
            print('Número inteiro')
        else:
            print('Número flutuante')
    if cont == 2:
        break
'''numero = leiaInt('Digite um número: ')
print(f'O número informado foi o: {numero}') '''