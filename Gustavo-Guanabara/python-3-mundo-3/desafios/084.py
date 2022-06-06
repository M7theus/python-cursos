dados = list()
total = list()
quant_pessoa = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso em (Kg): ')))
    if quant_pessoa == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    total.append(dados[:])
    quant_pessoa += 1
    dados.clear()
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break
print(f'Foram cadasdrado um total de {quant_pessoa} pessoas')
print(f'O maior peso é {maior}.0Kg. Peso de: ',end='')
for p in total:
    if p[1] == maior:
        print(p[0])
print(f'O menor peso é {menor}.0Kg. Peso de: ',end='')
for p in total:
    if p[1] == menor:
        print(p[0])
