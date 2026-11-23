from app.feeds.parser import fetch_feed

RSS_URL = "https://blog.talosintelligence.com/rss"


def get_talos():
    return fetch_feed(RSS_URL, "Cisco Talos")