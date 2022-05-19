#Laço while
'''numero = int(input('Digite um número qualquer: '))

contador = numero
mult = 1
print(numero,'! = ',end='')
while contador != 0:
    contador -= 1
    print(' {} '.format(numero),end='')
    print('x' if contador > 0 else ' = ',end='')
    mult *= numero
    numero -= 1
print(mult,end='')'''

#Laço for
'''numeros = int(input('Digite um número qualquer: '))
print(numeros,'!= ',end='')
cont = numeros
mult = 1
for numero in range(1,numeros+1):
    print('{}'.format(cont),end='')
    print(' x' if cont > 1 else ' =',end=' ')
    mult *= cont
    cont -= 1
print(mult,end='')'''

#Função propria
from math import factorial
numero = int(input('Digite um número qualquer: '))
fatorial = factorial(numero)
print('O fatorial de {} é {}'.format(numero,fatorial))