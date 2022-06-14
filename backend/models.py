from django.db import models
from django.utils import timezone


class News(models.Model):
    news = models.Manager()
    url = models.URLField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    views = models.IntegerField(default=0)
    tags = models.CharField(max_length=1000)
    published = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['published']

    def __str__(self):
        return self.title
