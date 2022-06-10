n1 = float(input('Qual será a distância da viagem em Km/H? '))
if n1 <= 200:
    print('O preço da passagem será de \033[4;32mR${}\033[m'.format(n1 * 0.50))
else:
    print('O preço da passagem será de \033[4;32mR${}\033[m'.format(n1 * 0.45))
print('==FIM==')