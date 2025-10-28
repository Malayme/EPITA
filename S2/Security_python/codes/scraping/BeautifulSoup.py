from bs4 import BeautifulSoup
import requests

proxies = {"http":"120.234.135.251:9002"}
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebkit/537.36 (KHTML,  like Gecko) Chrome/112.0.0.0 Safari/537.36"}
FILE = "Epita.html"

with open(FILE) as f:
    soup = BeautifulSoup(f, features="html.parser")

print(soup.title)
print("=" * 64)
print(soup.title.string)
print("=" * 64)
print("=" * 64)
print(soup.prettify())
print("=" * 64)
print(soup.get_text())

for script in soup.find_all("script"):
    print(script.get('src'))
    print("-" * 64)
print("=" * 64)

for cell in soup.find_all("td"):
    print(cell)
    print("-" * 64)
else:
    print("no cell")
