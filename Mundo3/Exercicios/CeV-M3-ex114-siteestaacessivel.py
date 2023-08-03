import urllib
from urllib import request

try:
    site = request.urlopen('http://pudim.com.br/')
except (urllib.error.URLError):
    print('O site stá inacessível.')
else:
    print('O site stá acessível.')