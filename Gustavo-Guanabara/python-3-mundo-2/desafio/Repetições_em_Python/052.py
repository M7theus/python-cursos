numero = int(input('Digite um número qualquer: '))
total = 0

for c in range(1,numero + 1):
    if numero % c == 0:
        print('\033[33m{}\033[m'.format(c), end=' ')
        total += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')

if total == 2:
    print('\nO número {} é primo'.format(numero))
else:
    print('\nO número não é primo')
        