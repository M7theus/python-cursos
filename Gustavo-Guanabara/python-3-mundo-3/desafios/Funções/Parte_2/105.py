dados = dict()
lista = list()

def notas (*num,sit=0):
    cont = maior = menor = 0

    lista = num
    dados['total'] = len(lista)
    
    while cont != len(lista):
        if cont == 0:
            maior = lista[cont]
            menor = lista[cont]
        else:
            if lista[cont] > maior:
                maior = lista[cont]
            elif lista[cont] < menor:
                menor = lista[cont]
        cont += 1
    
    dados['maior'] = maior
    dados['menor'] = menor
    dados['media'] = sum(lista)/len(lista)
    dados['notas'] = num
    
    if sit == True:
        if dados['media'] <= 6:
            dados['situação'] = 'Situação ruim'
        else:
            dados['situação'] = 'Situação boa'
    return dados
    

resp = notas(10,4,5,3,4,9,6,sit=True) #Inserindo notas
print(resp)