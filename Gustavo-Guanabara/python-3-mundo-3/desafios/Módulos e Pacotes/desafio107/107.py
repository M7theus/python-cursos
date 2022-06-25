import moeda

preco = float(input('Digite o preço da moeda: '))
print(f'A metade de {preco} é: {moeda.metade(preco)}')
print(f'O dobro de {preco} é: {moeda.dobro(preco)}')
print(f'Aumento de 18%: {moeda.aumento(preco,18)}')
print(f'Redução de 13% é: {moeda.redução(preco,13)}')