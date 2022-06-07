lista = list()
lista_par = []
lista_impar = []
for posicao in range(0,8):
    lista.append(int(input(f'Digite o {posicao} número: ')))
    if lista[0] % 2 == 0:
        lista_par.append(lista[:])
    else:
        lista_impar.append(lista[:])
    lista.clear()
print(f'Os valores pares digitados foram: {lista_par}')
print(f'Os valores ímpares digitados foram: {lista_impar}')