s = 0
print('Os números ímpares e múltiplos de três são:')
for c in range(0,501,3):
    print(c)
    s += c
print('E a soma entre eles é {}'.format(s))