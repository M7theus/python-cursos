from random import randint,choice
from time import sleep
import emoji

print('Que tal um jogo? Ímpar ou Par?')
print('')
numero = cont = 0
while True:
    list = ['Par','Impar']
    escolha_c = choice(list)

    vez_c = randint(1,2)
    numero_c = randint(0,10)
    
    if vez_c == 1:
        print('Sinto muito, mas vou escolher')
        print('Hmm...')
        sleep(1)
        numero_p = int(input('Pronto! Digite seu número agora: '))
        soma = (numero_p + numero_c)
        print('Hmm...')
        sleep(1)
        print('')
        if escolha_c == 'Par':
            if soma % 2 == 0:
                print(f'Eu \033[1;31mvenci!\033[m Escolhir \033[1;37m{escolha_c}\033[m e meu número foi \033[1;37m{numero_c}\033[m')
                break
            else:
                print(f'Você \033[1;32mvenceu.\033[m Escolhir \033[1;37m{escolha_c}\033[m e meu número foi \033[1;37m{numero_c}\033[m')
                cont += 1
        if escolha_c == 'Impar':
            if soma % 2 != 0:
                print(f'Eu \033[1;31mvenci!\033[m Escolhir \033[1;37m{escolha_c}\033[m e meu número foi \033[1;37m{numero_c}\033[m')
                break
            else:
                print(f'Você \033[1;32mvenceu.\033[m Escolhir \033[1;37m{escolha_c}\033[m e meu número foi \033[1;37m{numero_c}\033[m')
                cont += 1
        vez_c = 0
        
    if vez_c == 2:
        numero += cont
        print('Certo, você escolhe primeiro')
        escolha_p = str(input('[Par] ou [Impar]: ')).strip().upper()[0]
        print('Já escolhir meu número. Escolha o seu agora!')
        numero_p = int(input('Digite seu número: '))
        soma = (numero_p + numero_c)
        print('Hmm...')
        sleep(1)
        print('')
        if escolha_p == 'P':
            if soma % 2 == 0:
                print(f'Você \033[1;32mvenceu.\033[m Escolhir o número \033[1;37m{numero_c}\033[m')
                cont += 1
            else:
                print(f'Eu \033[1;31mvenci!\033[m Escolhir o número \033[1;37m{numero_c}\033[m')
                break
        if escolha_p == 'I':
            if soma % 2 != 0:
                print(f'Você \033[1;32mvenceu.\033[m Escolhir o número \033[1;37m{numero_c}\033[m')
                cont +=1
            else:
                print(f'Eu \033[1;31mvenci!\033[m Escolhir o número \033[1;37m{numero_c}\033[m')
                break
        vez_c = 0
numero += cont
print('')
print('\033[35m-=-\033[m'*20)
print(emoji.emojize(f'Fim de jogo :skull:. Você teve um total de \033[1;34m{cont}\033[m vitórias'))
print('\033[35m-=-\033[m'*20)