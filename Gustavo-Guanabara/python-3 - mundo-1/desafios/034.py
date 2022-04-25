n1 = float(input('Digite o valor do seu salário em R$: '))
if n1 > 1250:
    print('Você terá um aumento no seu salário de \033[4;33m10%\033[m, resultando no valor de \033[1;32mR${}\033[m'.format(((10/100)*n1)+n1))
else:
    print('Você terá um aumento no seu salário de \033[4;33m15%\033[m, resultando no valor de \033[1;32mR${}\033[1;32m'.format(((15/100)*n1)+n1))