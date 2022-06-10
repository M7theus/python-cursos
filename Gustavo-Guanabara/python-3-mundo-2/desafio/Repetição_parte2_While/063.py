termo = int(input('Quantos termos deseja mostrar? '))

c = 0
primeiro = 0
segundo = 1
soma = primeiro
while c != termo:
    soma += primeiro
    print(' {} '.format(soma),end='')
    primeiro = segundo
    segundo = soma
    
    
    c += 1
    
