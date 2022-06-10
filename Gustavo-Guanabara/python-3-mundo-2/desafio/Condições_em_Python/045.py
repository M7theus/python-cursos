from random import randint
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0,2)
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Escolha sua opção de jogada: '))
print('-=-' *10)
print('O computador escolheu: \033[1;31m{}\033[m'.format(itens[computador]))
print('O jogador escolheu: \033[1;33m{}\033[m'.format(itens[jogador]))
print('-=-' *10)

if jogador == 0: # Jogador escolheu pedra
    if computador == 0:
        print('Jogo \033[1;34mempatou\033[m')
    elif computador == 1:
        print('O computador \033[1;31mvenceu\033[m')
    else:
        print('O jogador \033[1;32mvenceu\033[m')
    
if jogador == 1: # Jogador escolheu Papel
    if computador == 0:
        print('O jogaodor \033[1;32mvenceu\033[m')
    elif computador == 1:
        print('O jogo \033[1;34mempatou\033[m')
    else:
        print('O computador \033[1;31mvenceu\033[m')
    
if jogador == 2: # Jogador escolheu Tesoura
    if computador == 0:
        print('O computador \033[1;31mvenceu\033[m')
    elif computador == 1:
        print('O jogador \033[1;32mvenceu\033[m')
    else:
        print('O jogo \033[1;34mempatou\033[m')