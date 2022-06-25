def metade(valor = 0, form = False):
    m = valor/2
    if form == True:
        return f'{"R$"}{m:.2f}'.replace('.', ',')
    return m


def dobro(valor, form = False):
    d = valor*2
    if form == True:
        return f'{"R$"}{d:.2f}'.replace('.', ',')
    return d


def aumento (valor, porcentagem = 1, form = False):
    co = (porcentagem/100)*valor + valor
    if form == True:
        return f'{"R$"}{co:.2f}'.replace('.', ',')
    return co
    
def redução (valor, porcentagem =1, form = False):
    re = valor-(porcentagem/100)*valor
    if form == True:
        return f'{"R$"}{re:.2f}'.replace('.', ',')
    return re

def formatacao(valor = 0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo (valor=0,tax_au = 0, taxa_dim = 0):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t\t{formatacao(valor)}')
    print(f'Metade desse preço: \t\t{metade(valor,True)}')
    print(f'Dobro desse preço: \t\t{dobro(valor,True)}')
    print(f'Aumento de {tax_au}% do preço: \t{aumento(valor,tax_au,True)}')
    print(f'Diminuição de {taxa_dim}% do preço: \t{redução(valor,taxa_dim,True)}')
    