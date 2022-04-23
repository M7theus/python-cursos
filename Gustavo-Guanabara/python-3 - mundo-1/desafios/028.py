from random import randint
from time import sleep

r = randint(0,5)

print('Vou pensar em um número entre 0 e 5, você consgue adivinhar em qual vou escolher?')
n1 = str(input('Pronto? '))
print('Pensando em um número....')
sleep(1)
print('Pronto, já pensei em um')
n2 = int(input('Qual foi? '))
print('Hum.......')
sleep(1.1)
if n2 == r:
    print('Parabéns, você conseguiu adivinhar!')
else:
    print('Ah! Não foi dessa vez :0')
print('O número que tinha pensado era no {}'.format(r))