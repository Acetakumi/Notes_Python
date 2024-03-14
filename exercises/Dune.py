import requests

from bs4 import BeautifulSoup

URL = "https://allnovel.net/dune-dune-chronicles-1/page-1.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
book = soup.find(class_="des_novel")



paragraphes = book.find_all("p")
paragraphes = list(paragraphes)

for i in range(0,len(paragraphes),1):
    paragraphes[i] = str(paragraphes[i]) .replace("<p>","\n")
    paragraphes[i] = str(paragraphes[i]) .replace("</p>","\n")
print(paragraphes)