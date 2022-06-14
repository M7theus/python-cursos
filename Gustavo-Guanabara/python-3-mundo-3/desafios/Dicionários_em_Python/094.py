lista = []
nomes = list()
idades = []
sexos = []
mulheres = []
dados = dict()

while True:
    nome = str(input('Digite seu nome: '))
    nomes.append(nome)
    dados['nomes'] = nomes
    while True:
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('-='*30)
            print('Sexo não informado')
            sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            sexos.append(sexo)
            dados['sexo'] = sexos
            break
    idades.append(int(input('Digite sua idade: ')))
    dados['idades'] = idades
    if sexo in 'F':
        mulheres.append(nome)
        dados['mulheres'] = mulheres
    while True:
        pergunta = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if pergunta not in 'SN':
            print('Por favor, digite apenas S ou N')
        if pergunta in 'SN':
            break
    if pergunta in 'N':
        break
lista.append(dados.copy())
print('-=-'*30)
print(lista)
print('-=-'*30)
print(f'A) Ao todo temos {len(dados["nomes"])} pessoas cadastrados')
print(f'B) A média de idade é: {sum(dados["idades"])/len(dados["idades"]):.2f}')
print(f'C) As mulheres cadastradas foram: {dados["mulheres"]}')
print(f'D) Pessoas que possuem idade acima da média do grupo: ')
for q in range(0, len(dados["nomes"])):
    if dados["idades"][q] > (sum(dados["idades"])/len(dados["idades"])):
        print(f'{dados["nomes"][q]} --> {dados["sexo"][q]} --> {dados["idades"][q]}')
