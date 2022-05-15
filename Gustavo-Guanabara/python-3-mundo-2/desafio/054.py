from datetime import datetime
ano = datetime.today().year
print(ano)
s = 0
n = 0



for pessoa in range(1,8):
    pessoas = int(input('Digite o ano de nascimento da {} pessoa: '.format(pessoa)))
    idade = ano - pessoas
    if idade >= 21:
        s += 1
    else:
        n += 1
print('Do total das {} pessoas\n-->{} São maiores de idade\n-->{} São menores de idade'.format(pessoa,s,n))