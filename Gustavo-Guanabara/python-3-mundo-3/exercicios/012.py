lanche = ('Pizza', 'Hambúrguer', 'Pudim', 'Bolo')
#print(lanche[-1])
#print(lanche[1:3])
#print(lanche[1:])
#print(lanche[:2])
#print(lanche[-1:])
'''for comida in lanche:
    print(f'Eu vou comer: {comida}')'''
for comida in range(0,len(lanche)):
    print(lanche[comida], comida)
'''for pos, comida in enumerate(lanche):
    print(f'{pos} {comida}')'''
#print(sorted(lanche))
'''a = (1,2,3)
b = (4,5,4,7)
c = a + b
print(c.count(2))
print(c.index(4,4))'''
#del(lanche)