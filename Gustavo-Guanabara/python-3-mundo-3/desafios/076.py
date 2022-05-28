lista = ('Tomate', 3.40,'Banana',2.30,'Maça',4.59,'Manga',5.96,'Acerola',2.43)
preco = 'LISTAGEM DE PREÇOS'
print('-'*40)
print(f'{preco:^40}')
print('-'*40) 
for termo,preco in lista:
    print(f'{termo[0::1]:10} --> {preco[1::1]:10}')