dados = dict()
gols = list()
lista = list()
total = 0
cont = 0

while True:
    dados['cod'] = cont
    cont += 1
    dados['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Quantas partidasd {dados["nome"]} jogou? '))
    for posicao in range(0,partidas):
        pergunta_gols = int(input(f'Quantos gols na {posicao} partida? '))
        gols.append(pergunta_gols)
        total += pergunta_gols
    dados['gols'] = gols[:]
    dados['total'] = total
    lista.append(dados.copy())
    gols.clear()
    dados.clear()
    confirmacao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if confirmacao in 'N':
        break
    print('-='*30)
print(f'{"cod":<10}{"nome":>5}{"gols":>20}{"Total":>30}')
for teste in lista:
    print(f'{teste["cod"]:<10},{teste["nome"]:>5},{teste["gols"]:>20},{teste["total"]:>30}')
