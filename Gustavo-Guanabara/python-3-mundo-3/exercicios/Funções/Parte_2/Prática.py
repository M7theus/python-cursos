'''def fatorial(num = 1):
    f = 1
    for cont in range(num,0,-1):
        f *= cont
        return f

n = int(input('Digite um número: '))
print(f'O fatorial de n é igual a:{ fatorial(n)}')'''

def Par(num=0):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
    

num = int(input('Digite um número: '))
print(Par(num))
if Par(num):
    print(f'É par')
else:
    print('Não é par')