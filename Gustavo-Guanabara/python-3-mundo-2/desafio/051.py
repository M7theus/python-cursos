termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite sua razão: '))
decimo = termo + (9) * razao

print('A sua PA é: ')
for numero in range(termo,decimo,razao):
    print(numero, end=' -> ')
print('FIM')