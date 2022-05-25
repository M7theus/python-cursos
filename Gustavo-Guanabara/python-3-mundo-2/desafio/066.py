soma = quant = 0
while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    quant += 1
print(f'A soma entre os {quant} é {soma}')