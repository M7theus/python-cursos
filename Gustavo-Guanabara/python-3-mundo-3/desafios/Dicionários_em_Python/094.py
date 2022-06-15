dados = dict()
galera = list()
idades = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Digite seu nome: ')).strip().title()
    while True:
        dados['sexo'] = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Sexo informado incorretamente, tente novamente')
    dados['idade'] = int(input('Digite sua idade: '))
    idades += dados['idade']
    galera.append(dados.copy())
    while True:
        pergunta = str(input('Deseja continuaar? [S/N]: ')).strip().upper()[0]
        if pergunta in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if pergunta in 'N':
        break
print('-=-'*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas. ')
print(f'B) A média entre as idades é: {idades/len(galera):5.2f}.')
print(f'C) As mulheres cadastradas foram: ')
for pessoa in galera:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]}',end='')
print(f'D) As pessoas que possuem idade acima da média são: ')
for pessoa in galera:
    if pessoa['idade'] >= (idades/len(galera)):
        print()
        for keys,values in pessoa.items():
            print(f'{keys} --> {values}')
print()
print('Programa encerrado com sucesso')