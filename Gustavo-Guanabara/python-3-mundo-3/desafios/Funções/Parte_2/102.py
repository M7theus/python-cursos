def fatorial (numero, show = 0):
    """
    --> Função fatorial <--
    Possui dois atribudos:
    * numero = O valor que você quer vê o fatorial
    * show = Caso seja 'True' ele mostrará o passo a passo da conta
    """
    if show == False:
        cont = numero
        conta = 1
        while cont > 1:
            conta *= cont
            cont -= 1
        print(conta)
    elif show == True:
        cont = numero
        conta = 1
        while cont >= 1:
            print(f' {cont} ',end='')
            if cont > 1:
                print(f'x',end='')
            if cont == 1:
                print(f'{"="}',end='')
            conta *= cont
            cont -= 1
        print(f' {conta} ',end='')

help(fatorial)
