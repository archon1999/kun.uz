import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from django.utils import timezone

from .models import News


BASE_URL = 'https://kun.uz/'


def get_html(url):
    response = requests.get(url)
    if response.ok:
        return response.text


def parse_and_create_news(news_url):
    html = get_html(news_url)
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find(class_='single-header__title').text.strip()
    body = str(soup.find(class_='single-content'))
    views = int(soup.find(class_='view').text.strip())
    tags = soup.find(class_='tags-ui__items').text.strip()

    return News.news.create(
        url=news_url,
        title=title,
        body=body,
        views=views,
        tags=tags,
    )


def parse_last_news():
    if (news := News.news.last()):
        last_news_dt = news.published
    else:
        last_news_dt = timezone.now() - timezone.timedelta(minutes=120)

    last_news_dt = timezone.make_naive(last_news_dt,
                                       timezone.utc)
    last_news_dt += timezone.timedelta(hours=5)
    news_url = urljoin(BASE_URL, '/uz/news/list')
    html = get_html(news_url)
    soup = BeautifulSoup(html, 'lxml')

    for news_tag in soup.find_all(class_='daily-block'):
        news_time_tag = news_tag.find(class_='news-date')
        news_time = news_time_tag.text.strip()
        hour, minute = map(int, news_time.split(':'))
        now = datetime.datetime.now()
        news_dt = timezone.datetime(
            year=now.year,
            month=now.month,
            day=now.day,
            hour=hour,
            minute=minute,
        )
        if news_dt <= last_news_dt:
            break

        news_url = urljoin(BASE_URL, news_tag.get('href'))
        news = parse_and_create_news(news_url)
        news.published = news_dt
        news.save()


def parse_view(news: News):
    html = get_html(news.url)
    soup = BeautifulSoup(html, 'lxml')
    return int(soup.find(class_='view').text.strip())


def update_views():
    for news in News.news.all():
        views = parse_view(news)
        news.views = views
        news.save()


def delete_old_news():
    News.news.filter(
        published__lt=timezone.now()-timezone.timedelta(days=7)
    ).delete()
