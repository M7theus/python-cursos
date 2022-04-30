n1 = float(input('Digite o valor da sua primeira nota: '))
n2 = float(input('Digite o valor da sua segunda nota: '))
media = (n1 + n2)/2
if media <= 5.0:
    print('Reprovado')
elif media >= 7.0:
    print('Aprovado')
else:
    print('Recuperação')