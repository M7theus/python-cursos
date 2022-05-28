termo = (int(input('Digite um número: ')),int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'\nOs valores digitados foram: {termo}')
print(f'\nO valor 9 apareceu {termo.count(9)}')
if 3 in termo:
    print(f'\nO valor 3 foi digitado na posição: {termo.index(3)+1}')
else:
    print('\nO valor 3 não foi digitado nenhuma vez')
print(f'\nOs numeros pares foram: ')

for numero in termo:
    if numero % 2 == 0:
        print(f'{numero}',end='')

