lista = list()
while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    contagem = lista.count(numeros)
    print(contagem)
    if contagem > 1:
        print('Hmm.... Número repetido. Vou remover!')
        lista.remove(numeros)
    pergunta = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'Você digitou os números {lista.sort()}')