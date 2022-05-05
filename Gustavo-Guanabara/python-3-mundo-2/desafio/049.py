from re import A


print('-='*20)
print('Tabuada')
print('=-'*20)


# 1 
# 1 + 1 
# 1 + 1 + 1

n1 = int(input('Digite o número que deseja vê a tabuada: '))
for c in range(0, 11):
    print('{} X {} = {}'.format(c, n1, n1 * c))
