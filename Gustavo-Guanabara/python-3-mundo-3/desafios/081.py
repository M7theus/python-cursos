lista = list()
contagem = quan_cinco = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 5:
        quan_cinco += 1
    contagem += 1
    lista.append(numero)
    lista.sort(reverse=True)
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'Foram digitados um total de {contagem} números')
print(f'A ordem decrescente dos números foi: {lista}')

if 5 in lista:
    if quan_cinco > 1:
        for posi in range(0,quan_cinco):
            print(f'{lista.index(5,posi)+1}') 
    else:
        print(f'O número cinco foi digitado e se encontra na posição {lista.index(5)+1}')      
else:
    print('O valor cinco não foi digitado')