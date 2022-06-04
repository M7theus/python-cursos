exprecao = str(input('Digite sua expresão: '))
soma = []
for simb in exprecao:
    if simb == '(':
        soma.append('(')
    elif simb == ')':
        if len(soma) > 0:
            soma.pop()
        else:
            soma.append(')')
            break
if len(soma) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')
    