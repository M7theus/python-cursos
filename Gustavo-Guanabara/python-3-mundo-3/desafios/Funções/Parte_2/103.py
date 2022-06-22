def dados (nome = '<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gols')

n = str(input('Digite o nome do jogado: '))
g = str(input('Digite a quantidade de gols feita no jogo: '))


if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    dados(gol = g)
else:
    dados(n,g)

