gasto = 0
maior = 0
menor = 0
b_barato = 0
m_caro = 0
while True:
    print('-='*15)
    print('Cadastramento de produtos')
    print('-='*15)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto em R$: '))
    gasto += preco
    if preco > 1000:
        maior += 1
    else:
        menor += 1
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while pergunta not in 'S''N':
        pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
    
    if b_barato == 0 :
        b_barato = preco
        b_nome = nome
    else:
        if preco < b_barato:
            b_barato = preco
            b_nome = nome
    
    if m_caro == 0:
        m_caro = preco
        m_nome = nome
    else:
        if preco > m_caro:
            m_caro = preco
            m_nome = nome
print('Fim do programa')
print(f'Você gastou um total de R${gasto:.2f}')    
print(f'{maior} produtos custam acima de R$ 1000')
print(f'{menor} produtos custam abaixo de R$ 1000')
print(f'O/A {b_nome} é o produto mais barato e custa R$ {b_barato}')
print(f'O/A {m_nome} é o produto mais caro e custa R$ {m_caro}')