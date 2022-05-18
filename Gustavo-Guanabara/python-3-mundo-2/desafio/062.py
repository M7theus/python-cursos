numero = int(input('Digite um número qualquer: '))
razao = int(input('Digite a razão: '))

n = 0
soma = numero - razao
while n != 10:
    n += 1
    soma += razao
    if n == 1:
        print('{}! = {}'.format(numero,soma), end=' ')
    else:
        print('{}'.format(soma), end =' ')
    if n == 10:
        pergunta = str(input('Você deseja inserir novos números? [S/N]: ')).upper()
        while pergunta == 'S':
            numero = int(input('Digite o novo número: '))
            razao = int(input('Digite a razão: '))
            n = 0
            soma = numero - razao
            while n != 10:
                n += 1
                soma += razao
                if n == 1:
                    print('{}! = {}'.format(numero,soma), end=' ')
                elif n == 10:
                    pergunta = str(input('Você deseja inserir novos números? [S/N]: ')).upper()
                else:
                    print('{}'.format(soma), end =' ')
        else:
            print('Fim do programa')
            
           
        

