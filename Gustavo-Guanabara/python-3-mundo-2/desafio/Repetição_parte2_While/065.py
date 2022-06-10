pergunta = 'S'
soma = quant = maior = menor = 0
while pergunta == 'S':
    numero = int(input('Digite um número; '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = numero
        menor = numero
    else:
        if maior < numero:
            maior = numero
        elif menor > numero:
            menor = numero
    pergunta = str(input('Deseja continuar? [S/N]: ')).upper().strip()
media = (soma/quant)
print('A média é {}'.format(media))
print('O maior número é {}'.format(maior))
print('O menor número {}'.format(menor))