n1 = float(input('Digite o valor de uma reta: '))
n2 = float(input('Digite o valor de outra reta: '))
n3 = float(input('Valor de mais uma reta: '))
if n1 - n3 < n2 and n1 + n3 > n2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')