numero = 0
while True:
    numero = int(input('Digite o número que queira ver da tabuada (negativo para parar): '))
    if numero < 0:
        break
    for c in range(1,11):
        print(f'{numero} x {c} = {numero*c}')
print('Fim do programa')