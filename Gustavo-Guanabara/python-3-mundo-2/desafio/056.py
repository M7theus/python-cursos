from datetime import date

data = date.today().year


soma = 0
novo = 0
pnome = 0
vnome = 0
velho = 0
f = 0
m = 0


for tabela in range(1,5):
    print('\033[1;31m-\033[m'*7,'\033[1;37m{}_Pessoa\033[m'.format(tabela),'\033[1;32m-\033[m'*7)
    nome = str(input('Digite seu nome: ')).title().strip()
    ano = int(input('Digite seu ano de nascimento: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    idade = data - ano
    
    if tabela == 1:
      novo = idade
      pnome = nome
    else:
        if novo > idade:
            novo = idade
            pnome = nome
            
    if tabela == 1:
        vnome = nome       
        velho = idade
    else:
        if velho < idade:
            vnome = nome
            velho = idade
    
    if sexo == 'M':
        m += 1
    if sexo == 'F':
        f += 1    
print(' ')
media = idade / tabela
print('A média das idades é: \033[1;36m{}\033[m'.format(media))
print('A pessoa mais nova dentre os \033[1;37m{}\033[1;m é {} e possue {} anos'.format(tabela,pnome,novo))
print('A pessoa mais velha dentre os \033[1;33m{}\033[m é {} e possue {} anos'.format(tabela,vnome,velho))
print('Dessa lista de {} pessoas:\n--> \033[1;34m{}\033[m São homens\n--> \033[1;35m{}\033[m São mulheres'.format(tabela,m,f))