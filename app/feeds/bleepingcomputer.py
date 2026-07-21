from app.feeds.parser import parse_rss

RSS_URL = "https://www.bleepingcomputer.com/feed/"


def get_news(limit=5):
    return parse_rss(
        RSS_URL,
        "BleepingComputer",
        limit,
    )