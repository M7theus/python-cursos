from math import pow, sqrt, ceil

print('Cateto dos trinângulos')
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
c = sqrt(pow(n1,2) + pow(n2,2))
print('O valor da sua hipotenusa será de: {:.2f} ou {}'.format(c, ceil(c)))