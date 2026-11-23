import re
from app.feeds.parser import fetch_feed

RSS_URL = "https://isc.sans.edu/rssfeed.xml"


def get_sans():
    return fetch_feed(RSS_URL, "SANS ISC")