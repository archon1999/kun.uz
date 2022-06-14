# Generated by Django 4.0.4 on 2022-06-13 13:12

import datetime
from django.db import migrations, models
import django.db.models.manager
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('tags', models.CharField(max_length=1000)),
                ('published', models.DateTimeField(default=datetime.datetime(2022, 6, 13, 13, 12, 27, 762846, tzinfo=utc))),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['published'],
            },
            managers=[
                ('news', django.db.models.manager.Manager()),
            ],
        ),
    ]
