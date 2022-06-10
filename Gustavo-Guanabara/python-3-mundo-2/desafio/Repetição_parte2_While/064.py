numero = soma = cont = 0
while numero != 999:
    numero = int(input('Digite um número qualquer [999 para parar]: '))
    if numero != 999:
        soma += numero
        cont += 1
print('Você digidou um total de {} números e a soma entre eles deu {}'.format(cont,soma))
