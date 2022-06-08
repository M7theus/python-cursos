from random import randint
from time import sleep
lista = list()
pergunta = int(input('Quantos jogos você quer que eu sortei? '))
print(f'Sorteando { pergunta :=> 10} jogos')


for posicao in range(0,pergunta):
    b = -1
    jogo = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    for a in enumerate(jogo):
        while a[1] == jogo[b]:
            jogo[b] = randint(0, 60)
        b += 1
    lista.append(jogo[:])
    for jogos in lista:
        jogos.sort()
        print(f'Jogo {posicao +1}: {jogos}')
        sleep(1)
    lista.clear()
print('Boa sorte!')