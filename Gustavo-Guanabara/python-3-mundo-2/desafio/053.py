frase = str(input('Digite uma frase qualquer: ')).strip().upper()
fat = frase.split()
junto = ''.join(fat)
inverso = junto[::-1]
print('O inverso da palavra {} é {}'.format(junto,inverso))
if junto == inverso:
    print('Sua frase é um palíndromo')
else:
    print('Sua frase não é um palíndromo')
