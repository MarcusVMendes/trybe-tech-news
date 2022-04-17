from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = search_news({
        "title": {
            "$regex": title, "$options": "i"
        }
    })
    news = []
    for item in query:
        news.append((item["title"], item["url"]))
    return news


# Requisito 7
def search_by_date(date):
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            query = search_news({
                "timestamp": {
                    "$regex": date
                }
            })
            news = []
            for item in query:
                news.append((item["title"], item["url"]))
            return news
    except ValueError:
        raise ValueError("Data inválida")


# strptime - validar data
# https://pt.stackoverflow.com/questions/377579/valida%C3%A7%C3%A3o-de-data-testes-com-python


# Requisito 8
def search_by_source(source):
    query = search_news({
        "sources": {
            "$elemMatch": {
                "$regex": source, "$options": "i"
            }
        }
    })
    news = []
    for item in query:
        news.append((item["title"], item["url"]))
    return news


# Requisito 9
def search_by_category(category):
    query = search_news({
        "categories": {
            "$elemMatch": {
                "$regex": category, "$options": "i"
            }
        }
    })
    news = []
    for item in query:
        news.append((item["title"], item["url"]))
    return news
