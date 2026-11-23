from app.feeds.parser import fetch_feed

RSS_URL = "https://krebsonsecurity.com/feed/"


def get_krebs():
    return fetch_feed(RSS_URL, "Krebs on Security")