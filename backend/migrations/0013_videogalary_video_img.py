# Generated by Django 3.1 on 2021-12-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_videogalary'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogalary',
            name='video_img',
            field=models.ImageField(default='imges/default.jpg', upload_to='images/'),
        ),
    ]