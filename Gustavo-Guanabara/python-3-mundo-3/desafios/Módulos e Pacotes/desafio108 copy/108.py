import moeda

preco = float(input('Digite o preço da moeda: '))
print(f'A metade de {moeda.moeda(preco)} é: {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é: {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumento de 18%: {moeda.moeda(moeda.aumento(preco))}')
print(f'Redução de 13% é: {moeda.moeda(moeda.redução(preco))}')