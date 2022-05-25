total = p_1000 = cont = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: '))
    total += preco
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if preco > 1000:
        p_1000 += 1    
    if pergunta == 'N':
        break
    if cont == 0 or preco < m_barato:
        m_barato = preco
        m_nome = nome
    cont += 1
print(f'O total da comprar foi de R$ {total}')
print(f'{p_1000} produto custam acima de R$ 1000.00')
print(f'O produto mais barato é o {m_nome} e o seu preço é R$ {m_barato}')