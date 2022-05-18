from math import floor

numero = int(input('Digite qualquer número: '))
novo = numero
novo1 = numero

n = 0
while n != 10:
    
    #Sequência de frente
    divisao = floor(novo/1.6)
    soma = divisao + novo
    novo = soma
    print(soma, end=' ')
    
    
    #Sequência de tráz
    divisao1 = floor(novo1/1.6)
    novo1 = divisao1
    print(divisao1, end=' ')

    n += 1
    
print('De frente: ')
