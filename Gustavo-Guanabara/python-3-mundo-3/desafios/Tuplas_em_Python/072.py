nome = ('Zero','Um', 'Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quartoze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    pergunta = int(input('Digite um número entre 0 e 20: '))
    if 0 <= pergunta <= 20:
        break
    else:
        pergunta = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número: {nome[pergunta]}')

continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
while continuar not in 'SN':
    continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
while True:
    if continuar == 'S':
        pergunta = int(input('Digite um número entre 0 e 20: '))
        while True:
            if 0 <= pergunta <= 20:
                break
            else:
                pergunta = int(input('Digite um número entre 0 e 20: '))               
        print(f'Você digitou o número: {nome[pergunta]}')
    elif continuar == 'N':
        break
    continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
print('Fim do programa')
