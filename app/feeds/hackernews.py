from app.feeds.parser import parse_rss

RSS_URL = "https://feeds.feedburner.com/TheHackersNews"


def get_news(limit=5):
    return parse_rss(
        RSS_URL,
        "The Hacker News",
        limit,
    )