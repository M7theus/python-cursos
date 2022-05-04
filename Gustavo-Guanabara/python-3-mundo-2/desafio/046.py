from time import sleep
import emoji


n1 = int(input('De quantos segundos será a contagem regres siva dos fogos? '))
for c in range(0,n1+1):
    print(c)
    sleep(1)
    
print(emoji.emojize(':fireworks:'))