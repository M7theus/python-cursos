valores = list()
for numeros in range(0,5):
    valores.append(int(input(f'Digite o {numeros}: ')))
print(f'Os valores digitados foram: {valores}')
print(f'O maior número entre os {numeros} foi o {max(valores)} e suas posições são a {valores.index(max(valores))}')
print(f'O menor número entre os {numeros} foi o {min(valores)} e suas posições são a {valores.index(min(valores))}')

maior = max(valores)
menor = min(valores)
quant_maior = valores.count(maior)
quant_menor = valores.count(menor)
d = 0
for valor in range(0,len(valores)):
    print(f'{valor:.<10}',end='')
    print(f'{valores[valor]:.>10}')
    
if maior in valores:
    if quant_maior > 1:
        for s in range(0,quant_maior):
            print(valores.index(maior,d))
            d += 1
        d = 0
    if menor > 1:
        for s in range(0,quant_menor):
            print(valores.index(menor,d))
            d += 1
        
    