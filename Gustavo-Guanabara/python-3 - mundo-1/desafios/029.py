import emoji

n1 = float(input('Digite seus Km/h: '))
n2 = n1 - 80
if n1 > 80:
    print(emoji.emojize('Você foi multado :police_car_light:, a sua multa será de \033[1;31mR${}\033[m'.format(7*n2)))
else:
    print(emoji.emojize('Você não foi multado, parabéns! :oncoming_police_car:'))
print('--FIM--')