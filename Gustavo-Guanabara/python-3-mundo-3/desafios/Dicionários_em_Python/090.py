dicionario = dict()
lista = list()

dicionario['nome'] = str(input('Digite seu nome: ')).strip().title()
dicionario['media'] = float(input('Digite sua média: '))
if dicionario['media'] < 7:
    dicionario['situacao'] = 'Reprovado'
else:
    dicionario['situacao'] = 'Aprovado'
lista.append(dicionario.copy())
print('-='*30)
for dados in lista:
    for keys, values in dados.items():
        print(f'{keys} é igual a {values}')