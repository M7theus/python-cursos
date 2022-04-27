n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O primeiro número {} é maior do que o {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número {} é o maior do que o {}'.format(n2, n1))
else:
    print('Os dois números são iguais')