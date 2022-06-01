lista = list()
ant_numero = 0
for posicao in range(0,5):
    numero = int(input('Digite um número: '))
    if posicao == 0:
        lista.append(numero)
        ant_numero = numero
    else:
        if numero > ant_numero:
            print('Número adicionado ao final da lista')
            lista.insert(posicao, numero)
            ant_numero = numero 
        elif numero < ant_numero:
            print('Número adicionado ao início da lista')
            if numero > lista[0] and numero < lista[1]:
                lista.insert(1, numero)
            else:
                lista.insert(0,numero)
            ant_numero = numero
    print(lista)
    