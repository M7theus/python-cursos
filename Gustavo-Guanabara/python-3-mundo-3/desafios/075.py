valor_1 = int(input('Digite um número: '))
valor_2 = int(input('Digite mais um: '))
valor_3 = int(input('DIgite outro: '))
valor_4 = int(input('Último número: '))

lista = (valor_1,valor_2,valor_3,valor_4)
print(lista)
print(f'O número 9 apareceu: {lista.count(9)}')
if lista == 3:
    print(f'O número 3 foi digitado na posição {lista.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os números pares foram: ')

for numeros in lista:
    if numeros % 2 == 0:
        print(numeros,end='')
