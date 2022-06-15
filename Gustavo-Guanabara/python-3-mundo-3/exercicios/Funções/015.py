'''def linha():
    print('-=-'*30)

linha()
print('Teste')
linha()'''

'''def titulo(txt):
    print('-='*30)
    print(txt)
    print('-='*30)


titulo('Curso em vídeo')
titulo('Python')'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A com B é: {s}')
    
    
soma(b=4, a=5)'''

'''def contador(*num):
    for valor in num:
        print(f'{valor} ',end='')
    print('Fim')'''

'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} número')

contador(2,1,7)
contador(8,0)
contador(2,3,4,5,6,7)'''

'''def dobra(dobro):
    pos = 0
    while pos < len(dobro):
        dobro[pos] *= 2
        pos += 1


valores = [9,4,3,2,1]
dobra(valores)
print(valores)'''

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(s)


soma(5,2)
soma(2,9,4)
