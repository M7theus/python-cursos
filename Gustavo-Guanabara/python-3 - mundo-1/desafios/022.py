from itertools import count


print('Nome')
n1 = str(input('Por favor, digite seu nome completo: ')).strip()

print('Letras maísculas --> {}'.format(n1.upper()))

print('Letras minúsculas --> {}'.format(n1.lower()))

print('Total de letras sem espaço --> {}'.format(len(n1)-n1.count(' ')))

n2 = n1.split()
print('Primeira parte do nome --> {}'.format(len(n2[0])))