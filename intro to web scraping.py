from bs4 import BeautifulSoup
# Use when working with XML websites, instead of html.parser type lmxl
import lxml

# Format to open a html document
with open("website.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser", from_encoding="utf-8")

# '.name' (name of tag used), '.string' (name within the tags)
# print(soup.title)
# print(soup.title.string)

# finds all the tags with p
soup.find_all(name="p")

# finds all the tags with a (find_all turns it in a list).
all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
    # print(tag.getText())    # gets the text between all anchor tags
    # print(tag.get("href"))  # gets the text for all href Attributes (the link)


heading = soup.find(name="h1", id="name")   #same for class attribute too
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)  # we can apply the methods for soup, to our variable (section_heading.get()) as an eg.

# select anchor within paragraph
company_url = soup.select_one(selector="p a")
# print(company_url)

# select #main
name = soup.select_one(selector="#main")
# print(name)







