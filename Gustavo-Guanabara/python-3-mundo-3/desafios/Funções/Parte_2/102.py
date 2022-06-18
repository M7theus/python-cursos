def fatorial (digito): #Faz a conta
    global numero
    cont = numero
    conta = 1
    while cont != 0:
        conta *= cont
        cont -= 1
    return conta
    if show == True:
        def show(): #Mostra o passo
            global numero
            cont = numero
            while cont != 0:
                if cont > 1:
                    print(f' {"x"} ',end='')
                if cont == 1:
                    print(f' {"="} ',end='')
                cont -= 1
            return cont
        


numero = int(input('Digite um número: '))
print(fatorial(5), show=True)