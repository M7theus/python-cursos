print('{:=^40}'.format(' Loja '))
n1 = float(input('Qual o preço do produto? '))
print('''Formas de pagamento:
[ 1 ] À vista dinheiro/cartão
[ 2 ] À Vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
    ''')
n2 = int(input('Qual será a forma de pagamento: '))
if n2 == 1:
    print('Você escolheu a forma de pagamento à vista. Seu produto ficou no valor de R${}'.format(n1-(10/100)*n1))
elif n2 == 2:
    print('Você escolheu a forma de pagamento à vista no cartão. Seu produto ficou no valor de R${}'.format(n1-(5/100)*n1))
elif n2 == 3:
    print('Você escolheu a forma de pagamento em até 2x no cartão. Seu produto ficou no valor de duas prestações de R${}'.format(n1/2))
elif n2 == 4:
    qtaparcela = int(input('Quantas vezes no cartão ? '))
    parcela = n1/qtaparcela
    print('Você escolheu a forma de pagamento em {}x no cartão. Seu produto ficou no valor de R${:.2f}'.format(qtaparcela ,(n1+(20/100)*n1)/qtaparcela))
else:
    print('Opção inválida, tente novamente')