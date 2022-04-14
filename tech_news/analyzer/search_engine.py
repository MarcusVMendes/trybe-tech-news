from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
