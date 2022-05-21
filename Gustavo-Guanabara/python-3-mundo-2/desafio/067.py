c =  0
numero = int(input('Deseja vê a tabuada de qual número? '))
while True:
    if numero > 0:
        for numeros in range(0,11):
            resultado = numero * numeros
            print(f'{numero} x {numeros} = {resultado}')
    numero = int(input('Digite outro número: '))
    if numero < 0:
        break
print('Fim do programa')
    