soma = 0

mnome = 0
midade = 0

fidade = 0
s = 0
m = 0

for rela in range(1,5):
    print('-'*5, '{} Pessoa'.format(rela), '-'*5)
    nome = str(input('Digite seu nome: ')).strip().title()
    idade = float(input('Digite sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    if rela == 1:
        mnome = nome
        midade = idade
    else: 
        if idade > midade:
            midade = idade
            mnome = nome   
            
    if rela == 1:
        fidade = idade
    else:
        if sexo == 'M':
            sexo = 'M'
        elif fidade < 20:
            s += 0
        else:
            m += 1

media = soma / rela
print('A média de idade do grupo é de {} anos'.format(media))   

print('A pessoa mais velho tem {} anos e se chama {}'.format(midade,mnome)) 

print('Ao todo são {} mulheres com mais de 20 anos'.format(m))