import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://eventum.pucpr.br/eventos')
except:
    print('Deu erro')
else:
    print('Deu certo')