import requests
from bs4 import BeautifulSoup

# TODO: Write a '.txt' file containing all 100 films from 100 Movies website

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/#expand"
response = requests.get(url=URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")
movie_tags = soup.find_all(name="h3", class_="title")
movie_tags.reverse()


all_movies = [] # Stores all movie names in string format
for each_movie in movie_tags:
    all_movies.append(each_movie.getText())

# all_movies contains each film 1-100

# Adds each film
# I was receiving a Traceback error, hence the encoding attribute.
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for each_film in all_movies:
        file.write(f"{each_film}\n")

