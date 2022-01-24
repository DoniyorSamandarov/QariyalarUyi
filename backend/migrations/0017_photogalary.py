# Generated by Django 3.1 on 2021-12-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20211208_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_title', models.CharField(max_length=255)),
                ('photoo', models.ImageField(default='imges/default.jpg', upload_to='images/')),
            ],
            options={
                'verbose_name': 'Rasm',
                'verbose_name_plural': 'Rasmlar',
            },
        ),
    ]
