from random import randint
numeros = list()

def sorteio(lista):
    for posicao in range(0,5):
        numeros.append(randint(1,10))
    print('Os valores sorteados foram: ')
    print(numeros)

sorteio(numeros)

def somaPar(lista_soma):
    soma = 0
    for posicao in numeros:
        if posicao % 2 == 0:
            soma += posicao
    print(f'A soma dos números pares da lista: {numeros} é: {soma}')

somaPar(numeros)