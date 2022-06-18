from datetime import datetime
ano_atual = datetime.now().year

def voto (nacimento):
    global ano_nascimento
    global ano_atual
    idade = ano_atual - ano_nascimento
    if idade < 18:
        print(f'Com {idade} anos seu voto é opcional')
    elif 65 > idade >= 18:
        print(f'Com {idade} anos seu voto é obrigatório')
    elif idade >= 65:
        print(f'Com {idade} anos seu voto é opcional')        
        

ano_nascimento = int(input('Digite seu ano de nascimento: '))
voto(ano_nascimento)


