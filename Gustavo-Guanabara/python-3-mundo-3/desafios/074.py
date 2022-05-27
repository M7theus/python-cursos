from random import randint
'''numero = randint(0,10)
lista = (numero, numero,numero,numero,numero)
print(lista)'''

#lista = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os números sorteados foram')
for c in range(0,5):
    a = randint(0,10)
    print(f'{ [a] }',end='')
    if c == 0:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        elif a < menor:
            menor = a
print(end='')
print(f'O maior número é o: {maior}\nE o menor número é o: {menor}')
    