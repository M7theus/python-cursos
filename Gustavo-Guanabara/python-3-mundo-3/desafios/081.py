lista = []
while True:
    lista.append(int(input('Digiteu um número: ')))
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break
lista.sort(reverse=True)
print(f'Foram digitados um total de {len(lista)}')
print(f'A lista em forma decrescente torna-se: {lista}')
if 5 in lista:
    print(f'O valor cinco encontra-se na lista e suas respectivas possições são: ',end='')
    for p,v in enumerate(lista):
        if v == 5:
            print(p)
else:
    print('O valor cinco não se encontra presente na lista')