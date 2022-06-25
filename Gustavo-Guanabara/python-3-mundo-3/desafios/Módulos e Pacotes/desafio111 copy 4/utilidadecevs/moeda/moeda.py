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

def resumo(valor = 0, aumento = 0, desconto = 0):
    print('-'*30)
    print(f'{"Resumo do valor":^30}')
    print('-'*30)
    print(f'{"Preço analisado:"}',end='')
    print(f'{"R$":>10}{valor:>5.2f}')
    print(f'{"Dobro do preço:":>10} {"R$":>10}{valor*2:>5.2f}')
    print(f'{"Metade do preço:":>10} {"R$":>10}{valor/2:>5.2f}')
    aumento = ((8/100)*valor) + valor
    print(f'{"8% de aumento:":>10} {"R$":>10}{aumento:>5.2f}')
    desconto = ((35/100)*valor) + valor
    print(f'{"35% de desconto:":>10} {"R$":>10}{desconto:>5.2f}')