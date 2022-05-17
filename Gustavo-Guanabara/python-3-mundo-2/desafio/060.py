# Com o larço while

'''numero = int(input('Digite um número qualquer para descobrir seu fatorial: '))
n = 1
mult = numero

while n != numero:
    mult *= n
    n += 1
print('{}! = {}'.format(numero,mult))'''

# Com o larço for

numeros = int(input('Digite o número que deseja visualizar seu fatorial: '))
mult = numeros
for numero in range(1,numeros):
    mult *= numero
print('O fatorial do número {} é {}'.format(numeros,mult))