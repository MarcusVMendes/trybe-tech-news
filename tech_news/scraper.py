import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
