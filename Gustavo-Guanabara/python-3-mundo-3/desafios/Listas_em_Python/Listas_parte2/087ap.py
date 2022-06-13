lista = [[],[]]
dado = dict()

print(f'{" Matriz ":=^30}')
pergunta_colun = int(input('Quantas colunas terá sua matriz? '))
pergunta_linha = int(input('Quantas linhas terá sua matriz? '))
for coluna in range(0,pergunta_colun):
    for linha in range(0,pergunta_linha):
        pergunt = int(input(f'Digite [{coluna}, {linha}]: '))
        if linha == 0:
            dado['coluna'] = pergunt
            lista[0].append(dado.copy())
        if linha >= 1:
            dado['linha'] = pergunt
            lista[1].append(dado.copy())
        dado.clear()

for coluna in range(0,pergunta_colun):
    print(f'{lista[0][coluna]}')
    for linha in range(0, pergunta_linha):
        print(f'{lista[1][linha]}')