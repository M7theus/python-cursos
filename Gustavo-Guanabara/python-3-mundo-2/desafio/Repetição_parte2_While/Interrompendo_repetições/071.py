valor = int(input('Digite o valor que queira sacar: '))
total = valor
cedula = 100
cont = 0
while True:
    if total >= 100:
        total -= cedula
        cont += 1
        print(f'{cont} Notas de R$ 100')
    else:
        cont = 0
        if total >= 50:
            cedula = 50
            total -= cedula
            cont += 1
            print(f'{cont} Notas de R$ 50')
        if total >= 20:
            cedula = 20
            total -= cedula
            cont += 1
            print(f'{cont} Notas de R$ 20')
        if total >= 10:
            cedula = 10
            total -= cedula
            cont += 1
            print(f'{cont} Notas de R$ 10')
        if total >= 5:
            cedula = 5
            total -= cedula
            cont += 1
            print(f'{cont} Notas de R$ 5')
        if total >= 0:
            cedula = 1
            total -= cedula
            cont += 1
            print(f'{cont} Notas de R$ 1')
        if total == 0:
            break
            
