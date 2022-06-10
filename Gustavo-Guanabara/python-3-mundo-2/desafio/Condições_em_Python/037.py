n1 = int(input('Digite qualquer número inteiro: '))
n2 = int(input('Digite\n\033[4;32m[ 1 ]\033[m para conversão \033[1;35mbinária\033[m\n\033[4;33m[ 2 ]\033[m para \033[1;36moctal\033[m\n\033[4;34m[ 3 ]\033[m para \033[1;37mhexadecimal\033[m: '))
if n2 == 1:
    print('{}'.format(bin(n1)[2:]))
elif n2 == 2:
    print('{}'.format(oct(n1)[2:]))
elif n2 == 3:
    print('{}'.format(hex(n1)[2:]))
else:
    print('Opção inválida.Tente novamente')