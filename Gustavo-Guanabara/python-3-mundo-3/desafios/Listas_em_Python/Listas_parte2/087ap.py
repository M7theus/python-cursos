from time import sleep
lista = list()

coluna = int(input('Quantas colunas terá sua matriz? '))
print('Hmmm')
sleep(0.5)
for _ in range(0,coluna):
    lista.append([])
quantidade_coluna = coluna
print()
print(f'Suas colunas: {lista}')

while True:
    linha = int(input('Quantas linhas terá sua matriz? '))
    print('Hmmm')
    sleep(0.5)
    if linha % 2 == 1:
        print('Impossível formação de matriz. Tente novamente')
        print()
    else:
        break
cont = 0
teste = 0

for linhas in range(0,coluna):
    if linhas % 2 == 0:
        while teste != linha:
            lista[linhas].append(0)
            teste += 1
        teste = 0
    elif linhas % 2 == 1:
        while teste != linha:
            lista[linhas].append(0)
            teste += 1
        teste = 0
print()   
print(f'Suas linhas: {lista}')

print('-=-' *30)
print(f'Agora digite os valoes para a sua matriz: ')
print('-=-'*30)
for val_coluna in range(0,coluna):
    for val_linha in range(0,linha):
        numero = int(input((f'Digite o valor para a posição: [{val_coluna}, {val_linha}]: ')))
        lista[val_coluna][val_linha] = numero

cont = 0
print(f'--> \033[1;32mPar\033[m')
print(f'--> \033[1;31mÍmpar\033[m')
print('-'*30)
print('Matriz em formação: ')
print()
for val_coluna in range(0,coluna):
    for val_linha in range(0,linha):
        if cont == coluna:
            cont = 0
            print()
        cont += 1
        if lista[val_coluna][val_linha] % 2 == 0:
            sleep(0.5)
            print(f'\033[1;32m[{lista[val_coluna][val_linha]:^5}]\033[m',end='')
        else:
            sleep(0.5)
            print(f'\033[1;31m[{lista[val_coluna][val_linha]:^5}]\033[m',end='')

print()