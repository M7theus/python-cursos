import moeda

preco = float(input('Digite o preço da moeda: '))
print(f'A metade de {moeda.formatacao(preco)} é: {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.formatacao(preco)} é: {moeda.dobro(preco, True)}')
print(f'O aumento de 10% sobre o {moeda.formatacao(preco)} é: {moeda.aumento(preco, 10, True)}')
print(f'A redução de 20% sobre o {moeda.formatacao(preco)} é: {moeda.redução(preco,20,True)}')