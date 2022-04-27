from datetime import date
n1 = int(input('Digite o ano de nascimento: '))
n2 = date.today().year
if n2 - n1 < 18:
    print('Falta {} anos para você ter que se alistar'.format(18-(n2 - n1)))
elif n2 - n1 == 18:
    print('Você possui 18 anos e está no tempo de se alistar')
else:
    print('Você já está {} anos atrasado para se alistar'.format(-(18-(n2 - n1))))

    