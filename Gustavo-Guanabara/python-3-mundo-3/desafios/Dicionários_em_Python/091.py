from random import randint
from time import sleep
dados = dict()
lista = list()

for posicao in range(1,5):
    numero = randint(1, 6)
    print(f'O jogador{posicao} tirou: {numero}')
    dados[f'jogador{posicao}'] = numero
    sleep(1)
    
lista.append(dados.copy())
print('Ranking dos jogadores: ')
numero = 1
for posicao in lista:
    for keys,values in posicao.items():
        print(f'{numero}o lugar: {keys} com {values}')
        numero += 1