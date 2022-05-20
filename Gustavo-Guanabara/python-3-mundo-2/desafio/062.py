numero = int(input('Digite um número: '))
razao = int(input('Digite sua razão: '))

c = 0
soma = numero
pergunta = 10
while pergunta != 0:
    while c != pergunta:
        print(soma)
        soma += razao
        c += 1
    if c == pergunta:
        pergunta = int(input('Novos números: '))
        c = 0
print('Fim do programa')