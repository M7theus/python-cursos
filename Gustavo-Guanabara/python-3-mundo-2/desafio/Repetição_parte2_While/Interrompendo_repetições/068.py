from random import randint, choice
lista = ['Par','Impar']
cont = 0
print('='*20)
print('Par ou Ímpar')
print('='*20)

while True:
    ale = randint(1,2)
    escolha = choice(lista)
    numero_c = randint(0,10)
    if ale == 1:
        print(f'Sinto muito, mas vou escolher primeiro!\ne minha escola será {escolha}')
        usuario = int(input('Digite seu número: '))
        soma = usuario + numero_c
        if escolha == 'Par':
            if soma % 2 == 0:
                print(f'Ganhei!\nescolhir o número {numero_c}')
                break
            elif soma % 2 != 0:
                print(f'Você ganhou\nescolhir o número {numero_c}')
                print('')
        elif escolha == 'Impar':
            if soma % 2 != 0:
                print(f'Ganhei!\nescolhir o número {numero_c}')
                break
            elif soma % 2 == 0:
                print(f'Você ganhou\nescolhir o número {numero_c}')
                print('')
    else:
        escolha_u = str(input('Escolha [P/I]: ')).strip().upper()[0]
        while escolha_u not in 'P''I':
            escolha_u = str(input('Escolha [P/I]: ')).strip().upper()[0]
        usuario = int(input('Digite seu número: '))
        soma = usuario + numero_c
        if escolha_u == 'P':
            if soma % 2 == 0:
                print(f'Parabéns! Você ganhou\nescolhir o número {numero_c}')
            else:
                print(f'Você perdeu\nescolhir o número {numero_c}')
                break
        elif escolha_u == 'I':
            if soma % 2 != 0:
                print(f'Você ganhou\nescolhir o número {numero_c}')
            else:
                print(f'Você perdeu\nescolhir o número {numero_c}')
                break
    cont += 1
print(f'Fim do jogo, você perdeu\nO usuário teve {cont} vitórias')