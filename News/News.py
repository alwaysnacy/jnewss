import requests
from bs4 import BeautifulSoup
import json
from Article import Article

baseUrl = "https://vnexpress.net/"


def GetNews(limit_news=20):  # the number of news we want
    s = requests.Session()  # Store the session
    response = s.get(baseUrl)  # GET request
    soup = BeautifulSoup(response.content, 'html.parser')  # convert the response to BS4 object
    article = soup.select("article.item-news", limit=limit_news)  # get the data in the article tag

    listArticle = []
    for element in article:
        title = element.select("h3.title-news > a")  # get the title tag
        description = element.select("p.description > a")  # Lấy the description class
        for x in range(len(title)): # serialize this object to JSON
            listArticle.append(json.dumps(Article(title[x]['title'], title[x]['href'], description[x].text).__dict__, ensure_ascii=False))
    return listArticle
