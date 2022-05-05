print('Logo abaixo, digite 6 números inteiro')

s = 0
for c in range(0,6):
    n1 = int(input('Digite um número: ')) 
    if n1 % 2 == 0:
        s += n1
print(s)