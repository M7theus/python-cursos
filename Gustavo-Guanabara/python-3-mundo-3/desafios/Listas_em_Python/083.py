expressao = str(input('Digite sua expressão: '))
lista = list()
for ex in expressao:
    if ex == '(':
        lista.append(ex)
    elif ex == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão não está correta')    