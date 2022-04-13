print('Reajuste salárial')
n1 = float(input('Digite o valor do salário: '))
n2 = float(input('Digite a porcentagem: '))
a = (n2/100)*n1 + n1
print('Seu salário terá um acréscimo de {}%, resultando no valor de R${:.3f}'.format(n2,a))