n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 +n2)/2
print('A sua média foi {:.1f}'.format(n))
print('Parabéns' if n>=6 else 'Estude mais')
    