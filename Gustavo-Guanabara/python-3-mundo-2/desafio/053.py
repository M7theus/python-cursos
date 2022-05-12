frase = str(input('Digite uma frase qualquer: ')).strip()
n2 = len(frase)
n3 = frase.count(' ')
n4 = n2 - n3
print(n4)

for c in range(1,n4+1):
    print(c, end=' ')
