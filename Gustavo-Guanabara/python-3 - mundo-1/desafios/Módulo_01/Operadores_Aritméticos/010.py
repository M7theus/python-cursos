print('COnersão real para dolar ')
n1 = float(input('Digite o valor em R$ que você possue em carteria: '))
print('Considerando US$ = 1.00 --> R$ 3.27')
c = n1/3.27
print('Com R${}, você consegue comprar US${:.2f}'.format(n1,c))