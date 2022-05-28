from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
print('Os números sorteados foram: ')
for numero in numeros:
    print(f'{numero}')
#Maneira menos prática:
'''maior = menor = 0
for termo in numeros:
    if termo == 0:
        maior = termo
        menor = termo
    else:
        if termo > maior:
            maior = termo
        elif termo < menor:
            menor = termo
print(f'\nO maior número foi o: {maior}')
print(f'O menor número foi o: {menor}')'''

#Maneira prática:
print(f'\nO maior número é o: {max(numeros)}')
print(f'O menor número é o: {min(numeros)}')

    