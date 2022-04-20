print('Cidade')
n1 = str(input('Digite o nome de qualquer cidade: ')).capitalize().strip().split()
n2 = 'Santo' in n1[0]
print('Sua cidade começa com santo: {}'.format(n2))
