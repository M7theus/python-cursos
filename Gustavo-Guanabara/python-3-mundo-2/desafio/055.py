maior = 0
menor = 0

for peso in range(1,6):
    pesos = float(input('Digite o peso da {} pessoa: '.format(peso)))
    if peso == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos

print('Maior peso: {}'.format(maior))
print('Menor peso {}'.format(menor))
        
    
        