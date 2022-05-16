from random import randint
from time import sleep

computador = randint(0,10)
print('Irei pensar em um número entre 0 e 10. Você consegue adivinhar? ')
sleep(1)

usuario = 0
tentativa = 0
while usuario != computador:
    usuario = int(input('Digite seu número: '))
    if usuario != computador:
        print('Não foi dessa vez, tente novamente')
    tentativa += 1
    
print('Parabéns! Você acertou. Porém, você precisou de um total de {} tentativas'.format(tentativa))