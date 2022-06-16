def linha ():
    
    print('-='*30)
def maior (*lista):
    linha()
    print('Analisando os valores passados...')
    while True:
        for posicao in lista:
            print(f'{posicao} .',end='')
        if max(lista) == 0:
            print(f'Foram informados ao todo {0} valores')
            print(f'O maior valor informado foi: {max(lista)}')
            break
        print(f'Foram informados ao todo {len(lista)} valores')
        print(f'O maior valor informado foi: {max(lista)}')
        break

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)