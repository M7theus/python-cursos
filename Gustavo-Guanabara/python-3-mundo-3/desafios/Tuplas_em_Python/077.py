palavras = ('Banana','Programador','Computador','Frase','Peixe','Casa','Pai','Mae','Irmao','Comida','Televisao','Python')

for palavra in palavras:
    print(f'\nPara {palavra.upper()} temos: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}\n',end='')


