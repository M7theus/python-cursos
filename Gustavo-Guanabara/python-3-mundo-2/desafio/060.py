numero = int(input('Digite um número qualquer para descobrir seu fatorial: '))
n = numero
soma = 0

while n != 0:
    conta = numero * n
    soma += conta
    print(numero,'! = {}X{}= {}'.format(numero,numero,n,soma))
    n -= 1