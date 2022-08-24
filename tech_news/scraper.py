import time
import requests
from parsel import Selector
from tech_news.helpers.format_scrape_noticia import (
    format_comments_count,
    format_summary
)


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
    html_selector = Selector(text=html_content)
    url = html_selector.css('head link[rel="canonical"]::attr(href)').get()
    title = html_selector.css(".entry-header-inner .entry-title::text").get()
    timestamp = html_selector.css(".post-meta .meta-date::text").get()
    writer = html_selector.css(".post-meta .meta-author .author a::text").get()
    comments_count = html_selector.css("#comments .title-block::text").get()
    summary = (
        html_selector.css(".entry-content > p:first-of-type *::text").getall())
    tags = html_selector.css(".post-tags li a::text").getall()
    category = html_selector.css(".category-style .label::text").get()

    noticia = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": format_comments_count(comments_count),
        "summary": format_summary(summary),
        "tags": tags,
        "category": category,
    }
    return noticia


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# if __name__ == "__main__":
#     url = "https://blog.betrybe.com/carreira/gatilho-mental-tudo-sobre/&#39;"
#     response = fetch(url)
#     print(scrape_noticia(response))
