from random import randint, choice

cont = 0
cont_1 = 0
cont_2 = 0
cont_3 = 0
while True:
    chance = randint(1,2)
    lista = ['P','I']
    escolha_c = choice(lista)
    computador_num = int(randint(0,10))
    
    if chance == 1:
        print('Sinto muito, mas vou escolher primeiro')
        print('Pronto, já escolhir. E escolhir o número também')
        numero_p = int(input('Digite seu número: '))
        conta = (numero_p + computador_num)
        if escolha_c == 'P':
            if conta % 2 == 00:
                print('Eu venci')
                break
            else:
                print('Você venceu')
                cont += 1
        
        elif escolha_c == 'I':
            if conta % 2 == 1:
                print('Você venceu')
                cont_1 += 1
            else:
                print('Eu venci')
                break
        chance += 1
        
    else:
        vez = str(input('Escolha [Par] ou [Impar]: ')).strip().upper()[0]
        numero_p = int(input('Escolha seu número: '))
        conta = (numero_p + computador_num)
        if vez == 'P':
            if conta % 2 == 00:
                print('Você venceu')
                cont_2 += 1
            else:
                print('Eu venci')
                break
        if vez == 'I':
            if conta % 2 == 1:
                print('Você ganhou')
                cont_3 += 1
            else:
                print('Você perdeu')
                break
print(cont + cont_1 + cont_2 + cont_3)
        