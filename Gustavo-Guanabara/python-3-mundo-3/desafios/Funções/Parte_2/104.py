'''def leiaInt(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            return n
            break
        print(f'Erro! Digite um número inteiro')
    
    
    
numero = leiaInt('Digite um número: ')  
print(f'O número informado foi o {numero}') '''


def leiaInt (txt):
    while True:
        numero = str(input(txt))
        if numero.isnumeric():
            valor = int(numero)
            return numero
        print(f'\033[1;31mERRO! Digite apenas números\033[m')


numero = leiaInt('Digite um número: ')
print(f'O número informado foi o: {numero}') 