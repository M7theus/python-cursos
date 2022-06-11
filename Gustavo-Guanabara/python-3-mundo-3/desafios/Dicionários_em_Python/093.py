quant_gol = 0
dados = dict()
gol = list()
total = list()

nome = str(input('Digite o nome do jogador: '))
dados['nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou? '))
for posicao in range(0,partidas):
    partida = int(input(f'Quantos gols {nome} fez na {posicao} partida? '))
    quant_gol += partida
    gol.append(partida)
dados['gols'] = gol
dados['total'] = quant_gol
total.append(dados.copy())
print('-='*30)
print(dados)
print('-='*30)
for valor in total:
    for keys,values in valor.items():
        print(f'O campo {keys} tem como valor {values}')
print('-='*30)
print(f'O jogador {nome} jogou {partidas} partidas.')
n = 0
for posicao in dados['gols']:
    print(f'Na partida {n}, fez {posicao} gols')
    n += 1
print(f'Foi um total de {quant_gol} gols')