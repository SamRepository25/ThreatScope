from app.feeds.hackernews import get_hackernews
from app.feeds.bleepingcomputer import get_bleepingcomputer
from app.feeds.securityweek import get_securityweek

print("Hacker News:", len(get_hackernews()))
print("BleepingComputer:", len(get_bleepingcomputer()))
print("SecurityWeek:", len(get_securityweek()))