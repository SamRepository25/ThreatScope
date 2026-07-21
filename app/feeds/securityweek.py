from app.feeds.parser import parse_rss

RSS_URL = "https://feeds.feedburner.com/securityweek"


def get_news(limit=5):
    return parse_rss(
        RSS_URL,
        "SecurityWeek",
        limit,
    )