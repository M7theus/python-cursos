def ajuda(txt):
    print(help(txt))

comando = ''
while True:
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)