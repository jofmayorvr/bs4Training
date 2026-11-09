from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

titles = soup.find_all("h3",class_="title")
titles.reverse()

movie_title_list = []

for title in titles:
    movie_title_list.append(title.text)

with open('movie_title_list.txt', 'w') as f:
    for title in movie_title_list:
        f.write(f"{title}" + '\n')