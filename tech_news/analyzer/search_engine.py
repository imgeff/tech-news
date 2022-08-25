from datetime import date, datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_by_title = search_news({"title": {"$regex": title, "$options": "i"}})
    result_search = [
        (new["title"], new["url"]) for new in news_by_title
    ]
    return result_search


# Requisito 7
def search_by_date(date):
    try:
        date_fromisoformat = datetime.fromisoformat(str(date))
        date_formated = date_fromisoformat.strftime("%d/%m/%Y")
        news_by_date = search_news({"timestamp": date_formated})
        result_search = [
            (new["title"], new["url"]) for new in news_by_date
        ]
        return result_search
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    print(search_by_date(date(2021, 4, 4)))
