n1 = float(input('Digite sua altura em metros: '))
n2 = float(input('Digite seu peso em Kg: '))
imc = n2/(n1*n1)
if imc < 18.5:
    print('Você está abaixo do peso. Seu IMC é {}'.format(imc))
elif imc <= 25:
    print('Você está com o peso ideal. Seu IMC é {:.2f}'.format(imc))
elif imc <= 30:
    print('Você está com sobrepeso. seu IMC é {:.2f}'.format(imc))
elif imc <= 40:
    print('Você está obeso. Seu IMC é {:.2f}'.format(imc))
else:
    print('Você está mórbido. Seu IMC é {:.2f}'.format(imc)) 
