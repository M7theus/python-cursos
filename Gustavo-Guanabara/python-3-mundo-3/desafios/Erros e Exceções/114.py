import requests

response = requests.get('http://pudim.com.br/')
if response:
    print('Certo')
else:
    print('Inválido')