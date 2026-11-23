from app.feeds.parser import fetch_feed

RSS_URL = "https://www.bleepingcomputer.com/feed/"


def get_bleepingcomputer():
    """
    Fetch the latest articles from BleepingComputer RSS feed.

    Returns:
        list: A list of article dictionaries.
    """
    return fetch_feed(RSS_URL, "BleepingComputer")