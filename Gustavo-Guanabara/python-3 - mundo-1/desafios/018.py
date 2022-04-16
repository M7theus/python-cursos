from math import sin, cos, tan, radians

n1 = float(input('Digite o valor de um ângulo qualquer: '))
s = sin(radians(n1))
c = cos(radians(n1))
t = tan(radians(n1))
print('O ângulo {} tem um:\n-Seno:{:.2f}\n-Cosseno:{:.2f}\n-Tangente:{:.2f}'.format(n1,s,c,t))