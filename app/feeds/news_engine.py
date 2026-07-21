from app.feeds.hackernews import get_news as hacker_news
from app.feeds.bleepingcomputer import get_news as bleeping_news
from app.feeds.securityweek import get_news as securityweek_news


def get_all_news(limit_per_source=3):

    articles = []

    articles.extend(hacker_news(limit_per_source))
    articles.extend(bleeping_news(limit_per_source))
    articles.extend(securityweek_news(limit_per_source))

    return articles