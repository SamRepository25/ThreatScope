import requests
import feedparser

url = "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml"

response = requests.get(url, timeout=20)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print(response.text[:500])

feed = feedparser.parse(response.text)

print("\nBozo:", feed.bozo)
if feed.bozo:
    print("Exception:", feed.bozo_exception)

print("Feed title:", feed.feed.get("title"))
print("Entries:", len(feed.entries))