from random import randint
computador = randint(0,10)
print('Vou pensar em um número entre 0 e 10')
print('Você consegue adivinhar?')
usuario = int(input('Digite o número: '))
tentativas = 0

while usuario != computador:
    if usuario > computador:
        print('Menor')
    else:
        print('Maior')
    usuario = int(input('Digite novamente: '))
    tentativas += 1
print('Você teve um total de {} tentativas. Parabéns'.format(tentativas))