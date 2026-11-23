from app.feeds.parser import fetch_feed

RSS_URL = "https://feeds.feedburner.com/TheHackersNews"


def get_hackernews():
    """
    Fetch the latest articles from The Hacker News RSS feed.
    """
    return fetch_feed(RSS_URL, "The Hacker News")