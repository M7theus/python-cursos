from random import randint
from time import sleep
lista = []
jogos = list()

pergunta = int(input('Quantos jogos serão feitos? '))
for posicao in range(1,pergunta+1):
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('Os jogos sorteados foram: ')
for posicao,valor in enumerate(jogos):
    print(f'Jogo {posicao+1}: {valor}')
    sleep(1)
print('Boa sorte')