lista = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense','Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminenser','Sport Recife','EC Vitória','Coritiba','Avai','Ponte Preta','Atlético-GO')

print('\033[1;34m=\033[m' *35)
print(f'A lista dos times completos é: ')
for time in lista:
    print(f'{ time }',end='')
print('')
print('\033[1;34m=\033[m' *35)
print(f'Os 5 primeiros times são: {lista[:5]}')
print('\033[1;34m=\033[m' *35)
print(f'Os 5 últimos times são: {lista[-5:]}')
print('\033[1;34m=\033[m' *35)
print(f'A ordem alfabética dos times é: {sorted(lista)}')
print('')
print('\033[1;34m=\033[m' *35)
print(f'O time da Chapecoense encontra-se na posição: {lista.index("Chapecoense")+1}')