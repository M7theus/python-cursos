valores = list()
quantidade_maior =  quantidade_menor = 0
for posicao in range(0,5):
    numero = int(input(f'Digite o {posicao} número: '))
    valores.append(numero)
print(valores)
print(f'O maior valor digitado foi: {max(valores)}')
print(f'O menor valor digitado foi: {min(valores)}')
quantidade_maior = valores.count(max(valores))
quantidade_menor = valores.count(min(valores))

if quantidade_maior > 1:
    for con in range(0,quantidade_maior):
        print(f'Posição dos maiores números: {valores.index(max(valores),con)}')
        con = valores.index(max(valores))
else:
    print(f'Posição dos maiores números: {valores.index(max(valores))}')
    
if quantidade_menor > 1:
    for cont in range(0,quantidade_menor):
        print(f'Posição dos menores números: {valores.index(min(valores),con)}')
        con = valores.index(max(valores))
else:
    print(f'Posição dos menores números: {valores.index(min(valores))}')
