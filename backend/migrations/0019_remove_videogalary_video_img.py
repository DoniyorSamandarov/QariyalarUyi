# Generated by Django 3.1 on 2021-12-17 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_photogalary_photo_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogalary',
            name='video_img',
        ),
    ]
