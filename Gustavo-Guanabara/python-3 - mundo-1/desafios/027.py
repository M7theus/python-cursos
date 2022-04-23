n1 = str(input('Digite seu nome completo: ')).strip()
n2 = n1.split()

print('A primeira parte do nome é {}'.format(n2[0]))
print('A última parte do nome é {}'.format(n2[len(n2)-1]))