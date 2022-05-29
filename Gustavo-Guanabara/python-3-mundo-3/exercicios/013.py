'''num = [2,5,9,1]
num[2] = 3 #Troca o termo
num.append(7) #Adiciona um novo elemento
num.sort(reverse=True) #Ordem inversa
num.insert(2, 2) #Adiciona um novo elemento em uma determinada posição
if 4 in num:
    num.remove(4)
else:
    print('Não há o valor 4 nessa lista')
num.pop(2) #Remove determinado elemento
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for posicao,valor in enumerate(valores):
    print(f'Encontrei o {valor} na posição {posicao}')