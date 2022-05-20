'''c = 0
while True:
    print(c)
    c += 1'''
    
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
    