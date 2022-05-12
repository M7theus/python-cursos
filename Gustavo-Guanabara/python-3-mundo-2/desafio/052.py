numero = int(input('Digite um número qualquer: '))

if numero > 1:
    
    for c in range(2,numero+1):
        
        if (numero % c) == 0:
            print('{} não é primo'.format(numero))
            
    else:
        print('{} é primo'.format(numero))
    
else:
    print('O número {}'.format(numero))