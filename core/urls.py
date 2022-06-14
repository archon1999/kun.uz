from django.contrib import admin
from django.urls import path

from backend.views import get_last_news, get_popular_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('last-news', get_last_news),
    path('popular-news', get_popular_news)
]
