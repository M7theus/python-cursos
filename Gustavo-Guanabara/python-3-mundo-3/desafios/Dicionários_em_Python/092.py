from datetime import datetime
ano_atual = datetime.now().year

dados = dict()
dados['nome'] = str(input('Digite seu nome: ')).strip().title()
ano_nascimento = int(input('Digite seu ano de nascimento: '))
dados['idade'] = ano_atual - ano_nascimento
dados['ctps'] = int(input('Carteira de trabalho? ( 0 para parar ): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Digite o ano de contratação: '))
    dados['salário'] = int(input('Digite seu salário: '))
    dados['aposentadoria'] = ((dados['contratação'] + 35) - ano_nascimento)
print('-='*30)
for keys, values in dados.items():
    print(f'--> {keys} tem o valor: \033[1;32m{values}\033[m')
