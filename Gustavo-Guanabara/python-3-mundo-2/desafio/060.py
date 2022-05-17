numero = int(input('Digite um número qualquer para descobrir seu fatorial: '))
soma = numero
mult = 0
a = 0

while a != numero:
    mult = numero * soma
    print('{}! = {}X{} = {}'.format(numero,soma,numero,mult),end = ' ')
    soma -= 1
    a += 1
