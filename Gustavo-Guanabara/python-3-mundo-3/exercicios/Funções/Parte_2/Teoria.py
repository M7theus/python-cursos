'''def contador(inicio,fim,passo):
    """
    --> Teste
    Conhecendo as funcionalidades da Docstring
    """
    cont = inicio
    while cont <= fim:
        print(f'{cont} ',end='')
        cont += passo

help(contador)'''

'''def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f'{s} ')

somar(2)'''

'''def teste():
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'O x vale {x}')


n = 2
print(f'N vale {n}')
teste(n)
print(f'No programa principal, x vale {x}')'''

'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')'''

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s
r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(2)
print(f'Meus cálculos deram {r1},{r2} e {r3}')