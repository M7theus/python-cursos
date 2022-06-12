completa = list()
colunas = [[]]
linhas = [[]]

print(f'{" Matriz ":=^30}')
pergunta_colun = int(input('Quantas colunas terá sua matriz? '))
pergunta_linha = int(input('Quantas linhas terá sua matriz? '))
for coluna in range(0,pergunta_colun):
    for linha in range(0,pergunta_linha):
        pergunt = int(input(f'Digite [{coluna}, {linha}]: '))
        if linha == 0:
            colunas[0].append(pergunt)
        else:
            linhas[0].append(pergunt)
colunas.extend(linhas) #Adicionei uma lista em outra
print(colunas)
a = 0
for coluna in range(0,pergunta_colun):
    print(f'[{colunas[0][a]}]',end='')
    a += 1
print()
for linha in range(0,pergunta_linha+1):
    if linha == 0:
        print(f'[{colunas[1][linha]}]',end='')
    else:
        print(f'[{colunas[1][linha::1]}]',end='')
print()