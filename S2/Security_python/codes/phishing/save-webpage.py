import requests #, urllib.request, urllib.error, urllib.parse

proxies = {"http":"120.234.135.251:9002"}
#headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

r = requests.get("https://epita.fr", proxies=proxies) #, headers=headers)

#url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

#reponse = urllib.request.urlopen(url)
#contenu_web = reponse.read().decode('UTF-8')

f = open('epita.html', 'w')
f.write(r.text)
f.close()
