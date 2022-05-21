soma = 0
quantidade = 0
while True:
    numero = int(input('Digite um número (999 para parar):'))
    if numero == 999:
        break
    soma += numero
    quantidade += 1
print(f'A soma entre os {quantidade} números é {soma}')