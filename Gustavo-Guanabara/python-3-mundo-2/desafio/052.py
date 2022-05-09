#Não conseguir chegar a uma lógica

numero = int(input('Digite qualquer número inteiro: '))

for c in range(1, numero+1):
    print(c, end=" ")
if numero:
    print(c,'Maior')
else:
    print(c, 'Menor')