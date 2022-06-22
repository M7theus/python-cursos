def dados (*num,sit=False):
    dic = dict()
    dic['Notas'] = num
    dic['Maior'] = max(num)
    dic['Menor'] = min(num)
    dic['Média'] = sum(num)/len(num)
    dic['Total'] = len(num)
    if sit:
        if dic['Média'] >= 7:
            dic['Situação'] = 'Boa'
        elif dic['Média'] >= 5:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Ruim'    
    return dic

info = dados(3,5,7,1,2,6,3,sit=True)
print(info)