from pprint import pprint

import feedparser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import views
# from .serializers import NewsSerializer


class HomeNewsSet(views.APIView):

    @csrf_exempt
    def get(self, request):
        titles = []
        urls = []
        url = 'https://news.google.com/news/rss/topstories?tab=rn&hl=ja&gl=JP&ceid=JP:ja'
        for entry in feedparser.parse(url).entries:
            titles.append(entry.title)
            urls.append(entry.link)
        return Response(titles)


class AbroadNewsSet(views.APIView):

    @csrf_exempt
    def get(self, request):
        titles = []
        url = 'https://news.google.com/news/rss/headlines/section/topic/WORLD?hl=ja&gl=JP&ceid=JP:ja'
        for entry in feedparser.parse(url).entries:
            titles.append(entry.title)
        return Response(titles)


class JapanNewsSet(views.APIView):

    @csrf_exempt
    def get(self, request):
        titles = []
        url = 'https://news.google.com/news/rss/headlines/section/topic/NATION?hl=ja&gl=JP&ceid=JP:ja'
        for entry in feedparser.parse(url).entries:
            titles.append(entry.title)
        return Response(titles)


class LocalNewsSet(views.APIView):

    @csrf_exempt
    def get(self, request):
        titles = []
        url = 'https://news.google.com/news/rss/headlines/section/geo/tokyo?hl=ja&gl=JP&ceid=JP:ja'
        for entry in feedparser.parse(url).entries:
            titles.append(entry.title)
        return Response(titles)


class BusinessNewsSet(views.APIView):

    @csrf_exempt
    def get(self, request):
        titles = []
        url = 'https://news.google.com/news/rss/headlines/section/topic/BUSINESS?hl=ja&gl=JP&ceid=JP:ja'
        for entry in feedparser.parse(url).entries:
            titles.append(entry.title)
        return Response(titles)


class ScienceNewsSet(views.APIView):
    print("sss")

    @csrf_exempt
    def get(self, request):
        titles = []
        url = 'https://news.google.com/news/rss/headlines/section/topic/SCIENCE?hl=ja&gl=JP&ceid=JP:ja'
        for entry in feedparser.parse(url).entries:
            titles.append(entry.title)
        return Response(titles)


class GossipNewsSet(views.APIView):

    @csrf_exempt
    def get(self, request):
        titles = []
        url = 'https://news.google.com/news/rss/headlines/section/topic/ENTERTAINMENT?hl=ja&gl=JP&ceid=JP:ja'
        for entry in feedparser.parse(url).entries:
            titles.append(entry.title)
        return Response(titles)


class SportsNewsSet(views.APIView):

    @csrf_exempt
    def get(self, request):
        titles = []
        url = 'https://news.google.com/news/rss/headlines/section/topic/SPORTS?hl=ja&gl=JP&ceid=JP:ja'
        for entry in feedparser.parse(url).entries:
            titles.append(entry.title)
        return Response(titles)