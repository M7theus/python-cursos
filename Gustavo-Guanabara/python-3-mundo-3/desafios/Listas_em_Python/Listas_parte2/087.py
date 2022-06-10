from stringcolor import *
paleta_cores = [['#281b24'],['#d02941'],['#f57e67'],['#d9c9a5'],['#8cab94']]

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = 0
soma_terceira = 0
maior_segunda = 0
for lista in range(0,3):
    for posicao in range(0,3):
        numero = int(input(f'Digite o número da posicao [{lista}, {posicao}]: '))
        if numero % 2 == 0:
            soma_pares += numero
        if posicao == 2:
            soma_terceira += numero
        if lista == 1:
            if posicao == 0:
                maior_segunda = numero
            else:
                if numero > maior_segunda:
                    maior_segunda = numero
        matriz[lista][posicao] = numero
print('-='*30)
for lista in range(0,3):
    for posicao in range(0,3):
        print(f'[{matriz[lista][posicao]:^5}]',end='')
    print()
print('-='*30)
print(f'A soma dos valores pares foi de: {soma_pares}')
print(f'A soma dos valores da terceira coluna foi de: {soma_terceira}')
print(f'O maior valor da segunda linha é o: {maior_segunda}')
    