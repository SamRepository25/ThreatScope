from app.feeds.parser import fetch_feed

RSS_URL = "https://www.darkreading.com/rss.xml"


def get_darkreading():
    return fetch_feed(RSS_URL, "Dark Reading")