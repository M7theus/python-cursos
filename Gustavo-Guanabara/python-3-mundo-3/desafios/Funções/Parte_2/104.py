def leiaInt(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            return n
            break
        print(f'Erro! Digite um número inteiro')
    
    
    
numero = leiaInt('Digite um número: ')  
print(f'O número informado foi o {numero}')  