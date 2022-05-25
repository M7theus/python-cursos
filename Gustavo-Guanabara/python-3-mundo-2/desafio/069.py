mais18 = menor18 = hc = mc = m20 = pessoas = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    pessoas += 1
    if pergunta == 'N':
        break
    
    if idade > 18:
        mais18 += 1
    if idade < 18: 
        menor18 += 1
    if sexo == 'M':
        hc += 1
    if sexo == 'F':
        mc += 1
    if idade > 20 and sexo == 'F':
        m20 += 1
print(f'Do total das {pessoas}')
print(f'{mais18} são maiores de idade')
print(f'{menor18} são menores de idade')
print(f'{hc} são do sexo masculino')
print(f'{mc} são do sexo feminino')
print(f'{m20} São mulheres com mais de 20 anos')