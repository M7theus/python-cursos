def metade(valor):
    m = valor/2
    return m


def dobro(valor):
    d = valor*2
    return d


def aumento (valor, porcentagem = 1):
    co = (porcentagem/100)*valor + valor
    return co
    
def redução (valor, porcentagem =1):
    re = valor-(porcentagem/100)*valor
    return re

def moeda(valor = 0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')