s = 0
d = 0

for c in range(0,7):
    n1 = int(input('Digite quantos anos você tem: '))
    if n1 > 21:
        s += 1
    else:
        d += 1
print('Dessas sete pessoas\n--> \033[1;32m{}\033[m São maiores de idade\n--> \033[1;31m{}\033[m São menores de idade'.format(s,d))
        
