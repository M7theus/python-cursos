dados = dict()
lista = list()
lista_mulher = list()
quant_pessoas = 0
soma_idade = 0

while True:
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    dados['nome'] = nome
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'Ff':
        lista_mulher.append(nome)
    dados['sexo'] = sexo
    idade = float(input('Digite sua idade: '))
    dados['idade'] = idade
    soma_idade += idade
    lista.append(dados.copy())
    dados.clear()
    quant_pessoas += 1
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break
media_idade = soma_idade / quant_pessoas
print(lista)
print('-='*30)
print(f'Foram cadasdrado um total de {quant_pessoas} pessoas.')
print(f'A média da idade do grupo é de: {media_idade:.2f}')
print(f'As mulheres cadastradas foram: {lista_mulher}')
print('Lista das pessoas que estão acima da média: ')
print('-='*30)
for posicao in lista:
    for keys,values in posicao.items():
        if posicao["idade"] > media_idade:
            print(f'{keys} = {values}',end='')
        print()

