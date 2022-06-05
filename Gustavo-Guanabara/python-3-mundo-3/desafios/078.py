lista = list()
for posicao in range(0,5):
    lista.append(int(input(f'Digite o número da posição {posicao}: ')))
print(f'Sua lista completa ficou: {lista}')
print(f'O maior valor digitado foi {max(lista)} e ele encontra-se nas posições: ',end='')
for p,v in enumerate(lista):
    if v == max(lista):
        print(p)
print(f'O menor valor digitado foi {min(lista)} e ele encontra-se nas posições: ',end='')
for p,v in enumerate(lista):
    if v == min(lista):
        print(p)    
        
    
