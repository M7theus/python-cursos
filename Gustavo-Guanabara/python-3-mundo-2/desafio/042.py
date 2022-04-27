n1 = float(input('Digite o valor de uma reta: '))
n2 = float(input('Digite o valor de outra reta: '))
n3 = float(input('Valor de mais uma reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n3:
    if n1 == n2 == n3:
        print('Todos os lados são iguais, então o tiângulo é Equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Dois lados são iguais, então o triângulo é Isósceles')
    else:
        print('Todos os lados são diferentes, então o triângulo é Escaleno')
else:
    print('Impossível formar um triângulo')