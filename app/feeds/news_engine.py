from app.feeds.hackernews import get_hackernews
from app.feeds.bleepingcomputer import get_bleepingcomputer
from app.feeds.securityweek import get_securityweek
from app.feeds.sans import get_sans
from app.feeds.krebs import get_krebs
from app.feeds.darkreading import get_darkreading
from app.feeds.talos import get_talos

from app.cache.news_cache import (
    get_cached_news,
    set_cached_news,
)

import logging

logger = logging.getLogger(__name__)


def get_all_news(limit: int = 10):
    """
    Fetch news from all configured cybersecurity sources.

    - Fetches all feeds
    - Removes duplicate links
    - Sorts articles by publication date (newest first)
    - Caches results for 5 minutes
    - Returns the latest articles

    Args:
        limit (int): Maximum number of articles to return.

    Returns:
        list: List of unique, sorted articles.
    """

    # Return cached news if available
    cached_news = get_cached_news()

    if cached_news is not None:
        logger.info("Returning news from cache.")
        return cached_news[:limit]

    articles = []

    sources = [
        get_hackernews,
        get_bleepingcomputer,
        get_securityweek,
        get_sans,
        get_krebs,
        get_darkreading,
        get_talos,
    ]

    for source in sources:
        try:
            articles.extend(source())
        except Exception:
            logger.exception(f"Failed to fetch {source.__name__}")

    logger.info(f"Fetched {len(articles)} total articles.")

    # Remove duplicate links
    seen_links = set()
    unique_articles = []

    for article in articles:
        link = article.get("link")

        if not link or link in seen_links:
            continue

        seen_links.add(link)
        unique_articles.append(article)

    # Sort newest first
    unique_articles.sort(
        key=lambda article: article.get("published_datetime"),
        reverse=True,
    )

    # Save to cache
    set_cached_news(unique_articles)

    logger.info("News cache updated.")

    return unique_articles[:limit]