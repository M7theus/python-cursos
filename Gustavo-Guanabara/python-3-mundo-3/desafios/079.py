lista = list()
while True:
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        lista.append(numero)
        print('Número adicionado com sucesso')
    else:
        print('Hmmm... Valor repetido. Não vou adicionar')
    pergunta = str(input('Você deseja continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break
print(f'Você digitou os valores: {lista}')