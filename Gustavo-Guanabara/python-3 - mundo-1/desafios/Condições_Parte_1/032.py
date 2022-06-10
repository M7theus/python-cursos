from datetime import date

n1 = int(input('Digite em qual ano você se encontra atualmente: Coloque 0 para analisar o ano atual:'))

if n1 == 0:
    n1 = date.today().year
if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('O ano \033[7;30m{}\033[m é bissexto'.format(n1))
else:
    print('O ano \033[0;36;44m{}\033[m não é bissexto'.format(n1))
print('**FIM**')