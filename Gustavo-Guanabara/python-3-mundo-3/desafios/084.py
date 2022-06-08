reserva = list()
principal = []
maior = menor = 0
while True:
    reserva.append(str(input('Digite seu nome: ')).title())
    reserva.append(float(input('Digite seu peso em (Kg): ')))
    if len(principal) == 0:
        maior = reserva[1]
        menor = reserva[1]
    else:
        if reserva[1] > maior:
            maior = reserva[1]
        elif reserva[1] < menor:
            menor = reserva[1]
    principal.append(reserva[:])
    reserva.clear()
    pergunta = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if pergunta in 'Nn':
        break
print('-='*30)
print(f'Foram cadastrado um total de {len(principal)} de pessoas')
print(f'O maior peso foi de {maior}Kg e pertence à: ',end='')
for maio in principal:
    if maio[1] == maior:
        print(maio[0])
print(f'O menor peso foi de {menor}Kg e pertence à: ',end='')
for men in principal:
    if men[1] == menor:
        print(men[0])