import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
    except requests.ReadTimeout:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    html_selector = Selector(text=html_content)
    css_selector = ".entry-title a::attr(href)"
    news_links = html_selector.css(css_selector).getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    html_selector = Selector(text=html_content)
    css_selector = ".nav-links .next::attr(href)"
    next_link = html_selector.css(css_selector).get()
    return next_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# if __name__ == "__main__":
#     response = fetch("https://blog.betrybe.com/")
#     print(scrape_next_page_link(response))
