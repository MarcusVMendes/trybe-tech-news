import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    links = []
    selector = Selector(html_content)
    if len(html_content) == 0:
        return links
    for item in selector.css(".tec--list__item"):
        links.append(item.css(".tec--card__title__link::attr(href)").get())
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    if len(html_content) == 0:
        return None
    selector = Selector(html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css(".tec--article__header__title::text").get()
    ts = selector.css("time::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn")
    summary = "".join(selector.css(
        ".tec--article__body > p:nth-child(1) *::text").getall())
    sources = selector.css(
        '.tec--badge[rel="noopener nofollow"]::text').getall()
    categories = selector.css("#js-categories a::text").getall()
    if type(shares_count) == str:
        shares_count = int(shares_count[1])
    if comments_count:
        comments_count = int(comments_count.attrib["data-count"])
    if type(categories) == list:
        categories = [item.strip() for item in categories]
    return {
        "url": url,
        "title": title,
        "timestamp": ts,
        "writer": writer.strip() if type(writer) is str else None,
        "shares_count": shares_count if shares_count is not None else 0,
        "comments_count": comments_count if type(comments_count) is int else 0,
        "summary": summary,
        "sources": [item.strip() for item in sources],
        "categories": categories
    }


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://www.tecmundo.com.br/novidades")
    news = scrape_novidades(html_content)
    news_list = []
    if len(news) < amount:
        links = scrape_novidades(fetch(scrape_next_page_link(html_content)))
        for link in links:
            news.append(link)
    for link in news:
        if len(news_list) < amount:
            html = fetch(link)
            news_list.append(scrape_noticia(html))
    create_news(news_list)
    return news_list
