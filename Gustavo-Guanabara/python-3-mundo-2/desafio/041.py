from datetime import date
n1 = date.today().year
n2 = int(input('Digite seu ano de nascimento: '))
print(n1-n2)
if n1 - n2 <= 9:
    print('Mirim')
elif n1 - n2 <= 14:
    print('Infantil')
elif n1 - n2 <= 19:
    print('Jnior')
elif n1 - n2 <= 20:
    print('Sênio')
else:
    print('Master')