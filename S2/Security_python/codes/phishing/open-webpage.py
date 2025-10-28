import urllib.request, urllib.error, urllib.parse
import requests


url = 'https://epita.fr'

reponse = urllib.request.urlopen(url)
contenu_web = reponse.read().decode('UTF-8')

print(contenu_web[0:300])
