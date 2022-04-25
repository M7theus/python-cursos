from random import randint
from time import sleep

r = randint(0,5)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, você consgue adivinhar em qual vou escolher?')
print('-=-'*20)
n1 = str(input('Pronto? '))
print('Pensando em um número....')
sleep(2)
print('Pronto, já pensei em um')
n2 = int(input('Qual foi? '))
print('Hum.......')
sleep(2)
if n2 == r:
    print('\033[1;32mParabéns, você conseguiu adivinhar!\033[m')
else:
    print('\033[1;33mAh! Não foi dessa vez :0\033[m')
print('O número que tinha pensado era no \033[4;0;43m{}\033[m'.format(r))