import logging
import feedparser
from datetime import datetime
from zoneinfo import ZoneInfo
import re

logger = logging.getLogger(__name__)


def clean_title(title: str, source: str) -> str:
    """
    Clean RSS titles. Currently only applies cleanup for SANS ISC.
    """
    if not title:
        return ""

    if source == "SANS ISC":
        # Remove embedded URLs
        title = re.sub(r"https?://\S+", "", title)

        # Remove trailing date in parentheses
        title = re.sub(r"\s*\([^)]*\)\s*$", "", title)

        # Remove extra whitespace
        title = re.sub(r"\s+", " ", title).strip()

        # Remove trailing commas
        title = title.rstrip(",")

    return title


def fetch_feed(url: str, source: str) -> list:
    """
    Fetch and parse an RSS feed.

    Args:
        url (str): RSS feed URL.
        source (str): News source name.

    Returns:
        list: List of article dictionaries.
    """
    try:
        logger.info(f"Fetching {source} feed...")

        feed = feedparser.parse(url)

        # Debug information
        logger.info("=" * 60)
        logger.info(f"Source       : {source}")
        logger.info(f"Feed Title   : {feed.feed.get('title', 'Unknown')}")

        if feed.bozo:
            logger.warning(f"{source} feed has parsing warnings.")
            logger.warning(f"Bozo Exception: {feed.bozo_exception}")

        logger.info(f"Entries Found: {len(feed.entries)}")
        logger.info("=" * 60)

        if not feed.entries:
            logger.warning(f"No articles found for {source}.")
            return []

        articles = []

        for entry in feed.entries:
            # Get published time (fallback to updated time)
            published_parsed = (
                entry.get("published_parsed")
                or entry.get("updated_parsed")
            )

            if published_parsed:
                # RSS timestamps are generally in UTC
                published_datetime = (
                    datetime(*published_parsed[:6], tzinfo=ZoneInfo("UTC"))
                    .astimezone(ZoneInfo("Asia/Kolkata"))
                )
                published_text = published_datetime.strftime(
                    "%d %b %Y, %I:%M %p IST"
                )
            else:
                published_datetime = datetime.min.replace(
                    tzinfo=ZoneInfo("Asia/Kolkata")
                )
                published_text = "Unknown Date"

            article = {
                "source": source,
                "title": clean_title(
                    entry.get("title", "No Title"),
                    source,
                ),
                "link": entry.get("link", ""),
                "published": published_text,
                "published_datetime": published_datetime,
                "summary": (
                    entry.get("summary")
                    or entry.get("description")
                    or "No Summary"
                ),
            }

            articles.append(article)

        logger.info(f"Retrieved {len(articles)} articles from {source}.")
        return articles

    except Exception:
        logger.exception(f"Failed to fetch {source}")
        return []