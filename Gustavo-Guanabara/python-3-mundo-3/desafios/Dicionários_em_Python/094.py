dados = dict()
lista = list()
quant_pessoas = 0
soma_idade = 0

while True:
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    dados['nome'] = nome
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    dados['sexo'] = sexo
    idade = float(input('Digite sua idade: '))
    dados['idade'] = idade
    soma_idade += idade
    lista.append(dados.copy())
    quant_pessoas += 1
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break
media_idade = soma_idade / quant_pessoas
print(lista)
print(media_idade)
print('-='*30)
print(f'Foram cadasdrado um total de {quant_pessoas}')
print(f'A média da idade do grupo é de: {media_idade:.2f}')
print('Uma lista com todas as mulheres')
