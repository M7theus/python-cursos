from random import sample

n1 = str(input('Primeiro grupo: '))
n2 = str(input('Segundo grupo: '))
n3 = str(input('Terceiro grupo: '))
n4 = str(input('Quarto grupo: '))
print('A ordem de apresentação dos grupos será: {}'.format(sample([n1,n2,n3,n4], k=4)))