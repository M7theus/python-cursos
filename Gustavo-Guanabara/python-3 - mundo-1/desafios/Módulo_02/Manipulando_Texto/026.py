n1 = str(input('Digite uma frase qualquer: ')).upper().strip()
print('A letra A aparece {} vezes'.format(n1.count('A')))
print('A primeira letra A aparece na posição {}'.format(n1.find('A')+1))
print('A última letra A aparece na posição {}'.format(n1.rfind('A')+1))