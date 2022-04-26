nome = str(input('Qual é seu nome? ')).title().strip()
if nome == 'Matheus':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome =='João':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))