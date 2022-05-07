n1 = int(input('Digite um número inteiro qualquer: '))
razao = int(input('Qual é a razão do número? '))


for c in range(n1,n1 + razao * 10,razao):
    print(c)
