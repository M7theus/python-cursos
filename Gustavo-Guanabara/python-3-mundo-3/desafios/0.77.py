palavras = ('Banana','Programador','Computador','Frase','Peixe','Casa','Pai','Mae','Irmao','Comida','Televisao',)
consoantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',)

for frases in palavras:
    print(f'Na palavra {frases.upper()}')
    
for palavra in consoantes:
    print((frases - palavra))