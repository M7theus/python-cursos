#pessoas = {'nome': 'Matheus','sexo': 'M','idade':18}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#del pessoas['sexo']
#pessoas['nome'] = 'Gustavo'
#pessoas['peso'] = 57
'''for k,v in pessoas.items():
    print(f'{k} = {v}')'''
    
'''brasil = []
estado = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado_2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado)
brasil.append(estado_2)
print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)