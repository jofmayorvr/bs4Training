from bs4 import BeautifulSoup

with open("website.html") as file:
    html = file.read()


soup = BeautifulSoup(html, "html.parser")

#print(soup.title.string)
#print(soup.prettify())

for p in soup.find_all('a'):
    print(p.get("href"))


heading = soup.find(name = 'h3', class_ = "heading")

print(heading)
