from app.feeds.news_engine import get_all_news

articles = get_all_news()

print(f"Total Articles: {len(articles)}")

if articles:
    first = articles[0]

    print("\nFirst Article")
    print(f"Source: {first['source']}")
    print(f"Title: {first['title']}")
    print(f"Published: {first['published']}")
    print(f"Link: {first['link']}")