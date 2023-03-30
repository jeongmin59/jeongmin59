import feedparser

URL="https://ggong59.tistory.com//rss"
RSS_FEED = feedparser.parse(URL)

print(RSS_FEED)
