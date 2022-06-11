from datetime import date
ano = date.today().year

dados = dict()
lista = list()

dados['nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Digite seu ano de nascimento: '))
dados['idade'] = ano - nascimento
carteiratrabalho = int(input('Carteira de trabalho (0 não tem): '))
dados['ctps'] = carteiratrabalho
if carteiratrabalho == 0:
    lista.append(dados.copy())
    print('-='*30)
    for posicao in lista:
        for keys, values in posicao.items():
            print(f'{keys} tem o valor {values}')
if carteiratrabalho != 0:
    contratacao = int(input('Ano de contratação: '))
    dados['contratação'] = contratacao
    dados['salário'] = int(input('Salário: R$ '))
    dados['aposentadoria'] = (contratacao + 35) - nascimento
    lista.append(dados.copy())
    print('-='*30)
    for posicao in lista:
        for keys, values in posicao.items():
            print(f'{keys} tem o valor {values}')