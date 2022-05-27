tabela = ('Corinthians','Palmeiras','São Paulo','Atlético-MG','Botafogo','Santos', 'Fluminense', 'Coritiba','América-MG','Avaí','Internacional','Athletico-PR','Bragantino','Flamengo','Goiás','Cuiabá','Atlético-GO','Juventude','Ceará','Fortaleza')
a = str(tabela).split()
print(f'Os 5 colocados são: {tabela[0:5]}')
c = 0
b = 16
print('Os 5 últimos colocados são:')
while c != 5:
    print(f'{a[b::-20]}',end='')
    c += 1
    b += 1
print(f'A ordem alfabética dos times é: {sorted(tabela)}')

nome = input('Digite o nome de um desses times para saber em qual posição ele se encontra na tabela: ').title()
print(tabela.index(nome))