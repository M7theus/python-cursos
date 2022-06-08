lista = list()
total = []
nomes = 0
cont = 0
while True:
    lista.append(str(input('Nome: ')).title())
    nomes += 1
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    lista.append((lista[1] + lista[2])/2)
    total.insert(0, lista[0])
    total.insert(1, lista[1:3])
    total.insert(2, lista[3])
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    cont += 1
    if pergunta in 'Nn':
        break
print('-='*20)
print(f'No. Nome          média')

print(total)

    