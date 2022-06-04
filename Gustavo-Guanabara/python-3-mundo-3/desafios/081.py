lista = list()
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    pergunta = str(input('Você deseja continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break
lista.sort(reverse=True)
print(f'Foram digitados um total de {len(lista)}')
print(f'A ordem decrescente da lista é: {lista}')
if 5 in lista:
    print(f'O cinco foi digitado e se encontra nas posições: ')
    for p,v in enumerate(lista):
        if v == 5:
            print(p,end=' ')
else:
    print('O valor cinco não foi digitado na lista')