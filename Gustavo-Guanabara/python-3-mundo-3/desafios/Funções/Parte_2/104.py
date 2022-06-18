def leiaInt (txt):
    while True:
        valor = input(txt)
        int(valor)
        if -1 >= valor >= 0:
            return valor
            break
        print('\033[1;31mERRO! Digite apenas números\033[m')
        str(valor)
    
numero = leiaInt('Digite um número: ')
print(f'Você digitou o número: {numero}')