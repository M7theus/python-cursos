def voto(ano):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} você ainda não pode votar'
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} seu voto é opcional'
    else:
        return f'Com {idade} seu voto é obrigatório'        

nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))


