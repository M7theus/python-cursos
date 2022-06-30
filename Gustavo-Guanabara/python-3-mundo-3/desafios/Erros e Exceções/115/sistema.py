from biblioteca.interface import *
from time import sleep
from biblioteca.interface import arquivo

arq = 'Cursoemvídeo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)
    
cabeçalho('Teste')
while True:
    dado = corpo(['Pessoas cadastradas', 'Cadastradar novo usuário', 'Sair'])
    if dado == 1:
        arquivo.lerArquivo(arq)
    elif dado == 2:
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        arquivo.cadastrar(arq)
    elif dado == 3:
        cabeçalho('Saindo do programa. Até logo')
        sleep(2)
        break
    else:
        cabeçalho('\033[31mValor inválido\033[m')
    sleep(2)    