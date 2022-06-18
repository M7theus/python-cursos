from time import sleep

def contador(inicio,fim,passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio > fim:
        print()
        print(f'Contagem de {inicio} até {fim} pulando de {passo} em {passo}')
        print('-=-'*20)
        cont = inicio
        while cont >= fim:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont -= passo 
        print()   
    elif inicio < fim:
        print()
        print(f'Contagem de {inicio} até {fim} pulando de {passo} em {passo}')
        print('-=-'*20)
        cont = inicio
        while cont <= fim:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont += passo
        print()

        
    
contador(10,1,1)
contador(1, 20, 2)
print('-=-'*20)
print('Agora é sua vez de personalizar! ')
inicio = int(input('Digite o ínicio da sua contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Passo da contagem: '))

contador(inicio, fim, passo)