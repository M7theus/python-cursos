lista = lista_par = lista_impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
    
lista_par = lista[:]
lista_impar = lista[:]
q = 0
for par in lista_par:
    if par % 2 == 1:
        del lista_par[q]
    q += 1

print(f'Lista completa:  {lista}')
print(lista_par)








