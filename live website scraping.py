from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text    # Code that represents the webpage

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(article_tag)
    link = article_tag.get("href")
    article_links.append(link)

# int format for upvote splitting 'points
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Alternatively, use the index method (number of where it is in the list)
print(article_texts[27].getText())
print(article_links[27])
print(max(article_upvotes))




