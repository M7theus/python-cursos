lista = []
seg_lista = list()
pri = seg = ter = par = maior_segunda = soma_tres = maior = 0
c = 2
d= 3
for posicao in range(0,9):
    numero = int(input(f'Digite um valor para {[pri,seg]}: '))
    if numero % 2 == 0:
        par += numero
    if posicao == c:
        soma_tres += numero
        c += 3
    
    if posicao == d:
        if d == 1:
            maior = numero
        else:
            if numero > maior:
                maior = numero
        d += 1
        if d == 6:
            d = 0
    lista.append(numero)
    seg_lista.append(lista[:])
    lista.clear()
    
    seg += 1
    if posicao == 2:
        pri = 1
        seg = 0
    if posicao == 5:
        pri = 2
        seg = 0

print('-='*20)
while True:
    print(seg_lista[ter],end='')
    ter += 1
    if ter == 3:
        print()
    if ter == 6:
        print()
    if ter == 9:
        print()
        break
print(f'A soma entre todos os números pares é: {par}')
print(f'A soma entre os valores da terceira coluna é: {soma_tres}')
print(f'O maior valor da segunda coluna é: {maior}')
    