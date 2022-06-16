from time import sleep
def linha ( ):
    print('-='*30)
def contador (inicio,fim,passo):
    if passo == 0:
        passo = 1
        for contagem in range(inicio,fim-passo,-passo):
            print(f'{contagem} ',end='')
    if inicio < fim:
        for contagem in range(inicio,fim-passo,passo):
            print(f'{contagem} ',end='')
    elif fim < 0:
        fim = fim * -1
        for contagem in range(inicio,fim,passo):
            print(f'{contagem} ',end='')
    else:
        if passo > 0:
            for contagem in range(inicio,fim-passo,-passo):
                print(f'{contagem} ',end='')
        else:
            for contagem in range(inicio,fim+passo,passo):
                print(f'{contagem} ',end='')

linha()
print('Contagem de 1 até 10 de 1 em 1')
contagem = 1
while contagem != 11:
    print(f'{contagem} ',end='')
    contagem += 1
print(f'{ "Fim"}')
linha()
print('Contagem de 10 até 0 de 2 em 2')
for posicao in range(10,-1,-2):
    print(f'{posicao} ',end='')
print(f'{ "Fim"}')
linha()
print('Agora é sua vez de personalizar a contagem! ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
while True:
    if passo == 0:
        print(f'Contagem de {inicio} até {fim} de {"1"} em {"1"}')
        break
    if passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        break
    else:
        print(f'Contagem de {inicio} até {fim} de {passo *-1} em {passo *-1}')
        break

contador(inicio, fim, passo)
print(f'{"Fim"}')