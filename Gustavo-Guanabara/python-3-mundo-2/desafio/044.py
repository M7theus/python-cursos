n1 = float(input('Qual o preço do produto? '))
n2 = int(input('Como será a forma de pagamento?\n [1.] À vista dinheiro/cheque: 10% de desconto.\n [2.] À vista no cartão: 5% de desconto.\n [3.] Em até 2x no cartão:preço normal.\n [4.] 3x ou mais no cartão: 20% de juros.\n [5.] Sair\n----> '))
if n2 == 1:
    print('Você escolheu a forma de pagamento à vista. Seu produto ficou no valor de R${}'.format(n1-(10/100)*n1))
elif n2 == 2:
    print('Você escolheu a forma de pagamento à vista no cartão. Seu produto ficou no valor de R${}'.format(n1-(5/100)*n1))
elif n2 == 3:
    print('Você escolheu a forma de pagamento em até 2x no cartão. Seu produto ficou no valor de duas prestações de R${}'.format(n1/2))
elif n2 == 4:
    print('Você escolheu a forma de pagamento em 3x ou mais no cartão. Seu produto ficou no valor de R${}'.format(n1+(20/100)*n1))
elif n2 ==5:
    print('Programa finalizado')