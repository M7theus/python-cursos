soma = 0
cont = 0


for num in range(1,7):
    numeros = int(input('Digite o {} número: '.format(num)))
    if numeros % 2 == 0:
        soma += numeros
        cont += 1
print('Você digitou um total de {} números pares e a soma entre eles deu {}'.format(cont,soma))