from app.feeds.parser import fetch_feed

RSS_URL = "https://www.cisa.gov/cybersecurity-advisories/all.xml"


def get_cisa():
    """
    Fetch the latest Cybersecurity Advisories from CISA.
    """
    return fetch_feed(RSS_URL, "CISA")