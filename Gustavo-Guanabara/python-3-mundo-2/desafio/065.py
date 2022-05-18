palavra = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while palavra == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    cont += 1
    media = (soma/cont)
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if maior < numero:
            maior = numero
        if menor > numero:
            menor = numero
    palavra = str(input('Deseja continuar? [S/N]')).upper().strip()
print('A média dos {} números é {:.2f}'.format(cont,media))
print('O maior número é o {}'.format(maior))
print('O menor número é {}'.format(menor))