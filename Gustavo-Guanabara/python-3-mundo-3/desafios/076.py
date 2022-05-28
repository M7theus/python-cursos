quantidade = int(input('Quantos produtos você deseja cadastrar no sistema: '))

for produto in range(0,quantidade):
    lista = (str(input('Escreva o nome do produto: ')), int(input('Preço do produto R$ ')))
print(lista)