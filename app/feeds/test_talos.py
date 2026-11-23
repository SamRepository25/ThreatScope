import requests
import feedparser

url = "https://blog.talosintelligence.com/rss"

response = requests.get(url, timeout=20)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("\nFirst 1000 characters:\n")
print(response.text[:1000])

print("\n----------------------------")

feed = feedparser.parse(response.text)

print("Bozo:", feed.bozo)
if feed.bozo:
    print("Exception:", feed.bozo_exception)

print("Feed title:", getattr(feed.feed, "title", "Unknown"))
print("Entries:", len(feed.entries))