# Generated by Django 3.1 on 2021-12-03 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
    ]
