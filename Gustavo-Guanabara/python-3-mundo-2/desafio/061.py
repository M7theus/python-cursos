numero = int(input('Digite um número qualquer: '))
razao = int(input('Digite a razão: '))

n = 0
a = numero
while n != 9:
    a += razao
    n += 1
    if n == 1:
        print(numero,a, end=' ')
    else:
        print(a,end=' ')
