from pprint import pprint

import feedparser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import views
# from .serializers import NewsSerializer


class HomeNewsSet(views.APIView):

    @csrf_exempt
    def get(self, request):
        result = []
        url = 'https://news.google.com/news/rss/topstories?tab=rn&hl=ja&gl=JP&ceid=JP:ja'
        for entry in feedparser.parse(url).entries:
            # print(entry.title)
            result.append(entry.title)
            pprint(entry)
        return Response(result)


# def parseRSS(rss_url):
#     return feedparser.parse(rss_url)
#
#
# def getHeadlines(rss_url):
#     headlines = []
#
#     feed = parseRSS(rss_url)
#     for news_item in feed['items']:
#         headlines.append(news_item['title'])
#     return headlines
#
#
# all_headlines = []
#
# news_urls = {
#     'googlenews': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US'
# }
#
# for key, url in news_urls.items():
#
#     all_headlines.extend(getHeadlines(url))
#
# for hl in all_headlines:
#     print(hl)
