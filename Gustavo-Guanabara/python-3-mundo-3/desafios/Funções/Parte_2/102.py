#Fazendo com o while
'''def fatorial(num, show=False):
    cont = num
    mult = 1
    while cont != 0:
        mult *= cont
        if show:
            print(cont,end='')
            if cont >= 2:
                print(f'{" X "}',end='')
            else:
                print(f'{" = "}',end='')
        cont -= 1
    return mult'''

#Fazendo com o for
def fatorial (num, show=False):
    """
    --> Docstring
    """
    mult = 1
    for posicao in range(numero,0,-1):
        if show:
            print(posicao,end='')
            if posicao >= 2:
                print(f'{" X "}',end='')
            else:
                print(f'{" = "}',end='')
        mult *= posicao
    return mult
        

numero = int(input('Digite o número que desejar visualizar o fatorial: '))
print(fatorial(numero, show=True))
