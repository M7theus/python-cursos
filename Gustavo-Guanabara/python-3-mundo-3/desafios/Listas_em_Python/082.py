lista = list()
lista_par = []
lista_impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break

print(f'Sua lista completa ficou: {lista}')
for par in lista:
    if par % 2 == 0:
        lista_par.append(par)
    else:
        lista_impar.append(par)
print(f'Sua lista par ficou: {lista_par}')
print(f'Sua lita ímpar ficou: {lista_impar}')





