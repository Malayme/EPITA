import requests

#r = requests.get("https://bing.com")
proxies = {"http":"120.234.135.251:9002"}
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

r = requests.get("https://epita.fr", proxies=proxies, headers=headers)

print(r.text)
for cookie in r.cookies:
    print(cookie)

f = open("Epita.html", "a")
f.write(r.text)
#f.write(str(cookie))
f.close()
