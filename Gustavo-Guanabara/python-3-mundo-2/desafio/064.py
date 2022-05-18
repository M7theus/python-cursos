numero = 0
soma = 0
cont = 0
print('Digite 999 para parar o programa')
while numero != 999:
    numero = int(input('Digite qualquer número: '))
    soma += numero -999
    cont += 1
print('Fim do programa')
print('A soma dos {} números digitados é {}'.format(cont,soma))