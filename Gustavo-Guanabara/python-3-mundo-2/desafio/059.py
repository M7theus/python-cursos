menu = 0
soma = 0
multiplicacao = 1
maior = 0
menor = 0



numeros = int(input('Quantos números você deseja realizar a análise? '))
for numero in range(1,numeros+1):
    n1 = int(input('Digite o {} número: '.format(numero)))
    soma += n1
    multiplicacao *= n1
    if numero == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
print('Okay.\nAgora escolha o que deseja fazer com esses números: ')
print('''
        \033[1;37m[1] Somar\033[m
        \033[1;35m[2] Multiplicar\033[m
        \033[1;37m[3] Maior\033[m
        \033[1;35m[4] Menor\033[m
        \033[1;37m[5] Novos números\033[m
        \033[1;35m[6] Sair\033[m
        ''')
while menu != 6:
    menu = int(input('Qual opção deseja submeter seus números?: '))
    if menu == 1:
        print('A soma entre os {} é \033[1;32m{}\033[m'.format(numeros, soma))
    if menu == 2:
        print('A multiplicação entre os {} é \033[1;32m{}\033[m'.format(numeros, multiplicacao))
    if menu == 3:
        print('O maior número entre os {} é o \033[1;32m{}\033[m'.format(numeros, maior))
    if menu == 4:
        print('O menor número entre os {} é o \033[1;32m{}\033[m'.format(numeros, menor))
        
    if menu == 5:
        soma *= 0
        maior *= 0
        menor *= 0
        numeros = int(input('Quantos números você deseja realizar a análise? '))
        for numero in range(1,numeros+1):
            n1 = int(input('Digite o {} número: '.format(numero)))
            soma += n1
            multiplicacao *= n1
            if numero == 1:
                maior = n1
                menor = n1
            else:
                if n1 > maior:
                    maior = n1
                if n1 < menor:
                    menor = n1
            if menu == 1:
                print('A soma entre os {} é \033[1;32m{}\033[m'.format(numeros, soma))
            if menu == 2:
                print('A multiplicação entre os {} é \033[1;32m{}\033[m'.format(numeros, multiplicacao))
            if menu == 3:
                print('O maior número entre os {} é o \033[1;32m{}\033[m'.format(numeros, maior))
            if menu == 4:
                print('O menor número entre os {} é o \033[1;32m{}\033[m'.format(numeros, menor))
print('Programa finalizado com sucesso')           
                