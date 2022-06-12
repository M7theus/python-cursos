colunas = []
linhas = [[]]

print(f'{" Matriz ":=^30}')
pergunta_colun = int(input('Quantas colunas terá sua matriz? '))
pergunta_linha = int(input('Quantas linhas terá sua matriz? '))
for coluna in range(0,pergunta_colun):
    for linha in range(0,pergunta_linha):
        pergunt = int(input(f'Digite [{coluna}, {linha}]: '))
        if linha == 0:
            colunas.append(pergunt)
        if linha  >= 1:
            linhas[0].append(pergunt)
print(colunas)
print(linhas)
for coluna in range(0,pergunta_colun):
    if coluna == 0:
        print(f'{colunas}\n',end='')
    for linha in range(0,pergunta_linha):
        print(f'[{linhas[0][linha]}]',end='')
        linhas.pop(0)
        if linha == pergunta_colun-1:
            print()