from random import randint
lista = []
jogos = list()

pergunta = int(input('Quantos jogos serão feitos? '))
for posicao in range(1,pergunta+1):
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
        if cont == 5:
            break
        cont += 1
    jogos.append(lista[:])
    lista.clear()
print(jogos)