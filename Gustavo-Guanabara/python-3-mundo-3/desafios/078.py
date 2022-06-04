valores = list()
maior = menor = 0
for numeros in range(0,5):
    valores.append(int(input(f'Digite o número da posicão {numeros}: ')))
    if numeros == 0:
        maior = menor = valores[numeros]
    else:
        if valores[numeros] > maior:
            maior = valores[numeros]
        if valores[numeros] < menor:
            menor = valores[numeros]
print(f'Sua lista completa é: {valores}')
print(f'O maior valor digitado foi o {maior} e ele encontra-se nas posições: ')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}...',end='')
print(f'O menor valor digitado foi o {menor} e ele encontra-se nas posições: ')
for p,v in enumerate(valores):
    if v == menor:
        print(f'{p}...',end='')
        
        
    
