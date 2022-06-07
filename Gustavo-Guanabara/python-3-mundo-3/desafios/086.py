lista = []
seg_lista = list()
pri = seg = ter = 0
for posicao in range(0,9):
    lista.append(int(input(f'Digite um valor para {[pri, seg]}: ')))
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
    
        
    