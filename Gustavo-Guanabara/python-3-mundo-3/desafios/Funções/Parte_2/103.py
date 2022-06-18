def jogo ():
    nome = str(input('Digite o nome do jogador: ')).strip().title()
    if len(nome) < 1:
        nome = '<desconhecido>'
    gols = str(input('Digite a quantidade de gols: '))
    if len(gols) < 1:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols')

jogo()