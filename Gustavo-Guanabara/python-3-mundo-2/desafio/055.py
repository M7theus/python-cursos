# Sem chegar a uma conclusão

s = 0
m = 0

for peso in range(0,5):
    pesos = float(input('Digite seu peso em Kg: '))
    s += pesos
    n = peso - s
print(s)
print(m)

for _ in range(0,5):
    if pesos > 0:
        a = pesos
        if pesos > n:
            print('O maior número é',pesos)
        else:
            print('O maior número é',m)
        