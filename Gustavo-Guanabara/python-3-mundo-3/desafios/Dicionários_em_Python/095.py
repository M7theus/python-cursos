dados = dict()
lista_gols = list()
lista_completa = list()
total = 0

while True:
    dados.clear()
    lista_gols.clear()
    dados['nome'] = str(input('Digite o nome do jogador: ')).strip().title()
    pergunta = int(input('Quantos jogos foram jogados? '))
    for posicao in range(0,pergunta):
        lista_gols.append(int(input(f'Quantos gols no jogo {posicao}: ' )))
        total += lista_gols[posicao]
    dados['gols'] = lista_gols
    dados['total'] = total
    lista_completa.append(dados.copy())
    while True:
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N como resposta')
    if resposta in 'N':
        break
print('-='*30)
for k in dados.keys():
    print(f'{k:<5}',end='')
print()
for k,v in enumerate(lista_completa):
    print(f'{k:<2}',end='')
    for value in v.values():
        print(f' {str(value)} ',end='')
    print()
while True:
    afirmacao = int(input('Digite o número do jogador para obter mais informações (999 para parar): '))
    if afirmacao == 999:
        break
    if afirmacao >= len(lista_completa):
        print('Valor informado não existente.Tente outro valor')
    else:
        print()
        for k,v in enumerate(lista_completa[afirmacao]["gols"]):
            print(f'{k} --> {v}')
            
    

