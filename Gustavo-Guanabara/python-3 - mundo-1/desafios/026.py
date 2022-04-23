from itertools import count


n1 = str(input('Digite uma frase qualquer: ')).strip()

n2 = n1.count('A')
n3 = n1.count('a')

a = n1.find('A')
b = n1.find('a') 
d = (n1.rfind('a') - n1.count(' ') - n1.count(','))

print('Sua frase possue um total de {} A'.format(n2))
print('Sua frase possuem um total de {} a'.format(n3))

print('O primeiro *A* aparece na posição {}'.format(a))
print('O *a* aparece na posição {}'.format(b))

print('Última posição que aparece a letra *a* {}'.format(d))