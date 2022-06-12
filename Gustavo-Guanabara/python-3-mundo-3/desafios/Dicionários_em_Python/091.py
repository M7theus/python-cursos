from random import randint #Números aleatórios
from time import sleep #Dormir
from operator import itemgetter #Organização das listas

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
}
ranking = list()
for keys,values in jogo.items():
    print(f'{keys} tirou o número: {values}')
    sleep(1)
print('-- Ranking dos jogadores --')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for keys,values in enumerate(ranking):
    print(f'{keys+1} --> {values[0]}:      {values[1]}')