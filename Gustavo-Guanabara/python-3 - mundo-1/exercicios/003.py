n1 = input('Qual é seu nome: ')
print('Prazer em te conhecer {:20}'.format(n1))
print('Prazer em te conhecer {:>20}'.format(n1))
print('Prazer em te conhecer {:<20}'.format(n1))
print('Prazer em te conhecer {:^20}'.format(n1))
print('Prazer em te conhecer {:=^20}'.format(n1))

n2 = int(input('Um valor: '))
n3 = int(input('Outro valor:'))
s = n2 + n3
s1 = n2 - n3
m = n2 * n3
d = n2 / n3
p = n2 ** n3
di = n2 // n3
r = n2 % n3
print('A soma vale {}\n a subtração vale {}\n a multiplicão vale {}\n e a divisão vale {:.3f}\n'.format(s,s1,m,d),end='')
print('Potência {:.3f}\n divisão inteira {:.3f} e resto {:.3f}\n'.format(p,di,r))