numero = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

c = 0
soma = numero
while c != 10:
    print('{} '.format(soma),end='')
    soma += razao
    c += 1
    if c == 10:
        pergunta = int(input('Deseja mostrar mais quantos termos? '))
        if pergunta == 0:
            print('Programa finalizado com sucesso. {} termos mostrados'.format(c))
        else:
            d = 0
            while d != pergunta:
                print('{} '.format(soma),end='')
                soma += razao
                d += 1
            if d == pergunta:
                pergunta = int(input('Deseja mostrar mais quantos termos? '))
                d = 0
                while d != pergunta:
                    print('{} '.format(soma),end='')
                soma += razao
                d += 1
                
print('Fim do programa')
        

