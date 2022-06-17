from time import sleep

def maior (* numeros):
    cont = maior = 0
    print(f'Analisando os valores passados {"..."}\n',end='')
    for num in numeros:
        print(f'{num} ',end='',flush=True)
        sleep(0.4)
        if cont == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        cont += 1 
    print(f'O maior número entre os {cont} é o: {maior}')
    print('-=-'*20)

maior(2,4,3,1,5,1)
maior(2,9,5,4)
maior(6,7)
maior(3)
maior()