n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite outro número inteiro qualquer: '))
n3 = int(input('Digite mais um número inteiro qualquer: '))
if n1 > n2 and n1 > n3:
    print('O maior número é o {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior número é o {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior número é o {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor número é o {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor número é o {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor número é o {}'.format(n3))
