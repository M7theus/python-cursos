lista = lista_par = lista_impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break

for posicao in range(0,len(lista)):
    if lista[posicao] % 2 == 0:
        del lista[posicao]
lista_par = lista[:]
        
print(f'Lista completa:  {lista}')
print(f'Lista par: {lista_par}')




