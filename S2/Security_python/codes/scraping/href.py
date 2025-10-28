from bs4 import BeautifulSoup
import requests

proxies = {"http":"120.234.135.251:9002"}
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebkit/537.36 (KHTML,  like Gecko) Chrome/112.0.0.0 Safari/537.36"}
FILE = "Epita.html"

with open(FILE) as f:
     soup = BeautifulSoup(f, features="html.parser")

count = 0

for elt in soup.find_all('a',href=True):
    print(elt["href"])
    try:
        r = requests.get(elt["href"], proxies=proxies,headers=headers)
        f = open(str(count)+"html", "a")
        f.write(r.text)
        #f.write(str(cookie))
        f.close()
        count = count+1
    except:
        pass
