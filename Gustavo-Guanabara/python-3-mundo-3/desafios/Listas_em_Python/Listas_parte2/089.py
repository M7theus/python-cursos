lista = list()
while True:
    nome = str(input('Digite seu nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2)/2
    lista.append([nome,[nota_1, nota_2],media])
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if pergunta in 'Nn':
        break 
print('-='*30)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*30)
for posicao, valor in enumerate(lista):
    print(f'{posicao:<4}{valor[0]:<10}{valor[2]:>8.1f}')
print('-='*30)
while True:
    pergunta = int(input('Qual nota gostaria de olhar? [999 para parar]: '))
    if pergunta == 999:
        break
    if pergunta <= len(lista)-1:
        print(f'Notas de {lista[pergunta][0]} são {lista[pergunta][1]}')