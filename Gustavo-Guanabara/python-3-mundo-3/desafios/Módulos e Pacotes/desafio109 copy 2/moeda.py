def metade(valor = 0, form = False):
    m = valor/2
    if form == True:
        return formatacao(m)
    return m


def dobro(valor, form = False):
    d = valor*2
    if form == True:
        return formatacao(d)
    return d


def aumento (valor, porcentagem = 1, form = False):
    co = (porcentagem/100)*valor + valor
    if form == True:
        return formatacao(co)
    return co
    
def redução (valor, porcentagem =1, form = False):
    re = valor-(porcentagem/100)*valor
    if form == True:
        return formatacao(re)
    return re

def formatacao(valor = 0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')