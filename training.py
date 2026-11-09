from os import link

from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('.titleline > a')

votes = soup.select('.subline .score ')

title_list = []
vote_list = []
link_list = []

for vote in votes:
    a = vote.text.split()[0]
    vote_list.append(int(a))

for t in titles:
    title_list.append(t.text)
    link_list.append(t.get("href"))

print(title_list)
print(vote_list)
print(link_list)

highest = 0

for vote in vote_list:
    if vote > highest:
        highest = vote
    else:
        pass

index = vote_list.index(highest)
print(f"highest voted post is '{title_list[index]}',{link_list[index]}'with {vote_list[index]} votes")
