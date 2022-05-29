valores = list()
for numero in range(0,5):
    valores.append(int(input(f'Digite o {numero}: ')))
print(f'Os números digitados foram: {valores}')
print(f'O maior número entres os {numero} foi o {max(valores)}') 
print(f'O menor número entre os {numero} foi o {min(valores)}')
print(f'Os maiores valores encontram-se nas posições: ')


for n in valores:
    print(max(valores))