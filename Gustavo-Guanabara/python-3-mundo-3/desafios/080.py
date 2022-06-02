lista = list()
primero_numero = segundo_numero = 0
for posicao in range(0,5):
    numero = int(input('Digite seu número: '))
    print(f'Posição: {posicao}')
    if posicao == 0:
        primero_numero = numero
        lista.insert(0, numero)
    if posicao == 1:
        if numero > primero_numero:
            lista.insert(posicao, numero)
        else:
            lista.insert(0, numero)
    if posicao > 1:
        if numero > primero_numero:
            if numero > segundo_numero:
                lista.insert(posicao, numero)
            else:
                lista.insert(posicao-1, numero)
        if numero < primero_numero: 
            if numero < segundo_numero:
                lista.insert(0, numero)
            else:
                lista.insert(posicao-1, numero)
    
    primero_numero = numero
    segundo_numero = numero
    print(lista)
print(lista)