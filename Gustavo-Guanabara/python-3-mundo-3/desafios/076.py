from stringcolor import *

produtos = ('Lápis', 1.75, 'Borracha',2.21,'Apontador',3.89,'Caderno',22.94,'Corretivo',5.67,'Mochila',100.32,'Marcador',7.50)

print('-='*30)
print(f'{"Listagem de produtos":^60}')
print('-='*30)
for item in range(0,len(produtos)):
    if item % 2 == 0:
        print(cs(f'{produtos[item]:.<30}','#A63629',).bold(),end='')
    else:
        print(cs(f'{produtos[item]:>7.2f}','green').bold())