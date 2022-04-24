n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite outro número inteiro qualquer: '))
n3 = int(input('Digite mais um número inteiro qualquer: '))
if n1 > n2:
    if n1 > n3:
        print('O maior número é {}'.format(n1))
if n2 > n1:
    if n2 > n3:
        print('O maior número é {}'.format(n2))
if n3 > n1:
    if n3 > n2:
        print('O maior número é {}'.format(n3))