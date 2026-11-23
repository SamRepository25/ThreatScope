from app.feeds.parser import fetch_feed

RSS_URL = "https://feeds.feedburner.com/securityweek"


def get_securityweek():
    """
    Fetch the latest articles from SecurityWeek RSS feed.

    Returns:
        list: A list of article dictionaries.
    """
    return fetch_feed(RSS_URL, "SecurityWeek")