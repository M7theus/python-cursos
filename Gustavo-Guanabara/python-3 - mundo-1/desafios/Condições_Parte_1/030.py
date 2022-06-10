n1 = int(input('Digite qualquer número inteiro: '))
if n1 % 2 == 0:
    print('O número \033[1;35m{}\033[m é \033[4;33;42mpar\033[m'.format(n1))
else:
    print('O número \033[1;36m{}\033[m é \033[4;37;45mímpar\033[m'.format(n1))
print('--FIM--')