lista = list()

coluna = int(input('Quantas colunas terá sua matriz? '))
for _ in range(0,coluna):
    lista.append([])
quantidade_coluna = coluna
print(lista)

while True:
    linha = int(input('Quantas linhas terá sua matriz? '))
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
        
    
print(lista)

'''for colunas in range(0,coluna):
    for linhas in range(0,coluna):
        if linhas % 2 == 0:
            lista[colunas][linhas] = int(input(f'Digite o número da posição: [{colunas},{linhas}]: '))
        else:
            lista[colunas][linhas] = int(input(f'Digite o número da posição: [{colunas},{linhas}]: '))
print(lista)'''