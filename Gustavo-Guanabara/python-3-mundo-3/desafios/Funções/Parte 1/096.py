def area (largura, comprimento):
    a = (largura * comprimento)
    print(f'A área de um terreno {largura} x {comprimento} é de {a}m')

largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento do terreno (m): '))
area(largura, comprimento)