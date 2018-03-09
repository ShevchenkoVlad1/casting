# Generated by Django 2.0 on 2018-03-08 21:51

import casting.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0015_auto_20180308_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=casting.models.get_film_photo_path)),
            ],
        ),
    ]
