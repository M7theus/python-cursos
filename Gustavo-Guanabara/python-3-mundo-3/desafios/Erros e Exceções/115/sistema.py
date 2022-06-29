from biblioteca.interface import *
from time import sleep

cabeçalho('Teste')
while True:
    dado = corpo(['Pessoas cadastradas', 'Cadastradar novo usuário', 'Sair'])
    if dado == 1:
        cabeçalho('Teste 1')
    elif dado == 2:
        cabeçalho('Teste 2')
    elif dado == 3:
        cabeçalho('Saindo do programa. Até logo')
        sleep(2)
        break
    else:
        cabeçalho('\033[31mValor inválido\033[m')
    sleep(2)    