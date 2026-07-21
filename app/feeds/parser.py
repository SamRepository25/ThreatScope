import feedparser


def parse_rss(url: str, source: str, limit: int = 5):
    """
    Parse an RSS feed and return articles in a standard format.
    """

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries[:limit]:
        articles.append(
            {
                "source": source,
                "title": entry.title,
                "link": entry.link,
            }
        )

    return articles