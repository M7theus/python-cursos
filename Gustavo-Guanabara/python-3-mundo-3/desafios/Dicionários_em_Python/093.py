dados = dict()
gols = list()

dados['nome'] = str(input('Digite o nome do jogador: ')).strip().title()
partida = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for posicao in range(0,partida):
    gols.append(int(input(f'    Quantos gols na partida: {posicao}? ')))
dados['gols'] = gols
dados['total'] = sum(gols)
print('-='*30)
print(dados)
print('-='*30)
for keys, values in dados.items():
    print(f'{keys} --> {values}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {len(gols)} partidas')
for keys,values in enumerate(gols):
    print(f'    gols na partida {keys}: {values}')
