print('='*15)
print('Banco - ')
print('='*15)

valor = int(input('Digite o valor a ser sacado: '))
ced_50 = 50
cont_50 = 0

result_50 = valor

ced_20 = 20
cont_20 = 0

ced_10 = 10
cont_10 = 0

ced_1 = 1
cont_1 = 0
while True:
    while result_50 >= 0:
        print(f'{cont_50} 50')
        cont_50 += 1
        result_50 -= ced_50
    if result_50 == 0:
        break
    else:
        sub_20 = result_50
        while sub_20 >= 0:
            print(f'{cont_20} 20')
            cont_20 += 1
            sub_20 -= ced_20
        if sub_20 == 0:
            break
        else:
            sub_10 = sub_20
            while sub_10 >= 0:
                print(f'{cont_10} 10')
                cont_10 += 1
                sub_10 -= ced_10
            if sub_10 == 0:
                break
            else:
                sub_1 = sub_10
                while sub_1 >= 0:
                    print(f'{cont_1} 1')
                    cont_1 += 1
                    sub_1 -= ced_1
                break

