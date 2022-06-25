def LeiaDinheiro(txt):
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! Informe um valor válido')
        else:
            valido = True
            return float(entrada)