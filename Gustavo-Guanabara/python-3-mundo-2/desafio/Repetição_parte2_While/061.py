#Laço while
'''numero = int(input('Digite seu número: '))
razao = int(input('Digite a razão: '))

cont = 0
soma = numero
while cont != 10:
    print('{} '.format(soma),end='')
    soma += numero
    cont += 1
print('FIM')'''

#Laço for

numero = int(input('Digite um número qualquer: '))
razao = int(input('Digite sua razao: '))

c = 0
conta = numero
for c in range(0,10):
    print(conta, end='')
    conta += razao
    c += 1