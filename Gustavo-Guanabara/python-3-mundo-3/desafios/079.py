lista = list()
while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Número duplicado. Não irei adicionar.')
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')
