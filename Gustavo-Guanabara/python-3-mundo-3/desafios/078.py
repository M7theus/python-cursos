valores = list()
for valor in range(0,5):
    valores.append(int(input(f'Digite o {valor} valor: ')))
print(f'Você digitou os seguintes números: {valores}')
print(f'O maior número dentre eles é o: {max(valores)}')
print(f'O menor número dentre eles é o: {min(valores)}')
maior = max(valores)
menor = min(valores)
contagem_maior = valores.count(maior)
contagem_menor = valores.count(menor)

print(f'A posição do maior valor é:')
if contagem_maior > 1:
    q = 0
    for c in range(0,contagem_maior):
        print(f'\n{valores.index(maior,q) }',end='')
        q += 2
else:
    print(valores.index(maior))

print(f'A posição do menor valor é: ')
if contagem_menor > 1:
    q = 0
    for c in range(0,contagem_menor):
        print(f'\n{valores.index(menor,q) }',end='')
        q += 2
else:
    print(valores.index(menor))