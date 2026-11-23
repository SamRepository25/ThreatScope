import time

# Cache lifetime (5 minutes)
CACHE_DURATION = 300

# Cached news
_cached_news = None

# Timestamp when cache was created
_cached_at = 0


def get_cached_news():
    """
    Return cached news if it is still valid.
    Returns None if cache has expired.
    """
    global _cached_news, _cached_at

    if _cached_news is None:
        return None

    if time.time() - _cached_at > CACHE_DURATION:
        _cached_news = None
        _cached_at = 0
        return None

    return _cached_news


def set_cached_news(news):
    """
    Store news in cache.
    """
    global _cached_news, _cached_at

    _cached_news = news
    _cached_at = time.time()


def clear_cache():
    """
    Manually clear the cache.
    """
    global _cached_news, _cached_at

    _cached_news = None
    _cached_at = 0