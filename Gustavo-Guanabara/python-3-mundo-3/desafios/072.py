nome = ('Zero','Um', 'Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quartoze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

pergunta = 22
while pergunta > 20 or pergunta < 0:
    pergunta = int(input('Digite um número entre 0 e 20: '))

print(nome[pergunta])

for palavra in range(0,len(nome)):
    print(nome[palavra],palavra)
    
    