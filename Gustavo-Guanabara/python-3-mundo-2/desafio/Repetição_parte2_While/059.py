numeros = int(input('Quantos números você deseja digitar? '))

soma = 0
multiplicacao = 1
divisao = 1
maior = 0
menor = 0
quantidade = 0

for numero in range(1,numeros+1):
    numeros1 = int(input('Digite o {} número: '.format(numero)))
    quantidade += 1
    soma += numeros1
    multiplicacao *= numeros1
    divisao /= numeros1
    if numero == 1:
        maior = numeros1
        menor = numeros1
    else:
        if maior < numeros1:
            maior = numeros1
        elif menor > numeros1:
            menor = numeros1

print('''
[ 1 ] Somar
[ 2 ] Multiplicação
[ 3 ] Divisão
[ 4 ] Maior
[ 5 ] Menor
[ 6 ] Novos números
[ 7 ] Sair
      ''')
opcao = 0
while opcao != 7:
    opcao = int(input('Qual opção você deseja? '))
    if opcao == 1:
        print('A soma entre os {} números é {}'.format(quantidade,soma))
    elif opcao == 2:
        print('A multiplicação entre os {} números é {}'.format(quantidade,multiplicacao))
    elif opcao == 3:
        print('A divisão entre os {} números é {:.2f}'.format(quantidade,divisao)) 
    elif opcao == 4:
        print('O maior números entre os {} números é {}'.format(quantidade,maior))
    elif opcao == 5:
        print('O menor números entre os {} números é {}'.format(quantidade,menor))
    elif opcao == 6:
        numeros1 = int(input('Quantos números você deseja digitar? '))

        soma = 0
        multiplicacao = 1
        divisao = 1
        maior = 0
        menor = 0
        quantidade = 0

        for numero in range(1,numeros1+1):
            numeros1 = int(input('Digite o {} número: '.format(numero)))
            quantidade += 1
            soma += numeros1
            multiplicacao *= numeros1
            divisao /= numeros1
            if numero == 1:
                maior = numeros1
                menor = numeros1
            else:
                if maior < numeros1:
                    maior = numeros1
                elif menor > numeros1:
                    menor = numeros1
            if opcao == 1:
                print('A soma entre os {} números é {}'.format(quantidade,soma))
            elif opcao == 2:
                print('A multiplicação entre os {} números é {}'.format(quantidade,multiplicacao))
            elif opcao == 3:
                print('A divisão entre os {} números é {}'.format(quantidade,divisao)) 
            elif opcao == 4:
                print('O maior números entre os {} números é {}'.format(quantidade,maior))
            elif opcao == 5:
                print('O menor números entre os {} números é {}'.format(quantidade,menor))