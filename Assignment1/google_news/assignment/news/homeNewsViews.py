import feedparser


def parseRSS(rss_url):
    return feedparser.parse(rss_url)


def getHeadlines(rss_url):
    headlines = []

    feed = parseRSS(rss_url)
    for news_item in feed['items']:
        headlines.append(news_item['title'])
    return headlines


all_headlines = []

news_urls = {
    'googlenews': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US'
}

for key, url in news_urls.items():

    all_headlines.extend(getHeadlines(url))

for hl in all_headlines:
    print(hl)
print(url)
