idade_18 = 0
quantidade_m = 0
idade_f = 0
quant = 0

while True:
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        idade_18 += 1
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'M' 'F':
        while sexo not in 'M''F':
                sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        quantidade_m += 1
    else:
        if idade < 20:
            idade_f += 1
    pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while pergunta not in 'S''N':
            pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    quant += 1
    print('-=-'*20)
    if pergunta == 'N':
        break
print('Certo. Programa finalizado com sucesso.')
print(f'Do total das {quant} pessoas, {idade_18} são maiores de 18')
print(f'{quantidade_m} são homens')
print(f'{idade_f} são mulheres com menos de 20 anos')