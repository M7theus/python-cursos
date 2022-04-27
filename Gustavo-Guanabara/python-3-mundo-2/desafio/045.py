from time import sleep
from random import choice
from emoji import emojize
import emoji
print(emoji.emojize('Que tal um jogo ?:video_game:'))
print('Pedra, Papel ou Tesoura')

opcao = ['Pedra','Papel','Tesoura']
escolha = choice(opcao)
n1 = str(input('Escolha a sua: '))
if n1 == escolha:
    print('Empatou')
elif n1 == 'Pedra' and escolha == 'Tesoura':
    print('Parabéns, vocễ venceu')
elif n1 == 'Pedra' and escolha == 'Papel':
    print('Eu ganhei :0')
elif n1 == 'Papel' and escolha == 'Pedra':
    print('Você venceu')
elif n1 == 'Papel' and escolha == 'Tesoura':
    print('Eu ganhei :0')
elif n1 == 'Tesoura' and escolha == 'Papel':
    print('Você ganhou')
elif n1 == 'Tesoura' and escolha == 'Pedra':
    print('Eu ganhei :0')
print(escolha)