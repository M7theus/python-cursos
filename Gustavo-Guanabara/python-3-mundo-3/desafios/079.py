valores = list()
n = 0
while True:
    numero = int(input('Digite um número qualquer: '))
    valores.append(numero)
    
    a = valores.count(numero)
    if a > 1:
        print('Número repetido, vou retirar da listagem')
        del valores[n]
    pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
    n += 1
print(valores)