import json

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse

from .models import News


def get_last_news(request):
    last_news = News.news.all().reverse()[:3]
    news_dict = dict()
    for news in last_news.values():
        news_dict[news['url']] = news

    return JsonResponse(news_dict)


def get_popular_news(request):
    last_news = News.news.order_by('-views')[:3]
    news_dict = dict()
    for news in last_news.values():
        news_dict[news['url']] = news

    return JsonResponse(news_dict)
    response = HttpResponse(json.dumps(news_dict, default=str))
    response.headers['Content-Type'] = 'application/json'
    return response
