dados = dict()
lista = list()
tabela = list()
total = 0
quant_jogador = 0

while True:
    dados['nome'] = str(input('Digite o nome do jogador: ')) 
    confirmacao = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for posicao in range(0,confirmacao):
        pergunta_gols = int(input(f'Quantos gols na partida {posicao}? '))
        total += pergunta_gols
        tabela.append(pergunta_gols)
        if confirmacao == len(tabela)+1:
            dados['gols'] = tabela[:]
            lista.append(dados.copy())
            dados.clear()
            tabela.clear()
    quant_jogador += 1
    dados['total'] = total
    total = 0
    lista.append(dados.copy())
    dados.clear()
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('-='*30)
    if pergunta in 'Nn':
        break
print(lista)
print(tabela)
'''print('-='*30)
print(f'{"cod.nome":<5}{"gols":>15}{"total":>20}')
print('-'*50)
for posicao in range(0,quant_jogador):
    print(f'{posicao:<2} {lista[posicao]["nome"]} [{lista[posicao]["gols"]}]')'''
