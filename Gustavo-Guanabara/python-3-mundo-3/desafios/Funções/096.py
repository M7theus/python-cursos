def area (largura, comprimento):
    a = (largura * comprimento)
    print(f'A área da {largura} largura com {comprimento} de comprimento é: {a:.1f}')

largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento do terreno (m): '))
area(largura, comprimento)