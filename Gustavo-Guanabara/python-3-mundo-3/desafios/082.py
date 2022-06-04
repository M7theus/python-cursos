lista = list()
lista_par = list()
lista_impar = list()
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    pergunta = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break
for valor in lista:
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
           
print(lista)
print(lista_par)
print(lista_impar)








