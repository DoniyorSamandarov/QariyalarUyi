# Generated by Django 3.1 on 2021-12-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_videogalary_video_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donat',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]
