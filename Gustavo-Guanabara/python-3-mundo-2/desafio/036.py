from math import ceil

print('\033[1;35m-=-\033[m'*20)
print('Empréstimo casa')
print('\033[1;35m-=-\033[m'*20)

n1 = str(input('Digite seu nome completo porfavor: ')).strip().title()
n2 = float(input('Digite o valor total em reais da casa R$:'))
n3 = float(input('Digite sua renda mensal em reais R$:'))
n4 = float(input('Digite em quantos anos deseja quitar a casa:'))
mes = n4 *12
prestacao = (n2 / mes) * 100 #Não pode exceder 30% do salário
arre = ceil(prestacao)
if prestacao > ((30/100)*n3):
    print('Suas prestações vão ficar no valor \033[4;32mde R${}\033[m mensais. Seu empréstimo foi \033[1;31mcancelado\033[m'.format(arre))
else:
    print('Certo {}, seu empréstimo foi \033[1;32mliberado\033[m com sucesso. Suas prestações mensais serão no valor de R$:{}'.format(n1,arre))