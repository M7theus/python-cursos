from time import sleep

def PyAjuda ():
    while True:
        nome = 'Sistema de ajuda'
        tamanho = len(nome) +2
        
        print('\033[42m^\033[m'*tamanho)
        print(f'\033[41m{nome}\033[m')
        print('\033[42m^\033[m'*tamanho)
        
        nome = str(input('Função ou biblioteca? '))
        sleep(0.5)
        
        if nome == 'FIM':
            break
        
        print('\033[42m^\033[m'*tamanho)
        print(f'\033[41mAcessando o manual do comando: {nome}\033[m')
        print('\033[42m^\033[m'*tamanho)
        
        print(help(nome))
        
PyAjuda()