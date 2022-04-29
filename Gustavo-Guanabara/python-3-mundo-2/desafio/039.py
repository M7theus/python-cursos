from datetime import date
data = date.today().year
n1 = int(input('Digite seu ano de nascimento: '))
n2 = str(input('Digite seu sexo [M/F]: ')).upper()
idade = data - n1

if n2 == 2:
    print('Você não precisa se alistar')
elif idade < 18:
    dado = 18 - idade + n1
    falta = 18 - idade
    print('Vocẽ ainda possui {} anos e portanto, não está no periodo de alistamento militar'.format(idade))
    print('Falta {} anos para você se alistar'.format(falta))
    print('Volte em {}'.format(dado))
elif idade > 18:
    dado = -idade + 18 + n1
    print('Você possui {} anos e passou do tempo para se alistar'.format(idade))
    print('Era para você ter se alistado em {}'.format(dado))
else:
    print('Você possue {} anos e está no tempo certo para realizar o alistamento'.format(idade))
