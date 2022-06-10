print('Preço: ')
n1 = float(input('Digite o valor do produto em R$: '))
n2 = float(input('Digite a porcentagem de desconto que deseja aplicar: '))
d = n1 - (n2/100)*n1 
print('Pegando os {}%, o novo valor do produto será de R${}'.format(n2,d))