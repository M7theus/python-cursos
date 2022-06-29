import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Acesso não deu certo')
else:
    print('Conseguir acessar!')