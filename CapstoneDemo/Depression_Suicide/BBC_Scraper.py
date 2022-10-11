from bs4 import BeautifulSoup as bs
import requests


class bbcScraper:
    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")

        self.body = self.getBody()
        self.title = self.getTitle()

    def getBody(self) -> list:
        body = self.soup.find(property="articleBody")
        return [p.text for p in body.find_all("p")]

    def getTitle(self) -> str:
        return self.soup.find(class_="story-body__h1").text


parsed = bbcScraper("https://www.bbc.com/news/world-us-canada-63036617")
parsed.title
parsed.body
