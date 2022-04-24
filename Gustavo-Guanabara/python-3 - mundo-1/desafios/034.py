n1 = float(input('Digite o valor do seu salário em R$: '))
if n1 > 1250:
    print('Você terá um aumento no seu salário de 10%, resultando no valor de R${}'.format(((10/100)*n1)+n1))
else:
    print('Você terá um aumento no seu salário de 15%, resultando no valor de R${}'.format(((15/100)*n1)+n1))